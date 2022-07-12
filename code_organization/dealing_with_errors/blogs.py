from db import DB

db = DB()

def blog_lst_to_json(item):
    return {
        'id': item[0],
        'published': item[1],
        'title': item[2],
        'content': item[3],
        'public': bool(item[4])
    }

def fetch_blogs():
    cur = db.execute('SELECT * FROM blogs WHERE public=1')

    result = list(map(blog_lst_to_json, cur.fetchall()))

    db.close_connection()

    return result

def fetch_blog(id: str):
    cur = db.execute(f'SELECT * FROM blogs WHERE id="{id}"')

    result = blog_lst_to_json(cur.fetchone())

    db.close_connection()

    return result