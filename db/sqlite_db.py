import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('db.db')
    cur = base.cursor()
    if base:
        print('DB connected')
    base.execute('Create table if not exists menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('insert into menu values (?,?,?,?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * from menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             '{0}\nОписание: {1}\nЦена: {2} руб.'.format(ret[1], ret[2], ret[-1]))

async def sql_read_for_delete():
    return cur.execute('SELECT * from menu').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM menu where name == ?',(data,))
    base.commit()
