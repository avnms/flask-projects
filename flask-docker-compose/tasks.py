import os
from celery import Celery

app = Celery("tasks", broker=os.getenv("REDIS_URL"))

@app.task
def example_task(param):
    # Perform task logic here
    print(f"Executing task with param: {param}")
