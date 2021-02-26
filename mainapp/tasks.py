from appEvent.celery import app

from .service import check_news


@app.task
def update_news():
    """ ОБновить по запросу """
    check_news()


@app.task
def beat_update_news():
    """ ОБновлять периодически """
    check_news()
