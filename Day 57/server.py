from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    name = 'Vinzce Yadao'
    return render_template('index.html', number=random_number, year=current_year, name=name)

@app.route('/guess/<name>')
def guess(name):
    age_response = requests.get(url="https://api.agify.io", params={'name': name})
    gender_response = requests.get(url='https://api.genderize.io', params={'name': name})
    return render_template('index1.html', name=name.title(), age=age_response.json()['age'], gender=gender_response.json()['gender'])

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = 'https://api.npoint.io/d8f5f122aa01ca7e3575'
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)



if __name__ == '__main__':
    app.run(debug=True)