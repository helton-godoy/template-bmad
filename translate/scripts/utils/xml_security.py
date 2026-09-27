import xml.etree.ElementTree as ET

try:
    from defusedxml import ElementTree as defused_ET
    from defusedxml.common import DefusedXmlException
    HAS_DEFUSED = True
except ImportError:
    defused_ET = None
    DefusedXmlException = None
    HAS_DEFUSED = False

if HAS_DEFUSED:
    # NOTE: defusedxml raises DefusedXmlException (a ValueError subclass),
    # NOT xml.etree.ElementTree.ParseError, when it blocks DTD/entities.
    # Callers of safe_fromstring must catch XML_PARSE_ERRORS (both).
    XML_PARSE_ERRORS = (ET.ParseError, DefusedXmlException)
else:
    XML_PARSE_ERRORS = (ET.ParseError,)


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
    Raises XML_PARSE_ERRORS on malformed or forbidden (DTD/entity) input.
    """
    if HAS_DEFUSED:
        return defused_ET.fromstring(text)

    # Fallback implementation
    target = ForbiddenDTDTreeBuilder()
    parser = ET.XMLParser(target=target)
    parser.feed(text)
    return parser.close()
