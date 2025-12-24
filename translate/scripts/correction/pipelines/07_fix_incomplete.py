#!/usr/bin/env python3
import os
import sys
from pathlib import Path

# Setup paths
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent.parent.parent
sys.path.append(str(project_root / 'translate' / 'src'))
sys.path.append(str(project_root / 'translate' / 'scripts'))

from bmad_translate.core.translator import BMADTranslator
from utils.state_manager import StateManager

def main():
    print("🚑 Starting incomplete file repair...")

    # Check if list exists
    list_file = Path('incomplete_files.txt')
    if not list_file.exists():
        print("No incomplete_files.txt found. Run audit first.")
        return

    translator = BMADTranslator()
    state = StateManager()

    with open(list_file, 'r') as f:
        files = [line.strip() for line in f if line.strip()]

    print(f"Found {len(files)} files to repair.")

    count = 0
    for source_file in files:
        if not os.path.exists(source_file):
            print(f"⚠️  Source not found: {source_file}")
            continue

        print(f"🔄 Re-translating: {os.path.basename(source_file)}...")

        result = translator.translate_file(source_file)

        if result.success:
            count += 1
            name, ext = os.path.splitext(source_file)
            target = Path(f"{name}{translator.settings.get_output_suffix()}{ext}")
            state.mark_file_processed(target, ["07_fix_incomplete.py"])
            print(f"  ✅ Fixed")
        else:
            print(f"  ❌ Failed: {result.error_message}")

    print(f"Repair complete. Processed {count} files.")

if __name__ == "__main__":
    main()
