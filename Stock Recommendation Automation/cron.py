from flask import Flask
import Automation
from flask_apscheduler import APScheduler

app = Flask(__name__)
scheduler = APScheduler()

@app.route("/")
def index():
    return "Welcome to the scheduler!"

def scheduledTask():
    Automation.SendMail()
    print("This task is running every 1 hour")


if __name__ == '__main__':
    scheduler.add_job(id ='Scheduled task', func = scheduledTask, trigger = 'interval', seconds = 3600)
    scheduler.start()
    app.run(host = '0.0.0.0', port = 8080)
