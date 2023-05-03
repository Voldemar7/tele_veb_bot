import sqlite3

user_base: dict[str, str] = {
    'login': '',
    'password': '',
    'user_id': '',
    'username': '',
    'full_name ': '',
}


def append_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                 (user_id INTEGER PRIMARY KEY, 
                  username TEXT, 
                  full_name TEXT,
                  login TEXT,
                  password TEXT)''')

    user_data = (user_base['user_id'],
                 user_base['username'],
                 user_base['full_name'],
                 user_base['login'],
                 user_base['password'],
                 )
    cursor.execute(
        'REPLACE INTO users (user_id, username, full_name, login, password) VALUES (?, ?, ?, ?, ?)',
        user_data)

    conn.commit()
    conn.close()
