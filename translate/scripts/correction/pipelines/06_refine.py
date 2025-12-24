#!/usr/bin/env python3
import os
import sys
from pathlib import Path

# Setup paths
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent.parent.parent
sys.path.append(str(project_root / 'translate' / 'src'))
sys.path.append(str(project_root / 'translate' / 'scripts'))

from bmad_translate.core.refiner import BMADRefiner

def main():
    print("✨ Starting refinement process...")
    try:
        with BMADRefiner() as refiner:
            # Refine _bmad directory
            results = refiner.refine_directory('_bmad')
            print(f"Refinement complete. Processed {len(results)} files.")
    except Exception as e:
        print(f"❌ Refinement failed: {e}")

if __name__ == "__main__":
    main()
