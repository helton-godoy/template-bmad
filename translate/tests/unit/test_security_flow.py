import sys
import unittest
from unittest.mock import MagicMock, patch

# Mock argostranslate modules BEFORE importing BMADTranslator
# This prevents loading heavy C++ libraries that cause Bus Errors in some envs
mock_argos = MagicMock()
mock_translate = MagicMock()
sys.modules['argostranslate'] = mock_argos
sys.modules['argostranslate.package'] = MagicMock()
sys.modules['argostranslate.translate'] = mock_translate
mock_argos.translate = mock_translate

from bmad_translate.core.translator import BMADTranslator
from bmad_translate.config.settings import Settings

class TestContentProtectionFlow(unittest.TestCase):
    def setUp(self):
        self.settings = Settings()
        self.translator = BMADTranslator(self.settings)
        # Mocking internal methods
        self.translator._ensure_argos_initialized = MagicMock()
        self.translator.protector = MagicMock()
        self.translator.protector.protect_content.return_value = "PROTECTED_CONTENT"
        self.translator.protector.restore_content.return_value = "RESTORED_CONTENT"
        self.translator.logger = MagicMock()

    def test_translate_text_protects_content(self):
        # Configure our pre-mocked translate function
        sys.modules['argostranslate.translate'].translate.return_value = "TRANSLATED_CONTENT"
        
        # Call with protect=True
        result = self.translator._translate_text("original text", protect=True)
        
        # DEBUG: Check for errors
        if self.translator.logger.error.called:
            print("\nLOGGED ERROR:", self.translator.logger.error.call_args)
        
        # Verify protect_content was called
        self.translator.protector.protect_content.assert_called_with("original text")
        
        # Verify argos receives protected content
        sys.modules['argostranslate.translate'].translate.assert_called_with("PROTECTED_CONTENT", 'en', 'pt')
        
        # Verify restore_content was called
        self.translator.protector.restore_content.assert_called_with("TRANSLATED_CONTENT")
        
        # Verify final result
        self.assertEqual(result, "RESTORED_CONTENT")

    def test_translate_text_without_protection(self):
        # Configure our pre-mocked translate function
        sys.modules['argostranslate.translate'].translate.return_value = "TRANSLATED_CONTENT"
        
        # Call with protect=False (default)
        result = self.translator._translate_text("original text", protect=False)
        
        # Verify protect_content was NOT called
        self.translator.protector.protect_content.assert_not_called()
        
        # Verify argos receives original content
        sys.modules['argostranslate.translate'].translate.assert_called_with("original text", 'en', 'pt')
        
        # Verify restore_content was NOT called
        self.translator.protector.restore_content.assert_not_called()
        
        self.assertEqual(result, "TRANSLATED_CONTENT")

if __name__ == '__main__':
    unittest.main()
