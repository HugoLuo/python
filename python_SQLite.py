import sqlite3

def create_sqlite_db():
    # 创建到数据库文件的链接
    conn = sqlite3.connect("example.db")

    #获得一个游标对象c ,以便用其对数据进行操作。
    c = conn.cursor()
    # c.execute('CREATE TABLE tab1(username text)')
    # # c.execute('insert into tab1 values("Hugo")')
    # c.execute('select * from tab1')
    # search_result=c.fetchall()
    # print(search_result)

    # c.execute('CREATE TABLE stocks(date text,trans text,symbol text,qty real,price real)')
    # c.execute('INSERT INTO stocks VALUES("2023-10-9","BUY","Symbol",100,10.23)')
    c.execute('INSERT INTO stocks VALUES("2024-10-9","BUY","CLPS",1000,6.23)')
    c.execute('select * from stocks')
    search_result=c.fetchall()
    print(search_result)

    conn.commit()
    conn.close()
create_sqlite_db()