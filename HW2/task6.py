from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/18/')
def submit_get():
    return render_template('age.html')


@app.post('/18/')
def submit_post():
    age = request.form.get('age')
    if int(age) < 18:
        return redirect(url_for('young'))
    return redirect(url_for('old'))


@app.route('/young/')
def young():
    return render_template('young.html')


@app.route('/old/')
def old():
    return render_template('old.html')


if __name__ == '__main__':
    app.run(debug=True)
