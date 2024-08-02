from flask import Flask, render_template, request, redirect, flash
from config.setting import db
from flask_migrate import Migrate
from models import Post

kitty = Flask(__name__)
kitty.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///kitty.db"
kitty.config["SECRET_KEY"] = '3120312093812031209'

db.init_app(kitty)
Migrate(kitty, db)


@kitty.route("/")
def home():
    return render_template("pages/index.jinja", hello=123)


@kitty.route("/about")
def about():
    return render_template("pages/about.jinja")


@kitty.route("/lottery")
def lottery():
    lottery_numbers = lottery_generator(6)
    return render_template("pages/lottery.jinja", numbers=lottery_numbers)


# 文章相關
@kitty.route("/posts", methods=["GET", "POST"])
def posts():
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


@kitty.route("/posts/<int:id>")
def show(id):
    post = Post.query.get_or_404(id)
    return render_template("posts/show.jinja", post=post)

@kitty.route("/posts/new")
def new_posts():
    return render_template("posts/new.jinja")


def lottery_generator(n):
    from random import sample

    numbers = sample(range(1, 44), n)
    return sorted(numbers)


if __name__ == "__main__":
    kitty.run(port=9527, debug=True)
