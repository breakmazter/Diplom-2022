import spacy


class NerFilter:
    def __init__(self, model_name: str = "nl_core_news_sm"):
        self.ner_model = spacy.load(model_name)

    @staticmethod
    def ner_filter(text: str) -> str:
        text = ner_model(text)

        filtered_string = ""

        for token in text:
            if token.pos_ in ['PROPN', 'NOUN', 'NUM', 'MED']:
                new_token = "<SENSITIVE_DATA>"
            elif token.pos_ == "PUNCT":
                new_token = token.text
        else:
            new_token = " {}".format(token.text)

        filtered_string += new_token

        return filtered_string[1:]
