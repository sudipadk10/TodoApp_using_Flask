from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def helloworld():
    # return "Hello World"
    return render_template('index.html')

@app.route('/projects')
def projects():
    return 'This is project'

if __name__ == '__main__':
    app.run(debug=True)