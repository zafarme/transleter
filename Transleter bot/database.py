import sqlite3

db = sqlite3.connect('bot.db')
sql = db.cursor()


sql.execute("""
CREATE TABLE IF NOT EXISTS  Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id int,
    phone_number varchar(255),
    user_name varchar(255)
    
);

""")


def add_user(telegram_id,phone_number,username):
    connection = sqlite3.connect('bot.db')
    sql = connection.cursor()

    sql.execute(
        """
            INSERT INTO users (telegram_id, phone_number,user_name)VALUES (?,?,?)
        """,(telegram_id,phone_number,username)
           )
    
    connection.commit()
    connection.close()


def delete_user(telegram_id):
    connection = sqlite3.connect('bot.db')
    sql = connection.cursor()

    sql.execute(
        '''
        DELETE FROM users WHERE telegram_id=?:
        ''',(telegram_id,)
    )
    connection.commit()
    connection.close()
    

def check_users(telegram_id):    
    connection = sqlite3.connect('bot.db')
    sql = connection.cursor()

    user = sql.execute(
        '''
        SELECT telegram_id FROM users WHERE telegram_id=?:
        ''',(telegram_id,)
    ).fetchone()


    if user:
        return True
    
    else:
        return False


while  True:
    telegram_id = input('tg.id: ')
    phone_number = input('number: ') 
    username = input('username: ') 

    add_user(telegram_id=telegram_id,phone_number=phone_number,username=username)





