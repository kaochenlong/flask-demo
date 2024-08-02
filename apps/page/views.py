from flask import Blueprint, render_template

page_bp = Blueprint("page", __name__)

@page_bp.route("/")
def home():
    return render_template("pages/index.jinja", hello=123)

@page_bp.route("/about")
def about():
    return render_template("pages/about.jinja")


@page_bp.route("/lottery")
def lottery():
    lottery_numbers = lottery_generator(6)
    return render_template("pages/lottery.jinja", numbers=lottery_numbers)



def lottery_generator(n):
    from random import sample

    numbers = sample(range(1, 44), n)
    return sorted(numbers)
