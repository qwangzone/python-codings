"""生成200个激活码，且保存到数据库中"""
import random
from pymysql import connect
class DB():
    def __init__(self):
        self.conn = connect(host="127.0.0.1", user="root", password="123456", db="wq_test")

    def insert(self, table_name, data):
        sql = "insert into " + table_name + "(activation)" + " values" + " (" + data + ")"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            print (sql)
            self.conn.commit()

    def close(self):
        self.conn.close()
class CreateActivation():

    def create_activation(self):
        i = 0
        b = []
        while i < 200:
            a = random.randint(1, 201)

            b.append(a)
            i = i + 1

        return b

create = CreateActivation()
insert = DB()
i = 0
while i < 200:
    insert.insert("activation_code", str(create.create_activation()[i]))
    i = i+1
insert.close()