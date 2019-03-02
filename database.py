#author:xzh#

import pymysql

db = pymysql.connect(host="115.28.79.206", user="root",password="f408909685", db="book_xzh", port=3306)

def search_content(key_word, start, limit):
    """"""
    db.ping(reconnect=True)
    cur = db.cursor()

    sql = "select * from spider_data where title like '%{0}%' limit {1}, {2}".format(key_word, start, limit)

    cur.execute(sql)
    results = cur.fetchall()
    # print(results)

    results_list = []
    for row in results:
        each_dic = {}
        id = row[0]
        each_dic["id"] = id
        url = row[1]
        each_dic["url"] = url
        title = row[2]
        each_dic["title"] = title
        results_list.append(each_dic)

    return results_list

def search_content_number(key_word):
    """"""
    cur = db.cursor()

    sql = "select count(*) from spider_data where title like '%{0}%' ".format(key_word)

    cur.execute(sql)
    results = cur.fetchall()
    number = results[0][0]

    return number

def all_data():
    """"""
    cur = db.cursor()
    sql = "select count(*) from spider_data"
    cur.execute(sql)
    result = cur.fetchall()
    print(result)

def insert_data(title, short_url):
    """"""
    cur = db.cursor()
    sql = "insert into spider_data (title, complete_url) values('{0}', '{1}')".format(title, short_url)
    try:
        print(sql)
        cur.execute(sql)  # 执行sql语句
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        raise e

def close_db():
    """"""

    db.close()



def select_all_complete_url():
    """
    查询所有的url   若爬虫拿到了一个url 判断在不在所有url列表里面 如果在 则不往数据库中添加了！
    :return:
    """

    cur = db.cursor()
    sql = "select complete_url from spider_data"
    result_list = []
    try:
        cur.execute(sql)  # 执行sql语句

        results = cur.fetchall()  # 获取查询的所有记录
        # print("id", "name", "password")
        # print(results)
        # 遍历结果

        for row in results:
            url = row[0]
            result_list.append(url)
            # print(url)
    except Exception as e:
        raise e
    finally:
        return result_list

