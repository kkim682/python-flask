"""
basic route
    @app.route('/')
    def page():
        return "<div></div>"
dynamic route
    @app.route('/some_page/<name>')
    def other_page(name):
        return 'User: {}'.format(name)
debug mode
    app.run(debug=True) - for actual product, it should be False
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Pyppy!</h1>"

@app.route('/information')
def infor():
    return "<h1>Puppies are cute!</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is a page for {}</h1>".format(name)

if __name__ == '__main__':
    app.run()
    #app.run(debug=True)
