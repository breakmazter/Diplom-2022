from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

from filters.ner_filter import NerFilter
from filters.regex_filter import RegexFilter

app = FastAPI()

regex_filter = RegexFilter()
ner_filter = NerFilter()


class Document(BaseModel):
    text: str = Field(..., title="The text to be processed.")


@app.post(
    'find_sensitive_data',
    response_model=Document,
    summary='Finds sensitive data in the text.',
    description='Finds sensitive data in the text.',
)
def find_sensitive_data(document: Document = Body(..., description='Find sensitive data.')) -> Document:
    document.text = regex_filter.find_sensitive_data(document.text)
    document.text = ner_filter.find_sensitive_data(document.text)

    return document


@app.post(
    f'/remove_sensitive_data',
    response_model=Document,
    summary='Removes sensitive data from the text.',
    description='Removes sensitive data from the text.',
)
def remove_sensitive_data(document: Document = Body(..., description='Remove sensitive data.')) -> Document:
    document.text = regex_filter.remove_sensitive_data(document.text)
    document.text = ner_filter.remove_sensitive_data(document.text)

    return document
