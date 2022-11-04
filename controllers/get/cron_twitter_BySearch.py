from unittest import result
import snscrape.modules.twitter as twitterScrapper
import json
import requests
import os

localUrl = 'https://dev-bhagaskarash4zl.microgen.id'
if os.environ.get("ENVIRONMENT") == 'STAGING':
    localUrl = 'https://stg-bhagaskarash4zl.microgen.id'
if os.environ.get("ENVIRONMENT") == 'PRODUCTION':
    localUrl = 'https://bhagaskarash4zl.microgen.id'


def scrap_twitter_bySearch(keyword):
    tweets = []

    scraper = twitterScrapper.TwitterSearchScraper(keyword)
    for i, tweet in enumerate(scraper.get_items()):
        print(tweet)
        if i > 50:
            break
        print(f"{i} content: {tweet}")
        tweets.append({"idUser": tweet.id,
                       "date": str(tweet.date),
                       "username": tweet.user.username,
                       'content': tweet.content,
                       'link': tweet.url,
                       'keyword': keyword,
                       'language': tweet.lang,
                       'likeCount': tweet.likeCount,
                       'replyCount': tweet.replyCount,
                       'retweetCount': tweet.retweetCount
                       })
    return tweets


def handler(request, jsonify):
    global r
    total_scrapt = 0
    total_data_post = 0
    try:
        # Get Token Administrator Microgen
        print('Get token admin microgen...')
        account_admin = {
            'email': 'admin@mail.com',
            'password': '2wsx1qaz'
        }
        config = {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        }

        token_admin = requests.post(
            "https://dev-bhagaskarash4zl.microgen.id/api/login", json=account_admin, headers=config)
        token_admin = json.loads(token_admin.text)['token']
        print('Get token admin success...')
        print('Token Admin: ', token_admin)

        header = {
            'Authorization': f"Bearer {token_admin}"
        }

        uniq_keyword = []
        keyword = requests.get(
            localUrl +
            "/api/statusCronTests?select=appScraper,status,keyword,limit,createdBy&where[status]=ACTIVE&where[appScraper]=Twitter&where[searchBy]=SEARCH",
            headers=header)
        keyword = json.loads(keyword.text)
        print("TOTAL UNTUK PUSH:", len(keyword))

        # Grouping Keyword for scraping
        for uniq in keyword:
            if uniq["keyword"] not in uniq_keyword:
                uniq_keyword.append(uniq["keyword"])

        print("Filter Uniq Keyword", uniq_keyword)

        for k in uniq_keyword:
            try:
                print("Scraping '{}' running...".format(k))
                r = scrap_twitter_bySearch(k)
                total_scrapt += len(r)
                if len(r) > 0:
                    print("Length Data Scrap: {}".format(len(r)))
                    for x in keyword:
                        limit = x['limit'] or 0
                        print('LIMIT:', x['limit'])
                        process = 1
                        if k == x['keyword']:
                            print(
                                f"Data Scraping Keyword: {k}, Send To : {x['createdBy']['email']}")
                            # Post All Data scrapt to Microgen
                            for post in r:
                                if process <= limit:
                                    print("POST: ", post['link'])
                                    print("Process : {}, Process limit: {}".format(
                                        process, limit))
                                    process += 1
                                    total_data_post += 1
                                    try:
                                        response = requests.post('https://dev-bhagaskarash4zl.microgen.id/api/twitterscraps', json={
                                            **post,
                                            'createByUserId': x['createdBy']['id']}, headers=header)
                                        print(response.text)
                                        if response.status_code == 400:
                                            return {
                                                "statusCode": 400,
                                                "error": response.text
                                            }
                                    except Exception as e:
                                        print(e)
                else:
                    print("Data scrap '{}' not found!".format(k))

            except Exception as e:
                print(e)
                jsonify({'statusCode': 500, 'error': str(e)})

        return jsonify({
            'statusCode': 200,
            'total_twitter_scrap': total_scrapt,
            'keyword_scrap': uniq_keyword,
            'total_data_post': total_data_post
        })

    except Exception as e:
        print(e)
        return jsonify({'statusCode': 500, 'error': str(e)})
