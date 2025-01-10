from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return ('<h1 style="text-align: center">Hello World!</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://marvelrivals.gg/wp-content/uploads/sites/47/2024/11/'
            'Black-Widow-Marvel-Rivals-Costume-White-Suit-1024x576.jpg" width=500>'
            '<img src=https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcW5jM2dscTQxYTA1ZnB4NmwxbDdvOHRocmZudWl5Z2o5'
            'NjY0eGQ3bSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OlPQEdkE7eOdZ22Ib4/giphy.webp width=500>')


def make_bold(function):
    def wrapper():
        return '<strong>' + function() + '</strong>'
    return wrapper

def make_emphasis(function):
    def wrapper():
        return '<em>' + function() + '</em>'
    return wrapper

def make_underlined(function):
    def wrapper():
        return '<u>' + function() + '</u>'
    return wrapper


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Bye!'

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == '__main__':
    app.run(debug=True)

