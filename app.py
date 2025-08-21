from flask import Flask, render_template
app = Flask(__name__, template_folder="templates", static_folder="static")

@app.get("/")
def home():
    # change "index.html" if your main file is named differently
    return render_template("index.html")

# add more routes as you discover pages, e.g.:
# @app.get("/about")
# def about(): return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
