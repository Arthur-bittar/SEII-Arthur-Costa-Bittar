from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return render_template("index.html")

if __name__ == "__name__":
    app.run()
    
@app.route('/about')
def about():
    return 'foda né'