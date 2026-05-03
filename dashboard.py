from flask import Blueprint, render_template
dashboard = Blueprint('dashboard', __name__, template_folder='templates', static_folder='static')

@dashboard.route('/')
def index():
    return render_template('/dashboard/index.html')