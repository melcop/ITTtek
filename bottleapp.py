from bottle import route, run

@route('/')
def home():
    return "Velkommen til min hjemmeside!"

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)