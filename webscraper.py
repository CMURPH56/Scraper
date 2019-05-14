from bs4 import BeautifulSoup
import requests
import json

url = 'http://twitter.com/i/moments'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")


tweetArr = []
for tweet in content.findAll('div', attrs={"class": "MomentCapsuleSummary-details"}):
  print(tweet)
  tweetObject = {
      "title": tweet.find('span', attrs={"class": "MomentCapsuleSubtitle-context"}).text,
  }
  tweetArr.append(tweetObject)
with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)