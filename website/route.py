from website import app


@app.route('/')
def hello():
    print('test')
    return "Bonjour Julia"
