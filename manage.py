from flask import Flask
from config.setting import db
from flask_migrate import Migrate
from apps.post.views import post_bp
from apps.page.views import page_bp
import models

kitty = Flask(__name__)
kitty.register_blueprint(post_bp)
kitty.register_blueprint(page_bp)
kitty.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///kitty.db"
kitty.config["SECRET_KEY"] = "3120312093812031209"
kitty.config["WTF_CSRF_SECRET_KEY"] = "32ip213i21pi312"

db.init_app(kitty)
Migrate(kitty, db)

if __name__ == "__main__":
    kitty.run(port=9527, debug=True)
