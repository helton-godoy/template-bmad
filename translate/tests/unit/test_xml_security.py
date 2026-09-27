"""Unit tests for translate/scripts/utils/xml_security.py (PR #23 follow-up)."""
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

# translate/scripts precisa estar no path para `from utils.xml_security import ...`
SCRIPTS_DIR = Path(__file__).resolve().parent.parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from utils.xml_security import (  # noqa: E402
    HAS_DEFUSED,
    XML_PARSE_ERRORS,
    ForbiddenDTDTreeBuilder,
    safe_fromstring,
)

BENIGN_XML = "<agent><name>Test</name><description>A test agent</description></agent>"

XXE_PAYLOAD = """<?xml version="1.0"?>
<!DOCTYPE agent [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<agent>&xxe;</agent>"""

BILLION_LAUGHS_PAYLOAD = """<?xml version="1.0"?>
<!DOCTYPE lolz [
 <!ENTITY lol "lollollollollollollollollollol">
 <!ENTITY lol2 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
]>
<agent>&lol2;</agent>"""


class TestSafeFromstring(unittest.TestCase):
    def test_benign_xml_parses(self):
        root = safe_fromstring(BENIGN_XML)
        self.assertEqual(root.tag, "agent")
        self.assertEqual(root.find("name").text, "Test")

    def test_external_entity_blocked(self):
        with self.assertRaises(XML_PARSE_ERRORS):
            safe_fromstring(XXE_PAYLOAD)

    def test_billion_laughs_blocked(self):
        with self.assertRaises(XML_PARSE_ERRORS):
            safe_fromstring(BILLION_LAUGHS_PAYLOAD)

    def test_malformed_xml_raises(self):
        with self.assertRaises(XML_PARSE_ERRORS):
            safe_fromstring("<agent><unclosed>")


class TestXmlParseErrors(unittest.TestCase):
    def test_contains_stdlib_parse_error(self):
        # Callers catch XML_PARSE_ERRORS; stdlib ParseError must always be covered.
        self.assertIn(ET.ParseError, XML_PARSE_ERRORS)

    def test_defused_exception_covered_when_installed(self):
        if HAS_DEFUSED:
            from defusedxml.common import DefusedXmlException
            # Regression test: defusedxml raises DefusedXmlException (ValueError),
            # NOT ET.ParseError, so it must be part of the caught tuple.
            self.assertIn(DefusedXmlException, XML_PARSE_ERRORS)
            self.assertNotEqual(DefusedXmlException, ET.ParseError)
        else:
            self.assertEqual(XML_PARSE_ERRORS, (ET.ParseError,))


class TestFallbackBuilder(unittest.TestCase):
    def test_fallback_rejects_doctype_directly(self):
        # Exercises the stdlib fallback path regardless of defusedxml presence.
        target = ForbiddenDTDTreeBuilder()
        parser = ET.XMLParser(target=target)
        with self.assertRaises(ET.ParseError):
            parser.feed(XXE_PAYLOAD)
            parser.close()

    def test_fallback_accepts_benign(self):
        target = ForbiddenDTDTreeBuilder()
        parser = ET.XMLParser(target=target)
        parser.feed(BENIGN_XML)
        root = parser.close()
        self.assertEqual(root.tag, "agent")


if __name__ == "__main__":
    unittest.main()
