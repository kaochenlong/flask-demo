from flask import Blueprint, request, flash, redirect, render_template, url_for
from models import Post
from config.setting import db
from forms.post_form import PostForm

post_bp = Blueprint("post", __name__)


@post_bp.route("/posts", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form = PostForm(request.form)

        if form.validate_on_submit():
            post = Post(title=form.title.data, content=form.content.data)
            db.session.add(post)
            db.session.commit()
            flash("新增成功")
            return redirect(url_for("post.index"))
        else:
            return render_template("posts/new.jinja", form=form)

    posts = Post.query.order_by(-Post.id)
    return render_template("posts/index.jinja", posts=posts)


@post_bp.route("/posts/<int:id>")
def show(id):
    post = Post.query.get_or_404(id)
    return render_template("posts/show.jinja", post=post)


@post_bp.route("/posts/new")
def new():
    form = PostForm()
    return render_template("posts/new.jinja", form=form)


@post_bp.route("/posts/<int:id>/edit")
def edit(id):
    post = Post.query.get_or_404(id)
    return render_template("posts/edit.jinja", post=post)


@post_bp.route("/posts/<int:id>", methods=["POST"])
def update(id):
    post = Post.query.get_or_404(id)

    title = request.form.get("title")
    content = request.form.get("content")

    post.title = title
    post.content = content
    db.session.add(post)
    db.session.commit()

    flash("更新文章成功")

    return redirect(url_for("post.show", id=post.id))


@post_bp.route("/posts/<int:id>/delete", methods=["POST"])
def delete(id):
    post = Post.query.get_or_404(id)

    db.session.delete(post)
    db.session.commit()

    flash("已成功刪除")
    return redirect(url_for("post.index"))
