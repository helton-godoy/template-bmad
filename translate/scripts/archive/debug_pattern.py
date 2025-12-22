
import re
from bmad_translate.core.protector import ContentProtector

# Protector internal logic loads the file relative to itself.
protector = ContentProtector()

# Add default protector patterns (manual copy for now or import if possible, but protector merges them)
# Let's use ContentProtector to be sure

test_str = "\n### "

print(f"Testing string: {repr(test_str)}")

for p in protector.patterns:
    pat = p['pattern']
    if re.search(pat, test_str):
        print(f"MATCH: {pat} ({p['description']})")

content = """
- "We are testing" -> "Estamos testando" (using proper aspect).

### Code Example
"""
print(f"\nProtecting content:\n{repr(content)}")
protected = protector.protect_content(content)
print(f"Protected:\n{repr(protected)}")
print(protector.get_placeholders())
