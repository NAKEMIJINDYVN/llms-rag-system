from lxml.html import fromstring, HtmlElement

from typing import *

class ParseHTMLProps(TypedDict):
    html_content: str

class ParseHTML:
    kwargs: ParseHTMLProps

    @staticmethod
    def create_tree():
        html_content = ParseHTML.kwargs["html_content"]
        return fromstring(html_content) if html_content else None
    
    @staticmethod
    def get_all_text(css_selector: str = 'body', text_only: bool = True, out_type: Literal["list", "string"] = "list"):
        try:
            elements: List[HtmlElement] = ParseHTML.create_tree().cssselect(css_selector)
            list_text = []

            for el in elements:
                if text_only:
                    el_text = el.text_content().strip()
                    if el_text:
                        list_text.append(el_text)
                else:
                    list_text.append(el_text)

            return list_text if out_type == "list" else "".join(list_text)
        except Exception as error:
            print(error)