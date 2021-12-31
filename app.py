from flask import Flask, request, render_template
from stories import Story

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in pre-covid {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

app = Flask(__name__)

@app.route('/')
def show_madlibs():
    prompts = story.prompts
    
    return render_template('madlibs.html', prompts_list=prompts)

@app.route('/story')
def show_story():
    answer = request.args
    madlib = story.generate(answer)
    return render_template('story.html', madlib = madlib)