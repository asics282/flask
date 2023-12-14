from flask import Flask, render_template

app = Flask(__name__)

html = """
    <h1> РИА Новости </h1>
"""


@app.route('/')
def head():
    return html


@app.route('/news/')
def news_block():
    _news = [
        {'data': "8.09.1812",
         'name': "Битва при Бородино",
         'description': "Русские войска дали отпор наполеону"},

        {'data': "25.04.1953",
         'name': "Расшифровка структуры ДНК",
         'description': "В журнале Nature опубликована статья \"Молекулярная структура нуклеиновых кислот: структура дезоксирибонуклеиновой кислоты\""},

        {'data': "19.07.1980",
         'name': "Олимпиада-80",
         'description': "В Москве открылись XXII Летние Олимпиийские иигры"}
    ]

    context = {"news": _news}

    return render_template('news.html', **context)

@app.route('/users/')
def users():
    _users = [{'name': 'Никанор',
    'mail': 'nik@mail.ru',
    'phone': '+7-987-654-32-10',
    },
    {'name': 'Феофан',
    'mail': 'feo@mail.ru',
    'phone': '+7-987-444-33-22',
    },
    {'name': 'Оверран',
    'mail': 'forest@mail.ru',
    'phone': '+7-903-333-33-33',
    }, ]
    context = {'users': _users}

    return render_template('users.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
