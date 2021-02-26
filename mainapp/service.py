from requests import get
from json import loads
from datetime import datetime
from .models import Post


def check_news():
    url_on_hacker_news_item = 'https://news.ycombinator.com/item?id='
    response = get('https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty')
    if response.status_code == 200:
        data = response.json()[:30] # Получаем id 30-ти новых постов
        for post_id in data:
            if not Post.objects.filter(post_id=post_id):
                news = detail_news(post_id)
                created = datetime.fromtimestamp(news['time'])
                Post.objects.get_or_create(
                    post_id=news['id'],
                    title=news['title'],
                    url=news.get('url', url_on_hacker_news_item+str(post_id)),
                    created=created
                )
        return data


def detail_news(id):
    """ Получение детальной информации поста """
    response = get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty')
    if response.status_code == 200:
        return response.json()

