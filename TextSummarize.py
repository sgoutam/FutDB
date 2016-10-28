from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
from urllib import request
import urllib
from nltk import data
from bs4 import BeautifulSoup


class Summary:
    def __init__(self,title,summary):
        self.title=title
        self.summary=summary


class FrequencySummarizer:
  def __init__(self, min_cut=0.1, max_cut=0.9):

    self._min_cut = min_cut
    self._max_cut = max_cut 
    self._stopwords = set(stopwords.words('english') + list(punctuation))

  def _compute_frequencies(self, word_sent):

    freq = defaultdict(int)
    for s in word_sent:
      for word in s:
        if word not in self._stopwords:
          freq[word] += 1
    m = float(max(freq.values()))
    keys=freq.keys()
    for w in list(freq.keys()):
      freq[w] = freq[w]/m
      if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
        del freq[w]
    return freq

  def summarize(self, text, n):

    sents = sent_tokenize(text)
    assert n <= len(sents)
    word_sent = [word_tokenize(s.lower()) for s in sents]
    self._freq = self._compute_frequencies(word_sent)
    ranking = defaultdict(int)
    for i,sent in enumerate(word_sent):
      for w in sent:
        if w in self._freq:
          ranking[i] += self._freq[w]
    sents_idx = self._rank(ranking, n)    
    return [sents[j] for j in sents_idx]

  def _rank(self, ranking, n):
    return nlargest(n, ranking, key=ranking.get)


def get_only_text(url):
    page = urllib.request.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page,"html.parser")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return soup.title.text, text


def url_scrape(url):
    fs = FrequencySummarizer()
    'for article_url in to_summarize:'
    title, text = get_only_text(url)
#    print (title)
    summary = []
    for s in fs.summarize(text, 10):
#       print ('*',s)
       summary.append(s)

    return Summary(title=title,summary=summary)


def wiki_scrape(playername):

    names = playername.split()
    searchparam = ''

    i=0
    for name in names:
        searchparam = searchparam +name
        i=i+1
        if i<names.__len__():
            searchparam = searchparam + '_'
    url ='https://en.wikipedia.org/wiki/'+searchparam
    Summaryobj = url_scrape(url)
    return Summaryobj
