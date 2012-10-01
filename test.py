
# encoding: utf-8

import unittest
from microsofttranslator import TranslateApiException
from mstranschain import ChainTranslator, EmptyTranslationChainError


class TestChainTranslator(unittest.TestCase):

    def setUp(self):
        self._client_id = "translaterpythonapi"
        self._client_secret = "FLghnwW4LJmNgEG+EZkL8uE+wb7+6tkOS8eejHg3AaI="

    def test_translate_empty(self):
        chain_translator = ChainTranslator(self._client_id, self._client_secret)
        with self.assertRaises(EmptyTranslationChainError):
            chain_translator.translate(u'空の翻訳？', [])

    def test_translate_listshort(self):
        chain_translator = ChainTranslator(self._client_id, self._client_secret)
        with self.assertRaises(EmptyTranslationChainError):
            chain_translator.translate(u'これはどう翻訳して欲しいの？', ['en'])

    def test_translate_norequest(self):
        # By passing invalid client info, assert no API access has occured...
        chain_translator = ChainTranslator('foo', 'bar')
        target = u'ムダな翻訳などしないッ'
        result = chain_translator.translate(target, ['ja', 'ja'])
        self.assertEqual(target, result)

    def test_translate_single(self):
        client = ChainTranslator(self._client_id, self._client_secret)
        self.assertEqual(client.translate("hello", ['en', 'pt']), u'Ol\xe1')

    def test_translate_multiple(self):
        chain_translator = ChainTranslator(self._client_id, self._client_secret)
        target = u'おはよう、諸君。'
        result = chain_translator.translate(target, ['ja', 'en', 'pt', 'ja'])
        self.assertEqual(result, u'\u826f\u3044\u65e5\u306f\u3001\u7d33\u58eb\u3067\u3059\u3002')

    def test_invalid_client_id(self):
        chain_translator = ChainTranslator("foo", "bar")
        with self.assertRaises(TranslateApiException):
            chain_translator.translate("hello", ["en", "pt"])


if __name__ == '__main__':
    unittest.main(verbosity=3)

