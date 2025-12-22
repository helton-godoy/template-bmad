#!/usr/bin/env python3
import os
import sys
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
from pathlib import Path

# Setup paths
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent.parent.parent
sys.path.append(str(project_root / 'translate' / 'src'))
sys.path.append(str(project_root / 'translate' / 'scripts'))

from bmad_translate.core.translator import BMADTranslator
from utils.state_manager import StateManager

class AgentTranslator:
    def __init__(self):
        self.translator = BMADTranslator()
        # Suppress logging to console for translator to avoid noise?
        # But we need it initialized.

    def translate_xml_content(self, xml_string):
        try:
            # Wrap in dummy root if multiple roots? <agent> should be single root.
            # But xml_string might have whitespace/newlines around it.
            root = ET.fromstring(xml_string.strip())
        except ET.ParseError as e:
            print(f"  ❌ XML Parse Error: {e}")
            return xml_string

        self._recursive_translate_xml(root)

        # Serialize
        raw_xml = ET.tostring(root, encoding='unicode', method='xml')

        # Prettify?
        # ET.tostring creates minified XML usually.
        # We want to preserve structure if possible or re-indent.
        try:
            parsed = minidom.parseString(raw_xml)
            pretty_xml = parsed.toprettyxml(indent="  ")
            # Remove empty lines that minidom might add
            pretty_xml = '\n'.join([line for line in pretty_xml.split('\n') if line.strip()])
            # Remove <?xml ...?>
            pretty_xml = re.sub(r'<\?xml.*?\?>', '', pretty_xml).strip()
            return "\n" + pretty_xml + "\n"
        except Exception:
            return raw_xml

    def _recursive_translate_xml(self, node):
        if node.text and node.text.strip():
            if not self._is_technical(node.text):
                # Preserve leading/trailing whitespace
                stripped = node.text.strip()
                translated = self.translator._translate_text(stripped, protect=True)
                node.text = node.text.replace(stripped, translated)

        for attr, value in node.attrib.items():
            if attr in ['title', 'description']:
                node.attrib[attr] = self.translator._translate_text(value, protect=True)
            elif attr == 'action' and not value.startswith('#') and len(value.split()) > 1:
                 node.attrib[attr] = self.translator._translate_text(value, protect=True)

        for child in node:
            self._recursive_translate_xml(child)

        if node.tail and node.tail.strip():
             if not self._is_technical(node.tail):
                stripped = node.tail.strip()
                translated = self.translator._translate_text(stripped, protect=True)
                node.tail = node.tail.replace(stripped, translated)

    def _is_technical(self, text):
        text = text.strip()
        if not text: return True
        if text.startswith('{') and text.endswith('}'): return True

        # If it looks like a single path/filename
        if '/' in text or '\\' in text:
             # If it has spaces, it's probably a sentence containing a path
             if ' ' in text:
                 return False
             # If no spaces, assume it's a path/url/technical string
             return True

        if text.startswith('*') and not ' ' in text: return True # simple command
        if text == "MANDATORY": return False
        return False

    def process_file(self, filepath):
        # Check if file exists
        if not os.path.exists(filepath):
            return

        print(f"🔄 Processando agente: {filepath.name}")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        pattern = r'(```xml\s*)(.*?)(\s*```)'
        match = re.search(pattern, content, re.DOTALL)

        if not match:
            # Maybe it uses " ``` " without xml?
            # Or just check for <agent> tag
            return

        start_fence = match.group(1)
        xml_content = match.group(2)
        end_fence = match.group(3)

        translated_xml = self.translate_xml_content(xml_content)

        # Validate XML integrity before saving
        try:
            ET.fromstring(translated_xml.strip())
        except ET.ParseError as e:
            print(f"  ❌ Erro de validação XML: {e} - Mantendo original para evitar quebra")
            return

        new_content = content.replace(match.group(0), f"{start_fence}{translated_xml}{end_fence}")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("  ✅ Atualizado com sucesso")

    def run(self):
        base_dir = Path('_bmad/bmm/agents')
        files = list(base_dir.rglob('*_pt-br.md'))
        print(f"Encontrados {len(files)} agentes para corrigir.")
        for f in files:
            self.process_file(f)

if __name__ == "__main__":
    translator = AgentTranslator()
    translator.run()
