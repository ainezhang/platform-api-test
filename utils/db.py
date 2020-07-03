import pymysql


class DB:

    def __init__(self):
        # 创建连接
        self.conn = pymysql.connect(
            host="rm-uf6f65xnlzrv74lxaao.mysql.rds.aliyuncs.com",
            user="plat_dev",
            password="ILpg6yNn0MQbDc0sLqjJ",
            port=3306,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor  # sql语句返回结果是字典类型
        )
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def query(self, sql, args=None, is_all=False):
        """
        :param sql:
        :param args:
        :param is_all:是否查询多条记录
        :return:
        """
        self.cursor.execute(sql, args=args)
        self.conn.commit()
        if is_all:
            # 返回多条数据
            data = self.cursor.fetchall()
        else:
            # 返回一条数据
            data = self.cursor.fetchone()
        print(data)
        return data

    def exec(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            # 发生错误时回滚
            self.conn.rollback()
            print(str(e))


if __name__ == "__main__":
    mysql = DB()
    # sql1 = "SELECT * from bbs_activity_calendar.act_info WHERE game_biz='bbs_cn'"
    # ret1 = mysql.query(sql1)
    sql2 = "DELETE from bbs_activity_calendar.act_info WHERE name='bbs54';"
    ret2 = mysql.exec(sql2)
