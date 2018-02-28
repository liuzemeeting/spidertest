import requests
import re

def linkurl():
    url="http://7766.gq/";
    response=requests.get(url);
    response.encoding='utf8'
    result=response.text;
    # result.encoding='utf8';
    print(result);
linkurl()

