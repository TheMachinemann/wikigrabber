from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)


# Define a route for the homepage
@app.route("/")
def home():
    exec(open('htmlgrab.py').read())
    return render_template("page.html")


# Run the application
if __name__ == "__main__":
    app.run(debug=True)
