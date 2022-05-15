import re

import emoji as emoji


class Preprocessor:
    """
    Preprocesses the text.
    """

    def __init__(self,
                 is_remove_escape_chain: bool = True,
                 is_remove_emoji: bool = True,
                 is_remove_bad_symbols: bool = True,
                 is_remove_tags_and_hashtags: bool = True,
                 is_replace_currency_symbols: bool = True):
        self.is_remove_escape_chain = is_remove_escape_chain
        self.is_remove_emoji = is_remove_emoji
        self.is_remove_bad_symbols = is_remove_bad_symbols
        self.is_remove_tags_and_hashtags = is_remove_tags_and_hashtags
        self.is_replace_currency_symbols = is_replace_currency_symbols

    @staticmethod
    def __remove_escape_chain(text: str) -> str:
        """
        Replaces escape sequences with their corresponding characters.

        Args:
            text: The text to be processed.

        Returns:
            str: The processed text.
        """
        text = text.replace('\\n', '\n')
        text = text.replace('\\t', '\t')
        text = text.replace('\\r', '\r')
        text = text.replace('\\"', '"')
        text = text.replace('\\\'', '\'')
        text = text.replace('\\\\', '\\')

        return text

    @staticmethod
    def __remove_emoji(text: str) -> str:
        """
        Removes emoji from the text.

        Args:
            text: The text to be processed.

        Returns:
            str: The processed text.
        """
        return ''.join(c for c in text if c not in emoji.unicode_codes.en.EMOJI_UNICODE_ENGLISH)

    @staticmethod
    def __remove_bad_symbols(text: str) -> str:
        """
        Removes symbols that are not allowed in the text.

        Args:
            text: The text to be processed.

        Returns:
            str: The processed text.
        """
        bad_symbols = re.compile(f"[{''.join(map(chr, list(range(0, 32)) + list(range(127, 160))))}]")

        return bad_symbols.sub('', text)

    @staticmethod
    def __remove_tags_and_hashtags(text: str) -> str:
        """
        Removes tags and hashtags from the text.

        Args:
            text: The text to be processed.

        Returns:
            str: The processed text.
        """
        text = re.sub(r'<.*?>', '', text)
        text = re.sub(r'#\w+', '', text)

        return text

    @staticmethod
    def __replace_currency_symbols(text: str) -> str:
        """
        Replaces currency symbols with their corresponding characters.

        Args:
            text: The text to be processed.

        Returns:
            str: The processed text.
        """
        currencies = {
            "$": "usd",
            "zł": "pln",
            "£": "gbp",
            "¥": "jpy",
            "฿": "thb",
            "₡": "crc",
            "₦": "ngn",
            "₩": "krw",
            "₪": "ils",
            "₫": "vnd",
            "€": "eur",
            "₱": "php",
            "₲": "pyg",
            "₴": "uah",
            "₹": "inr",
        }
        currency_regex = re.compile(
            "({})+".format("|".join(re.escape(c) for c in currencies.keys()))
        )

        return currency_regex.sub(lambda m: currencies[m.group()], text)

    def preprocess(self, text: str) -> str:
        """
        Preprocesses the text.

        Args:
            text: The text to be processed.

        Returns:
            str: The processed text.
        """
        if self.is_remove_escape_chain:
            text = self.__remove_escape_chain(text)

        if self.is_remove_emoji:
            text = self.__remove_emoji(text)

        if self.is_remove_bad_symbols:
            text = self.__remove_bad_symbols(text)

        if self.is_remove_tags_and_hashtags:
            text = self.__remove_tags_and_hashtags(text)

        if self.is_replace_currency_symbols:
            text = self.__replace_currency_symbols(text)

        return text
