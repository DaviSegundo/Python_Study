from db import DB, SQLite

db = DB()

def blog_lst_to_json(item):
    """Transform database instance into a dict."""
    return {
        'id': item[0],
        'published': item[1],
        'title': item[2],
        'content': item[3],
        'public': bool(item[4])
    }

def fetch_blogs():
    """Fetch blogs with context manager."""
    # db.execute('SELECT * FROM blogs WHERE public=1')
    # data = db.fetchall()

    # result = list(map(blog_lst_to_json, data))

    # db.close_connection()

    # return result

    with SQLite() as cur:
        cur.execute('SELECT * FROM blogs WHERE public=1')
        data = cur.fetchall()

        result = list(map(blog_lst_to_json, data))

        return result

def fetch_blog(id: str):
    """Fetch blogs with database abstration layer."""
    db.execute('SELECT * FROM blogs WHERE id=?', [id])
    data = db.fetchone()

    result = blog_lst_to_json(data)

    db.close_connection()

    return result