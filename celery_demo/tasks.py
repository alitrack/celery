from time import sleep,ctime
from .celery import app


@app.task
def add(x, y):
    sleep(5)
    return x + y


@app.task
def mul(x, y):
    sleep(10)
    return x * y
