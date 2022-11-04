import snscrape.modules.twitter as twitterScrapper
import json


def handler(request, jsonify):
    try:
        tweets = []

        scraper = twitterScrapper.TwitterTrendsScraper()
        for i, tweet in enumerate(scraper.get_items()):
            print(tweet)
            if i > 23:
                break
            print(f"{i} content: {tweet.name}")
            tweets.append({"name": tweet.name,
                           "domainContext": tweet.domainContext,
                           'totalTweets': tweet.metaDescription,
                           })

        j = json.dumps(tweets)
        return j
    except Exception as e:
        result = {
            "statusCode": 400,
            "error": e
        }
        return result
