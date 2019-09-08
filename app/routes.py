from app import app, jsonify

url_apiV1 = '/api/v1'
url_resources = url_apiV1 + '/resources'
url_books = url_resources + '/books'

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
def index():
    return 'Hello FriTease!'


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
