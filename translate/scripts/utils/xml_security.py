import xml.etree.ElementTree as ET

try:
    from defusedxml import ElementTree as defused_ET
    HAS_DEFUSED = True
except ImportError:
    HAS_DEFUSED = False

class ForbiddenDTDTreeBuilder(ET.TreeBuilder):
    """
    Custom TreeBuilder that forbids DTD (Document Type Definitions).
    This helps prevent XXE (XML External Entity) attacks when defusedxml is not available.
    """
    def doctype(self, name, pubid, system):
        raise ET.ParseError("DTD not allowed for security reasons")

def safe_fromstring(text):
    """
    Parses an XML string securely.
    Uses defusedxml if available, otherwise falls back to a custom safe parser.
    """
    if HAS_DEFUSED:
        return defused_ET.fromstring(text)

    # Fallback implementation
    target = ForbiddenDTDTreeBuilder()
    parser = ET.XMLParser(target=target)
    parser.feed(text)
    return parser.close()
