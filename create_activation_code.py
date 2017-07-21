
"""生成200个激活码，且保存到数据库中"""
import random
import uuid
import sys
from pymysql import connect
class DB():
    def __init__(self):
        self.conn = connect(host="127.0.0.1", user="root", password="123456", db="wq_test")

    def insert(self, table_name, data):
        sql = "insert into " + table_name + "(activation)" + " values" + " (" + "'" + data + "'" + ")"
        with self.conn.cursor() as cur:
            print(sql)
            cur.execute(sql)

            self.conn.commit()

    def close(self):
        self.conn.close()

class CreateActivation():
    def __init__(self, count):
        self.count = count

    def create_activation(self):
        res = []
        for i in range(0, self.count):
            res.append(str(uuid.uuid4()))
        return res


if __name__ == '__main__':
    #不传入任何参数时默认生成10个
    if len(sys.argv) != 2:
        count = 10
        print (sys.argv)
    else:
        count = sys.argv[-1]
        print(sys.argv)
    for l in CreateActivation(int(count)).create_activation():
        DB().insert("activation_code", l)
        print (l)
