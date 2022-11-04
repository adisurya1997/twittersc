import snscrape.modules.twitter as twitterScrapper
import json


def handler(request, jsonify):
    try:
        print(request.data)
        posts = json.loads(request.data)
        limit = posts['limit']
        keyword = posts['keyword']

        tweets = []

        scraper = twitterScrapper.TwitterSearchScraper(keyword)
        for i, tweet in enumerate(scraper.get_items()):
            print(tweet)
            if i > limit:
                break
            print(f"{i} content: {tweet}")
            tweets.append({"id": tweet.id,
                           "username": tweet.user.username,
                           'content': tweet.content,
                           'url': tweet.url,
                           'date': tweet.date,
                           'renderedContent': tweet.renderedContent,
                           'quoteCount': tweet.quoteCount,
                           'conversationId': tweet.conversationId,
                           'lang': tweet.lang,
                           'source': tweet.source,
                           'sourceUrl': tweet.sourceUrl,
                           'sourceLabel': tweet.sourceLabel,
                           #    'outlinks': jsonify(tweet.outLinks),
                           #    'tcooutlinks': tweet.tcooutLinks,
                           'media': tweet.media,
                           #    'retweetedTweet': json.dumps(tweet.retweeetTweet),
                           #    'quotedTweet': tweet.quotedTweet,
                           'inReplyToTweetId': tweet.inReplyToTweetId,
                           #    'inReplyToUser': tweet.inReplyToUsers,
                           #    'mentionedUsers': tweet.mentionedUsers,
                           'coordinates': tweet.coordinates,
                           'place': tweet.place,
                           #    'hashtags': tweet.hastags,
                           'cashtags': tweet.cashtags,
                           #    'link': tweet.link,
                           #    'search': tweet.seacrh,
                           'likeCount': tweet.likeCount,
                           'retweetCount': tweet.retweetCount,
                           'lang': tweet.lang
                           })
        return jsonify(tweets)
    except Exception as e:
        result = {
            "statusCode": 400,
            "error": e
        }
        return result
