from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/main/')
def head():
    return render_template('head.html')

@app.route('/products/')
def products():
    _products = [
        {'name': "Велосипед Merida Silex",
         'description': "Гревел",
         'link': 'https://d2lljesbicak00.cloudfront.net/merida-v2/crud-zoom-img//master/bikes/2022/SILEX_600_grnblk_MY2022.tif?p3',
         'price': 150000},

        {'name': "Велосипед Scott",
         'description': "MTB",
         'link': 'https://www.mag-russia.ru/f/product/280539_1699213_png_zoom_5.jpg',
         'price': 200000},

        {'name': "Велосипед Aist",
         'description': "Городской",
         'link': 'https://aist-velo.ru/uploads/product/7500/7520/20200322_144442.jpg',
         'price': 20000}
    ]

    context = {"products": _products}

    return render_template('product.html', **context)

if __name__ == '__main__':
    app.run(debug=True)