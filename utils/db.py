import pymysql
from utils.log import get_logger

log = get_logger('db')

DB_CONF = dict(
    host="rm-uf6f65xnlzrv74lxaao.mysql.rds.aliyuncs.com",
    port=3306,
    user="plat_dev",
    password="ILpg6yNn0MQbDc0sLqjJ",
    charset="utf8",
    autocommit=True
)


class DB(object):
    def __init__(self):
        # 创建连接,sql语句返回结果是字典类型
        self.conn = pymysql.connect(**DB_CONF)
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def query(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        result = self.cursor.fetchall()
        log.debug(f'查询sql:{sql}查询结果:{result}')
        print(result)
        return result

    def exec(self, sql):
        try:
            self.cursor.execute(sql)
            log.debug(f'执行sql:{sql}')
        except Exception as e:
            # 发生错误时回滚
            self.conn.rollback()

# if __name__ == "__main__":
#     mysql = DB()
#     sql1 = "SELECT * from bbs_activity_calendar.act_info WHERE game_biz='bbs_cn'"
#     ret1 = mysql.query(sql1)
#     print(ret1[0]['id'])
#     sql2 = "DELETE from bbs_activity_calendar.act_info WHERE name='bbs54';"
#     ret2 = mysql.exec(sql2)
