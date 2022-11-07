from flask import Flask,render_template

app = Flask (__name__)

@app.route('/')  # main page
def hello():
    return render_template('index.html',message="hello brother, Lets have some fun!!",imgname="hello")

@app.route('/<username>') # dynamic route
def hello_user(username):
    username=username.lower()
    result = numerology(username)
    return render_template('index.html',message=username+": "+result,imgname="jenkins")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
