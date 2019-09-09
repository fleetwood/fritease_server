from app import app, jsonify, render_template

url_apiV1 = '/api/v1'
url_resources = url_apiV1 + '/resources'
url_books = url_resources + '/books'
urls = {
    'api': url_apiV1,
    'resources': url_resources,
    'books': url_books
}

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city '
                       'Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Oh noes!</p>", 404


@app.route('/')
@app.route('/index')
@app.route('/book/<int:book_id>')
@app.route('/index/book/<int:book_id>')
def index(book_id=-1):
    results = []

    for book in books:
        if book_id and book_id == book['id']:
            results.append(book)
        if not book_id >= 0:
            results.append(book)

    return render_template('index.html', title='FriTease', content=results)


@app.route(url_books, methods=['GET'])
@app.route(url_books + '/', methods=['GET'])
@app.route(url_books + '/all', methods=['GET'])
def books_all():
    return jsonify(books)


@app.route(url_books + '/<int:book_id>', methods=['GET'])
def books_by_id(book_id):
    results = []

    for book in books:
        if book['id'] == book_id:
            results.append(book)

    return jsonify(results)
