from flask import Flask, request, render_template, g
import datetime

app = Flask(__name__)

@app.before_request  # Every time we get a request, first do this stuff.
def before_request():
    # get IP address from request
    g.ip = request.remote_addr
    # check for a name in any GET request
    if request.args.get('name'):
        g.name = request.args.get('name')

@app.route("/")
def index():
    now = datetime.datetime.now()
    g.now = now
    return render_template("my_index.html")

@app.route('/say_hi')
def say():
    return render_template("say_hi.html")

if __name__ == "__main__":
    app.run(debug=True)