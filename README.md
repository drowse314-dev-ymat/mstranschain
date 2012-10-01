Chain Translator
=========================

* Version: 0.0
* Licence: The MIT Licence. See `./LICENCE`.
* Prerequisites:
    * Python2.7 or later.
    * Python `(open)ssl` support (might need recompiling Python).
    * [`microsofttranslator`](https://github.com/openlabs/Microsoft-Translator-Python-API.git) Python module.
    * Your registered application on [Azure DataMarket](https://datamarket.azure.com/developer/applications/).

----
This module is a utility for chaining (applying one after another) translation between multiple languages on an arbitraly text.  The module uses `microsofttranslator`, a third party Python API to Microsoft Translator API, for the core operatoin of translation.

Please note that I created this package for my own use and for fun, and the quality seems rough...

## Usage

        >>> from mstranschain import ChainTranslator
        >>> chain_translator = ChainTranslator('<Your Client ID>', '<Your Client Secret>')
        >>> print(chain_translator.translate("おはよう、諸君。", chain=['ja', 'en', 'pt', 'ja'])
        u"\u826f\u3044\u65e5\u306f\u3001\u7d33\u58eb\u3067\u3059\u3002"
