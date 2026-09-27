#!/usr/bin/env python3
import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
import re

# Setup paths
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
sys.path.append(str(project_root / 'scripts'))

from utils.xml_security import safe_fromstring

def check_agents():
    base_dir = Path('_bmad/bmm/agents')
    if not base_dir.exists():
        print("⚠️  Agents directory not found")
        return

    files = list(base_dir.rglob('*_pt-br.md'))
    errors = 0
    print(f"🔍 Verifying {len(files)} agent files...")

    for f in files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()

        match = re.search(r'```xml(.*?)```', content, re.DOTALL)
        if match:
            xml_content = match.group(1).strip()
            try:
                # Wrap in fake root if needed? No, agent files have single root <agent>
                safe_fromstring(xml_content)
                print(f"✅ {f.name}: Valid XML")
            except ET.ParseError as e:
                print(f"❌ {f.name}: Invalid XML - {e}")
                errors += 1
        else:
            print(f"⚠️  {f.name}: No XML found")

    if errors > 0:
        print(f"❌ Found {errors} XML errors.")
        sys.exit(1)
    else:
        print("✅ All agents valid.")

if __name__ == "__main__":
    check_agents()
