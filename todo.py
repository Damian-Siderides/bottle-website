import sqlite3
from bottle import route, run, debug, template, request, static_file, get, post

@route('/')
def home():
    return template('home')

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
#    result = c.fetchall()
#    return str(result)
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output


@route('/new', method='GET')
def new_item():

    if request.GET.save:
        new = request.GET.task.strip()

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        return template('new_task.tpl')


@route('/edit/<no:int>', method='GET')
def edit_item(no):

    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()

        return '<p>The item number %s was successfully update</p>' % no
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no),))
        cur_data = c.fetchone()

        return template('edit_task', old=cur_data, no=no)


@route('/help')
def help():
    return static_file('help.html', root='./') # (filename, path to the folder)


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
        return username#"<p>Your login information was correct.{{username}} {{password}}</p>"
    else:
        return username#"<p>Login failed.</p>{{username}} {{password}}"



def check_login(username, password):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT password FROM data WHERE username LIKE 'john'")
    cur_data = c.fetchone()

    if password == cur_data:
        return True
    else:
        return False


run(reloader=True)
