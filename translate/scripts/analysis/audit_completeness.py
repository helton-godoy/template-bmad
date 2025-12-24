#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def audit_directory(base_dir):
    print(f"🔍 Auditing {base_dir}...")
    source_files = []
    # Collect source files (excluding _pt-br)
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if f.endswith('.md') and not f.endswith('_pt-br.md'):
                source_files.append(Path(root) / f)
            elif f.endswith('.yaml') and not f.endswith('_pt-br.yaml'):
                source_files.append(Path(root) / f)

    incomplete_files = []
    missing_files = []

    for source in source_files:
        name, ext = os.path.splitext(source)
        target = Path(f"{name}_pt-br{ext}")

        if not target.exists():
            # print(f"❌ Missing: {target.name}")
            missing_files.append(source)
            continue

        src_size = source.stat().st_size
        tgt_size = target.stat().st_size

        if src_size == 0:
            continue

        ratio = tgt_size / src_size

        # Heuristic: If target is < 60% of source, it's likely truncated.
        if ratio < 0.6:
            print(f"⚠️  Incomplete (Ratio {ratio:.2f}): {target.name} (Src: {src_size}, Tgt: {tgt_size})")
            incomplete_files.append(source)

    return incomplete_files, missing_files

def main():
    dirs = ['_bmad/core', '_bmad/bmm']
    all_incomplete = []
    all_missing = []

    for d in dirs:
        if os.path.exists(d):
            inc, miss = audit_directory(d)
            all_incomplete.extend(inc)
            all_missing.extend(miss)
        else:
            print(f"Directory not found: {d}")

    print("\n📊 Summary:")
    print(f"Missing: {len(all_missing)}")
    print(f"Incomplete: {len(all_incomplete)}")

    # Save list for repair script
    with open('incomplete_files.txt', 'w') as f:
        for p in all_incomplete + all_missing:
            f.write(str(p) + '\n')
    print("📝 List saved to incomplete_files.txt")

if __name__ == "__main__":
    main()
