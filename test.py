from celery_demo import tasks
res1 = tasks.add.delay(23333, 1111)
print(res1.get(timeout=60))
# 24444 测试完成