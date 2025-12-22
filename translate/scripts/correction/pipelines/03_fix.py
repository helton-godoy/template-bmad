#!/usr/bin/env python3
import os
import sys
from pathlib import Path

# Ensure correct path for imports
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent.parent.parent
sys.path.append(str(project_root / 'translate' / 'src'))
sys.path.append(str(project_root / 'translate' / 'scripts'))

from bmad_translate.core.translator import BMADTranslator
from utils.state_manager import StateManager

def main():
    print("🚀 Iniciando pipeline de correção/tradução...")

    # Initialize components
    try:
        translator = BMADTranslator()
        state = StateManager()
    except Exception as e:
        print(f"❌ Erro ao inicializar componentes: {e}")
        sys.exit(1)

    source_dir = '_bmad'

    # Collect source files
    print(f"📂 Coletando arquivos em {source_dir}...")
    source_files = translator.collect_files(source_dir)

    if not source_files:
        print("⚠️  Nenhum arquivo encontrado para processar.")
        return

    print(f"found {len(source_files)} source files.")

    count = 0
    errors = 0

    for source_file in source_files:
        # Determine target file name logic (must match translator's logic)
        name, ext = os.path.splitext(source_file)
        # Translator adds suffix before extension
        suffix = translator.settings.get_output_suffix()
        target_file = f"{name}{suffix}{ext}"

        # Check if we should process
        # If the target file doesn't exist, we must translate.
        # If it exists, we check state.

        should_process = False
        if not os.path.exists(target_file):
            should_process = True
        elif not state.is_file_processed(Path(target_file)):
            should_process = True

        if not should_process:
            continue

        print(f"🔄 Traduzindo: {os.path.basename(source_file)}...")
        result = translator.translate_file(source_file)

        if result.success:
            state.mark_file_processed(Path(target_file), ["03_fix.py"])
            count += 1
            print(f"  ✅ Sucesso -> {os.path.basename(target_file)}")
        else:
            errors += 1
            print(f"  ❌ Falha: {result.error_message}")

    print(f"\n🏁 Concluído. Processados: {count}, Erros: {errors}")
    state.mark_script_executed("03_fix.py", count)

if __name__ == "__main__":
    main()
