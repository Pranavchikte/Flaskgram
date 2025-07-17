from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Post, User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('home.html', posts=posts)

@main_bp.route('/upload')
@login_required
def upload_post():
    return "Only logged-in user can see this!"