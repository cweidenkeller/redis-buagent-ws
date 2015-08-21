from flask import Blueprint, render_template

backup_app = Blueprint('backup_app', __name__)

@backup_app.route('/')
def index():
    return render_template("layout.html")

@backup_app.route('/create_backup')
def make_backup():
    return render_template("create_backup.html")

@backup_app.route('/show_backups')
def show_backups():
    return render_template("show_backups.html")
