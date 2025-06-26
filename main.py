from flask import Flask, render_template
import requests

app= Flask(__name__)

posts = requests.get('https://api.npoint.io/43ec212597620120ff6c').json()

@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)
@app.route('/contact')
def contact():
    return render_template("contact.html")
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/post/<int:index>')
def show_post(index):
    cur_page = None
    for item in posts:
        if item['id'] == index:
            cur_page= item
            return render_template('post.html', post=cur_page)



if __name__=="__main__":
    app.run(debug=True)