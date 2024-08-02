from flask import Blueprint, request, flash, redirect, render_template
from models import Post
from config.setting import db

post_bp = Blueprint("post", __name__)

@post_bp.route("/posts", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')

        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()

        flash("新增成功")

        return redirect("/posts")

    posts = Post.query.order_by(-Post.id)
    return render_template("posts/index.jinja", posts=posts)


@post_bp.route("/posts/<int:id>")
def show(id):
    post = Post.query.get_or_404(id)
    return render_template("posts/show.jinja", post=post)

@post_bp.route("/posts/new")
def new():
    return render_template("posts/new.jinja")
