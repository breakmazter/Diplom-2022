import re


class RegexFilter:
    @staticmethod
    def remove_numbers(text: str) -> str:
        return re.sub(r'\w*\d\w*', '<SENSITIVE_DATA>', text).strip()

    @staticmethod
    def remove_postal_codes(text: str) -> str:
        return re.sub('[0-9]{4}[ ]?[A-Z]{2}([ ,.:;])', '<SENSITIVE_DATA>', text)

    @staticmethod
    def remove_email(text: str) -> str:
        return re.sub('(([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.'
                      '([a-z]{2,6}(?:\.[a-z]{2})?))(?![^<]*>)', '<SENSITIVE_DATA>', text)

    @staticmethod
    def remove_dates(text: str) -> str:
        text = re.sub("\d{2}[- /.]\d{2}[- /.]\d{,4}", "<SENSITIVE_DATA>", text)

        text = re.sub("(\d{1,2}[^\w]{,2}(januari|februari|maart|april|mei|juni|juli|augustus"
                      "|september|oktober|november|december)([- /.]{,2}(\d{4}|\d{2})){,1})"
                      "(?P<n>\D)(?![^<]*>)", "<SENSITIVE_DATA>", text)

        text = re.sub("(\d{1,2}[^\w]{,2}(jan|feb|mrt|apr|mei|jun|jul|aug|sep|okt|nov|dec)"
                      "([- /.]{,2}(\d{4}|\d{2})){,1})(?P<n>\D)(?![^<]*>)", "<SENSITIVE_DATA>", text)

        return text

    def find_sensitive_data(self, text: str) -> str:
        text = self.remove_numbers(text)
        text = self.remove_postal_codes(text)
        text = self.remove_email(text)
        text = self.remove_dates(text)

        return text

    def remove_sensitive_data(self, text: str) -> str:
        text = self.find_sensitive_data(text)

        text = text.replace("<SENSITIVE_DATA>", "")

        return text
