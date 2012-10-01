
# encoding: utf-8

import microsofttranslator as _microsofttranslator


class EmptyTranslationChainError(Exception):
    """
    Error to indicate translation chaining list must contain
    more than two language labels.
    """
    pass


class ChainTranslator(object):
    """
    Chain multiple translation using Microsoft Translator API
    (http://api.microsofttranslator.com/V2/Http.svc/Translate),
     using 'microsofttranslator' module
    (git://github.com/openlabs/Microsoft-Translator-Python-API.git)
    for API access.

    This class supplies simple wrapper for 'Translator' class in 
    microsofttranslator module, and ease the operations of translation
    requests.

    Usage:
        >>> from mstranschain import ChainTranslator
        >>> chain_translator = ChainTranslator('<Your Client ID>', '<Your Client Secret>')
        >>> print(chain_translator.translate("おはよう、諸君。", chain=['ja', 'en', 'pt', 'ja'])
        u""
    """

    def __init__(self, client_id, client_secret):
        self._translator = _microsofttranslator.Translator(client_id, client_secret)

    def translate(self, text, lang_chain):
        """
        Translate a text string through languages in lang_chain list.
        lang_chain must contain two or more string labels for languages.
        """
        # Shortage of lang_chain error.
        if len(lang_chain) < 2:
            raise EmptyTranslationChainError('ChainTranslator.translate takes two or more languages to chain translation.')
        # Shrink lang_chain if sequences of identical lang-labels found.
        lang_chain_shrink = [lang_chain.pop(0)]
        for lang in lang_chain:
            if lang == lang_chain_shrink[-1]:
                continue
            else:
                lang_chain_shrink.append(lang)
        # Shorten into less than pair by shrinking, results no error & returns results.
        if len(lang_chain_shrink) == 1:
            return text
        # Translation process.
        result = text
        for from_lang, to_lang in zip(lang_chain_shrink, lang_chain_shrink[1:]):
            result = self._translator.translate(result, to_lang=to_lang, from_lang=from_lang)
        return result
