import sys
from flask import Flask, render_template, redirect
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
import application

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

application = Flask(__name__)
flatpages = FlatPages(application)
freezer = Freezer(application)
application.debug=True
application.config.from_object(__name__)


@application.route('/')
def home():
    return redirect("/resume/", code=302)

@application.route('/resume/')
def resume():
    return render_template('resume.html')

@application.route('/projects/')
def projects():
    return render_template('projects.html')

@application.route("/blog/")
def blog():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item:item['date'], reverse=False)
    return render_template('blog.html', posts=posts)

@application.route('/blog/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)



if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        application.run(host='0.0.0.0', port=8080, debug=True)
