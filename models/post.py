from config.setting import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column


class Post(db.Model):
    __tablename__ = "posts"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String, nullable=False)
    content = mapped_column(String)
