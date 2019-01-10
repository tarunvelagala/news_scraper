from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template

import mail
from index import contents_list


def send_mail():
    mail.server.send_message(mail.msg)


scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(send_mail, 'interval', minutes=60)
scheduler.start()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', contents=contents_list)


if __name__ == '__main__':
    app.run()
