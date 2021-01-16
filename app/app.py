from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
   return (render_template("hello.html", x="World"))

@app.route('/foo/<color>/<x>')
def foo(color, x):
   return (render_template("hello.html", color=color, x=x))

if __name__ == '__main__':
   app.run()
