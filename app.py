from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "password"

debug = DebugToolbarExtension(app)


@app.route("/")
def get_words():
    """Create form to prompt for words."""

    prompts = story.prompts

    return render_template("questions.html", prompts=prompts)


@app.route("/story")
def show_story():
    """Display story with user answers."""

    text = story.generate(request.args)

    return render_template("story.html", text=text)