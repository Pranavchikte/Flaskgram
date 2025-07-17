import os
import secrets
from flask import Blueprint, render_template, redirect, url_for, flash, current_app, abort
from flask_login import login_required, current_user
from app import db
from app.forms import PostForm
from app.models import Post
from PIL import Image, ImageOps

post_bp = Blueprint('post', __name__, url_prefix='/post')


def save_image(form_image):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_image.filename)
    image_fn = random_hex + f_ext
    image_path = os.path.join(current_app.root_path, 'static/uploads', image_fn)

    img = Image.open(form_image)
    img = ImageOps.exif_transpose(img)

    output_size = (800, 800)
    img = Image.open(form_image)
    img.thumbnail(output_size)
    img.save(image_path)

    return image_fn


@post_bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        image_file = save_image(form.image.data)
        post = Post(image_file=image_file, caption=form.caption.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created!", 'success')
        return redirect(url_for('main.home'))
    return render_template('post_form.html', form=form)

@post_bp.route('/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.user_id != current_user.id:
        abort(403)

    image_path = os.path.join(current_app.root_path, 'static/upload', post.image_file)
    if os.path.exists(image_path):
        os.remove(image_path)

    db.session.delete(post)
    db.session.commit()

    flash('Post deleted successfully.' 'success')
    return redirect(url_for('main.home'))
