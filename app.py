from flask import Flask, request, jsonify
from controllers.get import cron_twitter_ByHashtag, cron_twitter_BySearch, cron_twitter_ByListPost, cron_twitter_ByUser
from controllers.post import scrap_twitter_ByHashtag, scrap_twitter_ByListPost, scrap_twitter_ByTrend, scrap_twitter_ByUser, scrap_twitter_BySearch
app = Flask(__name__)

# Get


@app.route('/twitter/cron/hastags', methods=['GET'])
def cron_twitter_byHastags():
    return cron_twitter_ByHashtag.handler(request, jsonify) 


@app.route('/twitter/cron/search', methods=['GET'])
def cron_twitter_bySearchs():
    return cron_twitter_BySearch.handler(request, jsonify)


@app.route('/twitter/cron/list-post', methods=['GET'])
def cron_twitter_byListPost():
    return cron_twitter_ByListPost.handler(request, jsonify)


@app.route('/twitter/cron/user', methods=['GET'])
def cron_twitter_byUsers():
    return cron_twitter_ByUser.handler(request, jsonify)


# Post


@app.route('/twitter/hashtag', methods=['POST'])
def scrap_twitter_ByHastags():
    return scrap_twitter_ByHashtag.handler(request, jsonify)


@app.route('/twitter/trends', methods=['POST'])
def scrap_twitter_ByTrends():
    return scrap_twitter_ByTrend.handler(request, jsonify)


@app.route('/twitter/listposts', methods=['POST'])
def scrap_twitter_ByListPosts():
    return scrap_twitter_ByListPost.handler(request, jsonify)


@app.route('/twitter/search', methods=['POST'])
def scrap_twitter_BySearchs():
    return scrap_twitter_BySearch.handler(request, jsonify)


@app.route('/twitter/user', methods=['POST'])
def scrap_twitter_ByUsers():
    return scrap_twitter_ByUser.handler(request, jsonify)


if __name__ == '__main__':
    app.run(debug=True)
