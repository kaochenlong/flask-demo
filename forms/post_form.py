from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField(
        "標題",
        validators=[DataRequired()],
        render_kw={
            "placeholder": "請輸入文章標題",
            "class": "w-full border border-black text-lg px-2 py-1",
            "x-model": "title",
        },
    )
    content = TextAreaField(
        "內文",
        render_kw={
            "placeholder": "文章內文",
            "class": "w-full border border-black text-lg px-2 py-1",
            "rows": 8,
        },
    )
