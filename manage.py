from flask import Flask, render_template
from config.setting import db
from flask_migrate import Migrate
from apps.post.views import post_bp
import models

kitty = Flask(__name__)
kitty.register_blueprint(post_bp)
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



def lottery_generator(n):
    from random import sample

    numbers = sample(range(1, 44), n)
    return sorted(numbers)


if __name__ == "__main__":
    kitty.run(port=9527, debug=True)
