from sqlite3 import connect
from sys import exc_info,exit
class DB_connector:

    def __init__(self,databases):
        self.conn=connect(databases)

    def read_from_db(self, column_name, table_name, condition):
        """construct select query for reading data"""
        query= """SELECT {0} from {1}
                  where {2}  """.format(column_name,table_name,condition)


        try:
            cursor=self.conn.execute(query)
            rows = cursor.fetchall()
            return rows
        except:
            print(exc_info()[1])
            print(query)
            return None
        #self.conn.close()


    def insert_message(self,table_name, inserted_row):
        """insert query for writing in the datbase"""
        query= """ insert into {0}
                    values({1})
                """.format(table_name,inserted_row)
        try:
            self.conn.execute(query)
            self.conn.commit()
            return 1
        except:
            print(exc_info()[1])
            print(query)
            return None

        # self.conn.close()


    def update_rows(self,table_name,column_name,value,condition):
        """Create a query to update row/rows(record/records) in table"""
        if isinstance(value,str):
            query = """UPDATE {0}
                SET {1} = '{2}'
                WHERE {3}""".format(table_name, column_name, value, condition)
        else:
            query = """UPDATE {0}
                            SET {1} = {2}
                            WHERE {3}""".format(table_name, column_name, value, condition)
        try:
            self.conn.execute(query)
            self.conn.commit()
            return 1
        except:
            print(exc_info()[1])
            print(query)
            return None
        # self.conn.close()


    def delete_message_DB(self,table_name, condition):
        """Creates a query which deletes record/records"""
        query = """DELETE FROM {0}
                        WHERE {1}""".format(table_name, condition)
        try:
            self.conn.execute(query)
            self.conn.commit()
            return 1
        except:
            print(exc_info()[1])
            print(query)
        # self.conn.close()


    def close_db(self):
        '''Method for connection closure'''
        try:
            self.conn.close()
        except:
            print(exc_info()[1])
            exit(0)
        return 1


if __name__ == "__main__":
    # Add uinit test cases
    #db = 'G:\Git_Code\chat-app\db\mydb.db'
    #inserted_message="1234,2548,'2020-05-19','N','Hello'"
    #DB_connector(db).insert_message('message_table',inserted_message)
    #DB_connector(db).delete_message_DB('message_table','abc')
    #DB_connector(db).update_rows('message_table','message','def', 'abc')
    #print(DB_connector(db).read_from_db('messag','message_table','sender=1234 and receiver= 2548'))
    pass

