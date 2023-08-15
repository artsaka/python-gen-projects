from flask import Flask, render_template, request

app = Flask(__name__)

# define route
@app.route('/')
def index():
    # sending dictionary's data
    data = {"name": "Trillions", "age": 46, "salary": "190K"}    
    return render_template("index.html", mydata = data)

@app.route('/about')
def about():
    aboutUs = 'This page is about us'
    return render_template("about.html", aboutus = aboutUs)

@app.route('/admin')
def profile():
    username = "bicmac22"
    return render_template("admin.html")

@app.route('/product')
def product():
    products = ["clothes", "hats", "mens", "kids"]
    return render_template('product.html', products = products)

@app.route('/sendData')
def signupForm():    
   fname = request.args.get('fname')
   desc = request.args.get('description')
   return render_template("thankyou.html", data={"name": fname, "description": desc})

if __name__ == "__main__":
    app.run(debug=True) # เปิดดีบักโหมดเพื่อดูว่าเกิดข้อผิดพลาดอะไรในโค้ดของเรา
    # app.run()