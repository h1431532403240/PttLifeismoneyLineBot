import pymysql
import configparser
import getTime

# 讀取設置檔
config = configparser.ConfigParser()
config.read('config.ini')

# 設置資料庫資料
db_settings = {
    "host": config.get('MySQL', 'host'),
    "port": config.getint('MySQL', 'port'),
    "user": config.get('MySQL', 'user'),
    "password": config.get('MySQL', 'password'),
    "db": config.get('MySQL', 'db'),
    "charset": "utf8mb4"
}

def save(nrec, title, date):
    # 連線至資料庫
    connection = pymysql.connect(**db_settings)
    try:
        # 創建cursor object
        with connection.cursor() as cursor:
            # 新增一行資料
            sql = "INSERT INTO `charts`(`nrec`, `title`, `date`)VALUES(%s, %s, %s) ON DUPLICATE KEY UPDATE `nrec`=%s"
            cursor.execute(sql, (nrec, title, date, nrec))
            # 儲存改變資料
            connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()

def delete(title):
    connection = pymysql.connect(**db_settings)
    try:
        with connection.cursor() as cursor:
            # 刪除一行資料
            sql = "DELETE FROM `charts` WHERE `title`=%s"
            cursor.execute(sql, (title))
            connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()

def auto_push_message():
    import getPTTDB
    connection = pymysql.connect(**db_settings)
    try:
        with connection.cursor() as cursor:
            # 讀取推文數>20且send_message為0的文章
            sql = "SELECT * FROM `charts` WHERE `nrec`>=%s AND `send_message`!=1"
            cursor.execute(sql, (20))
            result = cursor.fetchall()
            # 如果有讀取到文章就執行，沒有就pass
            if result:
                List = []
                for r in result:
                    title = getPTTDB.get_title('https://www.ptt.cc/' + r[1])
                    List.append([title, 'https://www.ptt.cc/' + r[1]])
                # 將文章的send_message更改為1
                sql = "UPDATE `charts` SET `send_message`='1' WHERE `nrec`>=%s AND `send_message`!=1"
                cursor.execute(sql, (20))
                # 儲存改變資料
                connection.commit()
            else:
                pass
            return List
    except Exception as e:
        print(e)
    finally:
        connection.close()

def get_bang_article():
    import getPTTDB
    connection = pymysql.connect(**db_settings)
    try:
        with connection.cursor() as cursor:
            # 讀取爆文的文章
            sql = "SELECT * FROM `charts` WHERE `nrec`>=%s ORDER BY `title` DESC LIMIT 3 "
            cursor.execute(sql, (100))
            result = cursor.fetchall()
            # 如果有讀取到文章就執行，沒有就pass
            if result:
                List = []
                for r in result:
                    title = getPTTDB.get_title('https://www.ptt.cc/' + r[1])
                    List.append([title, 'https://www.ptt.cc/' + r[1]])
            else:
                pass
            return List
    except Exception as e:
        print(e)
    finally:
        connection.close()

def save_user_token(token):
    # 連線至資料庫
    connection = pymysql.connect(**db_settings)
    try:
        # 創建cursor object
        with connection.cursor() as cursor:
            # 新增使用者資料
            sql = "INSERT ignore INTO `users`(`user_token`)VALUES(%s)"
            cursor.execute(sql, (token))
            # 儲存改變資料
            connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()

def get_alluser_token():
    connection = pymysql.connect(**db_settings)
    try:
        with connection.cursor() as cursor:
            # 獲取全部使用者的token
            sql = "SELECT `user_token` FROM `users` WHERE 1"
            cursor.execute(sql)
            result = cursor.fetchall()
            # 如果有讀取到文章就執行，沒有就pass
            if result:
                token = []
                for r in result:
                    token.append(r[0])
            else:
                pass
            return token
    except Exception as e:
        print(e)
    finally:
        connection.close()