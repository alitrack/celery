# celery

Celery Demo  with Windows Support

## install Redis Server

- download [Redis Server](https://github.com/zkteco-home/redis-windows)
- unzip
- run `redis-server.exe`

## install celery and flower

```BASH
pip install celery flower redis eventlet flask
```

- Celery execution pool options,

  - prefork, default, but doesn't support Windows
  - eventlet
  - gevent
  - solo
  - processes
  - threads
  - custom
  
- flask is for `flask_demo.py`

## run order

1. `worker.bat`
2. `flower.bat`(optional)
3. `python test.py` or `python flask_demo.py`
