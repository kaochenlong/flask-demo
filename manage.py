from flask import Flask, render_template, request, redirect
from config.setting import db
from flask_migrate import Migrate

kitty = Flask(__name__)
kitty.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///kitty.db"

db.init_app(kitty)
Migrate(kitty, db)


@kitty.route("/")
def hello_world():
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
        # 寫入資料庫
        # ORM
        return redirect("/posts")

    return render_template("posts/index.jinja")


@kitty.route("/posts/new")
def new_posts():
    return render_template("posts/new.jinja")


def lottery_generator(n):
    from random import sample

    numbers = sample(range(1, 44), n)
    return sorted(numbers)


if __name__ == "__main__":
    kitty.run(port=9527, debug=True)
