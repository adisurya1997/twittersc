import requests
# URL = "https://dev-bhagaskarash4zl.microgen.id/api"


def process_item(url):
    print("CHECK : {}".format(url))
    data = requests.get(
        f'https://dev-bhagaskarash4zl.microgen.id/api/twitterscraps?select=url&where[url]={url}')
    if data.text == "[]":
        return True
    else:
        return False
