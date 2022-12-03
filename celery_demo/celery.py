from celery import Celery

# 若redis设置了密码，URI应为`redis://:password@127.0.0.1:6379/0`
app = Celery('celery_demo',
             broker='redis://127.0.0.1:6379/0',
             backend='redis://127.0.0.1:6379/0',
             include=['celery_demo.tasks'])

app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()