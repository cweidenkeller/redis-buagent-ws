from flask import Blueprint

backup_app = Blueprint('backup_app', __name__)

@backup_app.route('/')
def show_backups():
    return 'HI MOM'
