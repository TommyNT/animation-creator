
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "here will be my upload interface"

@app.route("/make-animation")
def make_animation():
  return render_template(
          "make_animation.html",
          invitation="only limit is yourself")

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)
