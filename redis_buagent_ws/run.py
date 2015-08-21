from flask import Flask
from redis_buagent_ws.blueprints import backup_app

app = Flask(__name__)
app.register_blueprint(backup_app)
def run():
    app.run()

