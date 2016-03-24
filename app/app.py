from flask import Flask, render_template

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')
	
@app.route('/location')
def render_location():
    return render_template('location.html')
	
@app.route('/restaurant')
def render_restaurant():
    return render_template('restaurant.html')
	
@app.route('/category')
def render_category():
    return render_template('category.html')
	
@app.route('/about')
def render_about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1')
