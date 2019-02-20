import os
import pickle
import codecs

articles = []
headlines = []
keywords = []

# give path, return tuple of headline, article
def get_headline_to_article(fp):
    with open(fp) as article_file:
        data = article_file.readlines()
        headline = data[0].strip();
        data.pop(0)
        data = [d.strip() for d in data]
        article = "".join(data)
        return str(headline),str(article),None

def walk(dir):
    for f in os.listdir(dir):
        if f.endswith('.txt'):
            article, headline, keyword = get_headline_to_article(os.path.join(dir,f))
            articles.append(article)
            headlines.append(headline)
            keywords.append(keyword)

print("articles: ", len(articles))
print("headlines: ", len(headlines))
print("keywords: ", len(keywords))

walk('business')
print("articles: ", len(articles))
print("headlines: ", len(headlines))
print("keywords: ", len(keywords))

walk('entertainment')
print("articles: ", len(articles))
print("headlines: ", len(headlines))
print("keywords: ", len(keywords))

walk('politics')
print("articles: ", len(articles))
print("headlines: ", len(headlines))
print("keywords: ", len(keywords))

walk('tech')
print("articles: ", len(articles))
print("headlines: ", len(headlines))
print("keywords: ", len(keywords))

filehandler = open('articles.pkl', 'wb')
pickle.dump((articles, headlines, keywords), filehandler)
