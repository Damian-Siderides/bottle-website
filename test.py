from bottle import route, run, template, get, post, request # or route

@route('/hello')
def hello():
    return "Hello World!"


@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)




@get('/login')
def login():
    return '''
<form action="/login" method="post">
    Username: <input name=:username" type="text" />
    Password: <input name=:password" type="password" />
    <input value="Login" type="submit" />
</form>
'''

@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"



run(hote='localhost', port=8080, debug=True)
