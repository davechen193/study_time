import requests
import bs4
import jieba
import itertools
from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel
import re
import numpy as np
import pandas as pd
from hanziconv import HanziConv
from nltk.corpus import stopwords
import sys

def search_result(keywords):
    url = 'https://google.com/search?q=(' + "&".join(keywords) + ")"
    request_result=requests.get( url )
    # Creating soup from the fetched request
    soup = bs4.BeautifulSoup(request_result.text,
                            "html.parser")
    item_object=soup.find_all('div')
    result = set()
    for item in item_object:
        string_result = item.find('div', class_='BNeawe vvjwJb AP7Wnd')
        link_result = item.find('a')
        if string_result and link_result:
            tag_content = '<a target="_blank" href="' + link_result['href'][7:] + '" \
                >' + string_result.getText() + '</a>'
            if tag_content not in result:
                result.add(tag_content)
    return list(result)
mode = "en"
text= sys.argv[1]
process_words = ["concepts", "summarization", "applications", "analysis", "structure", "evaluation criteria"]
result = ""
for w in process_words:
    advanced_result = list(set(search_result([text + " " + w])))
    result += '<br/>' + "<h4>" + text + " " + w + "</h4>" + '<br/>'
    for text_line in advanced_result:
        result += text_line + '<br/>'
print(result)