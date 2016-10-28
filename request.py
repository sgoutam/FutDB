from urllib.request import Request, urlopen
import simplejson
from TextSummarize import url_scrape
class newsresponse():
    def __init__(self,content,unescapedurl,title,publisher):
        self.content = content
        self.unescapedurl = unescapedurl
        self.title = title
        self.publisher = publisher


def newsrequest(playername):
    news_responses = []
    names = playername.split()
    searchparam = ''

    i=0
    for name in names:
        searchparam = searchparam +name
        i=i+1
        if i<names.__len__():
            searchparam = searchparam + '+'

    url = ('https://ajax.googleapis.com/ajax/services/search/news?' +
           'v=1.0&q='+searchparam+'&userip=INSERT-USER-IP')

    request = Request(url, None, {'Referer': ''})
    response = urlopen(request)
    jsonresults = simplejson.load(response)

    results = jsonresults["responseData"]['results']
    for i in range(0,4):
        news_responses.append(newsresponse(results[i]['content'],results[i]['unescapedUrl'],results[i]['title'],results[i]['publisher']))


    return news_responses
