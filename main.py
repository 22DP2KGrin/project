from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import threading

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Nepieciešams sesiju darbībai Flask

# Ceļš uz datu bāzi
db_path = '../example.db'


class Database:
    def __init__(self, path):
        self.path = path

    def connect(self):
        return sqlite3.connect(self.path)

    def execute(self, query, parameters=(), fetchone=False, fetchall=False, commit=False):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query, parameters)
        if commit:
            connection.commit()
        if fetchone:
            result = cursor.fetchone()
        elif fetchall:
            result = cursor.fetchall()
        else:
            result = None
        connection.close()
        return result


class Note:
    def __init__(self, title, content, folder, user_id, timestamp=None):
        self.title = title
        self.content = content
        self.folder = folder
        self.user_id = user_id
        self.timestamp = timestamp

    def save(self):
        db = Database(db_path)
        db.execute("INSERT INTO notes (title, content, folder, user_id) VALUES (?, ?, ?, ?)",
                   (self.title, self.content, self.folder, self.user_id), commit=True)

    def delete(self):
        db = Database(db_path)
        db.execute("DELETE FROM notes WHERE id=?", (self.id,), commit=True)

    @staticmethod
    def get_by_id(note_id):
        db = Database(db_path)
        result = db.execute("SELECT * FROM notes WHERE id=?", (note_id,), fetchone=True)
        if result:
            return Note(*result)
        else:
            return None

    @staticmethod
    def get_all(user_id):
        db = Database(db_path)
        result = db.execute("SELECT * FROM notes WHERE user_id=?", (user_id,), fetchall=True)
        notes = []
        for item in result:
            notes.append(Note(*item))
        return notes


class User:
    def __init__(self, username, password, id=None):
        self.id = id
        self.username = username
        self.password = password

    def save(self):
        db = Database(db_path)
        db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (self.username, self.password), commit=True)

    @staticmethod
    def get_by_username_and_password(username, password):
        db = Database(db_path)
        result = db.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password), fetchone=True)
        if result:
            return User(*result)
        else:
            return None


# Funkcija datu bāzes pieprasījumu izpildei atsevišķā pavedienā
def db_notes():
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS table_name
                      (id INTEGER PRIMARY KEY,
                       name TEXT,
                       age INTEGER)''')

    cursor.execute("SELECT * FROM table_name")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    connection.close()


thread = threading.Thread(target=db_notes)
thread.start()
thread.join()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.get_by_username_and_password(username, password)
        if user:
            session['user_id'] = user.id
            return redirect(url_for('notes'))
        else:
            error_message = "Nepareizs lietotājvārds vai parole!"
    return render_template('login.html', error_message=error_message)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.get_by_username(username)
        if existing_user:
            return "Lietotājs ar šādu lietotājvārdu jau eksistē"
        else:
            new_user = User(username, password)
            new_user.save()
            return redirect(url_for('login'))
    return render_template('signup.html')


@app.route('/notes')
def notes():
    search_query = request.args.get('search', '')  # Iegūstam meklēšanas virkni no pieprasījuma
    user_id = session.get('user_id')  # Iegūstam user_id no sesijas

    if user_id:  # Pārbauda, vai lietotājs ir autentificējies
        notes = Note.get_all(user_id)
        if search_query:
            notes = [note for note in notes if search_query.lower() in note.title.lower() or
                     search_query.lower() in note.content.lower()]
        return render_template('notes.html', notes=notes)
    else:
        return redirect(url_for('login'))  # Ja lietotājs nav autentificējies, pāradresē uz pieteikšanās lapu


@app.route('/add_note', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    folder = request.form['folder']
    user_id = session.get('user_id')  # Iegūstam user_id no sesijas
    if user_id:  # Pārbauda, vai lietotājs ir autentificējies
        note = Note(title, content, folder, user_id)
        note.save()
        return redirect(url_for('notes'))
    else:
        return redirect(url_for('login'))  # Ja lietotājs nav autentificējies, pāradresē uz pieteikšanās lapu


@app.route('/delete_note/<int:id>', methods=['POST'])
def delete_note(id):
    note = Note.get_by_id(id)
    if note:
        note.delete()
    return redirect(url_for('notes'))


@app.route('/edit_note/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    note = Note.get_by_id(id)
    if not note:
        return "Piezīme nav atrasta", 404

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        folder = request.form['folder']
        note.title = title
        note.content = content
        note.folder = folder
        note.save()
        return redirect(url_for('notes'))
    else:
        return render_template('edit_note.html', note=note)


if __name__ == '__main__':
    app.run(debug=True)
