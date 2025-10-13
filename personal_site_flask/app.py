from flask import Flask, render_template
from data import AWARDS, TESTIMONIALS, PROJECTS

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.context_processor
def inject_now():
    from datetime import datetime
    return {"current_year": datetime.now().year}

@app.route("/")
def home():
    return render_template("home.html", testimonials=TESTIMONIALS)

@app.route("/awards")
def awards():
    return render_template("awards.html", awards=AWARDS)

@app.route("/testimonials")
def testimonials():
    return render_template("testimonials.html", testimonials=TESTIMONIALS)

@app.route("/mywork")
def projects():
    return render_template("mywork.html", projects=PROJECTS)

if __name__ == "__main__":
    app.run(debug=True)
