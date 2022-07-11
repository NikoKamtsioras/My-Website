from flask import Flask
from flask import render_template

webapp = Flask(__name__)


@webapp.route("/")
def app():
    return render_template('home.html')


@webapp.route("/blog")
def blog():
    return render_template('blog.html')


@webapp.route("/about")
def about():
    return render_template('about.html')


@webapp.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    webapp.run(debug=True)
