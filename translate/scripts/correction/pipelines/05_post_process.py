#!/usr/bin/env python3
import os
import sys
import re
from pathlib import Path

def fix_variables(content):
    # Fix {project- root} -> {project-root}
    content = re.sub(r'\{project-\s*root\}', '{project-root}', content)
    content = re.sub(r'\{user\s*name\}', '{user_name}', content)
    content = re.sub(r'\{nome\s*do\s*usuário\}', '{user_name}', content)
    content = re.sub(r'\{communication\s*language\}', '{communication_language}', content)
    content = re.sub(r'\{output\s*folder\}', '{output_folder}', content)
    content = re.sub(r'\{data\}', '{data}', content)

    # Fix paths with spaces
    # / bmad -> /_bmad
    content = re.sub(r'/\s*\\?\s*bmad', '/_bmad', content)
    content = re.sub(r'/\s*\\?\s*_bmad', '/_bmad', content)
    content = re.sub(r'bmad\s+/\s+bmm', '_bmad/bmm', content)

    return content

def main():
    base_dir = Path('_bmad')
    print("🧹 Executing post-processing...")
    files = list(base_dir.rglob('*_pt-br.md'))
    count = 0
    for f in files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()

        new_content = fix_variables(content)

        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Fixed {f.name}")
            count += 1
    print(f"Post-processing completed. Fixed {count} files.")

if __name__ == "__main__":
    main()
