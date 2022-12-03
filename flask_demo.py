from flask import Flask
from celery_demo.celery import app as celery

app = Flask(__name__)

@app.route('/add')
def add():
    from celery_demo import tasks
    results = tasks.add.delay(1234,6789)
    print('---------1234 + 6789 ------------')
    return {"msg": "success", "result": results.get()}

@app.route('/mul')
def mul():
    
    results = celery.send_task("celery_demo.tasks.mul",kwargs={"x":5,"y":6789})

    print('---------5 x 6789 ------------')
    result = results.get()
    
    return {"msg": "success", "result": result}

if __name__ == '__main__':
    app.run(debug=True)