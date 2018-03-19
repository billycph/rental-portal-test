from flask import render_template, Blueprint


dashboard = Blueprint(
    'dashboard',
    __name__,
    static_folder='static',
    template_folder='templates'
)


@dashboard.route('/', methods=['GET'])
def render_page():
    return render_template('dashboard.html')