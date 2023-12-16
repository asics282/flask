from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.get('/submit/')
def submit_get():
    return render_template('form.html')

@app.post('/submit/')
def submit_post():
    num = request.form.get('num')
    res = f'{(int(num)**2)}'
    # передача num и res как параметры в redirect
    return redirect(url_for('result', num=num, res=res))

@app.route('/result/')
def result():
    num = request.args.get('num')
    res = request.args.get('res')
    return render_template('result.html', num=num, res=res)

if __name__ == '__main__':
    app.run(debug=True)