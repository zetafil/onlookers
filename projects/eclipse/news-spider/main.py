
import pprint
import feedparser

url = None
baidu_national_news_url = 'http://news.baidu.com/n?cmd=1&class=civilnews&tn=rss';
result = feedparser.parse(baidu_national_news_url)
pprint.pprint(result)

for e in result["items"]:
    print(e.title)


