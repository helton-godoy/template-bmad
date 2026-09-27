"""Unit tests for installed-package cache invalidation (PR #19 follow-up).

Uses stdlib unittest + mocks so it runs without pytest/argos installed.
"""
import logging
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock

# Mocks para dependências pesadas/ausentes antes de importar o tradutor
sys.modules.setdefault('yaml', MagicMock())
_argos = MagicMock()
sys.modules.setdefault('argostranslate', _argos)
sys.modules.setdefault('argostranslate.package', _argos.package)
sys.modules.setdefault('argostranslate.translate', _argos.translate)

SRC_DIR = Path(__file__).resolve().parent.parent.parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import argostranslate.package as argos_package  # noqa: E402
from bmad_translate.core.translator import BMADTranslator  # noqa: E402


def _pkg(fr, to):
    return SimpleNamespace(from_code=fr, to_code=to)


def _translator(target='pt'):
    t = BMADTranslator.__new__(BMADTranslator)
    t.settings = SimpleNamespace(get_target_language=lambda: target)
    t.logger = logging.getLogger('test-installed-package-cache')
    t._argos_initialized = False
    return t


class TestInstalledPackageCache(unittest.TestCase):
    def setUp(self):
        BMADTranslator.clear_installed_langs_cache()

    def tearDown(self):
        BMADTranslator.clear_installed_langs_cache()

    def test_cache_hit_avoids_rescan(self):
        argos_package.get_installed_packages = MagicMock(return_value=[_pkg('en', 'pt')])
        argos_package.update_package_index = MagicMock()

        t1 = _translator()
        t1._ensure_argos_initialized()
        self.assertTrue(t1._argos_initialized)
        self.assertEqual(argos_package.get_installed_packages.call_count, 1)

        t2 = _translator()
        t2._ensure_argos_initialized()
        self.assertTrue(t2._argos_initialized)
        # Cache hit: nenhuma nova leitura e nenhum update de índice (era o custo evitado).
        self.assertEqual(argos_package.get_installed_packages.call_count, 1)
        argos_package.update_package_index.assert_not_called()

    def test_clear_forces_rescan(self):
        argos_package.get_installed_packages = MagicMock(return_value=[_pkg('en', 'pt')])
        argos_package.update_package_index = MagicMock()

        _translator()._ensure_argos_initialized()
        self.assertEqual(argos_package.get_installed_packages.call_count, 1)

        BMADTranslator.clear_installed_langs_cache()
        _translator()._ensure_argos_initialized()
        self.assertEqual(argos_package.get_installed_packages.call_count, 2)

    def test_post_install_refresh_is_authoritative(self):
        # Snapshot inicial sem en->pt; após install, releitura confirma en->pt.
        argos_package.get_installed_packages = MagicMock(
            side_effect=[[], [_pkg('en', 'pt')]]
        )
        available = SimpleNamespace(
            from_code='en', to_code='pt', download=MagicMock(return_value='/tmp/pkg.argosmodel')
        )
        argos_package.get_available_packages = MagicMock(return_value=[available])
        argos_package.update_package_index = MagicMock()
        argos_package.install_from_path = MagicMock()

        t = _translator()
        t._ensure_argos_initialized()

        argos_package.install_from_path.assert_called_once_with('/tmp/pkg.argosmodel')
        self.assertIn(('en', 'pt'), BMADTranslator._installed_langs_cache)
        # 1 leitura inicial + 1 releitura pós-install (não apenas .add() otimista).
        self.assertEqual(argos_package.get_installed_packages.call_count, 2)
        self.assertTrue(t._argos_initialized)


if __name__ == "__main__":
    unittest.main()
