import atexit
import time

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template
from index import headline_filtered

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', content=headline_filtered)


def send_mail():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    app.run()
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=send_mail(), trigger="interval", seconds=3)
    scheduler.start()
