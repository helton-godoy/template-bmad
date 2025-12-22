
import argostranslate.package
import argostranslate.translate
import re

# Setup
def setup_argos():
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    pkg = next(filter(lambda x: x.from_code == 'en' and x.to_code == 'pt', available_packages))
    argostranslate.package.install_from_path(pkg.download())

# Since we are in the env, assume installed models (or rely on existing ones to save time)
# Quick check if installed
try:
    installed = argostranslate.package.get_installed_packages()
    if not any(x.from_code == 'en' and x.to_code == 'pt' for x in installed):
        print("Model not found, skipping install for speed (assuming existing env has it)")
except:
    pass

def translate(text):
    return argostranslate.translate.translate(text, 'en', 'pt')

text_original = "Welcome to the **production environment** of the BMAD System."

# Strategy 1: Padding (Current - Failed)
text_pad = "Welcome to the ** production environment ** of the BMAD System."
trans_pad = translate(text_pad)
print(f"Padding: {trans_pad}")

# Strategy 2: Symbols (★)
text_sym = "Welcome to the ★production environment★ of the BMAD System."
trans_sym = translate(text_sym)
print(f"Symbols: {trans_sym}")

# Strategy 3: XML tags (<b>)
text_xml = "Welcome to the <b>production environment</b> of the BMAD System."
trans_xml = translate(text_xml)
print(f"XML:     {trans_xml}")

# Strategy 4: Quotes («)
text_quote = "Welcome to the «production environment» of the BMAD System."
trans_quote = translate(text_quote)
print(f"Quotes:  {trans_quote}")
