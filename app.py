from flask import Flask, request, render_template

# initiaslize flask object
app = Flask(__name__)

# Create routes to front end
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def about():
    return render_template('about.html')


@app.route('/')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug = True)