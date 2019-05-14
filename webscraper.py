from bs4 import BeautifulSoup
import requests
import json

url = 'http://twitter.com/i/moments'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")


tweetArr = []
for tweet in content.findAll('div', attrs={"class": "MomentCapsuleSummary-details"}):
    tweetObject = {
      "description": tweet.find("div", attrs={"class":"MomentCapsuleSummary-description"}).text,
      "link" : tweet.a['href']
    }
    tweetArr.append(tweetObject)
with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)