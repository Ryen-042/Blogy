from flask import render_template, request, Blueprint
from posts.models import Post

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html", posts=Post.query.order_by(Post.date_posted.desc())\
                            .paginate(page=request.args.get("page", 1, type=int),
                                      per_page=request.args.get("per_page", 5, type=int)), show_sidebar=True)


@main.route("/about")
def about():
    return render_template("about.html", show_sidebar=True)
