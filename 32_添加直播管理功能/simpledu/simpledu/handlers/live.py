from flask import Blueprint, render_template
from simpledu.models import Live

live = Blueprint('live', __name__, url_prefix='/live')


@live.route('/')
def index():
    # order_by 按列排序，desc 表示降序
    live = Live.query.order_by(Live.created_at.desc()).first()
    return render_template('live/index.html', live=live)

