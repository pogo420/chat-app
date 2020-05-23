import sqlite3

class DB_connector:

    def __init__(self,databases):
     self.conn=sqlite3.connect(databases)

    def Read_from_DB(self, column_name, table_name, condition):
        """construct select query for reading data"""
        query= """SELECT {0} from {1}
                  where {2}  """.format(column_name,table_name,condition)
        cursor=self.conn.execute(query)
        rows=cursor.fetchall()
        # self.conn.close()
        return rows

    def insert_message(self,table_name, inserted_row):
        """insert query for writing in the datbase"""
        query= """ insert into {0}
                    values({1})
                """.format(table_name,inserted_row)

        self.conn.execute(query)
        self.conn.commit()
        self.conn.close()
        return True
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
        self.conn.execute(query)
        self.conn.commit()
        self.conn.close()
        return True

    def delete_message_DB(self,table_name, condition):
        """Creates a query which deletes record/records"""
        query = """DELETE FROM {0}
                        WHERE {1}""".format(table_name, condition)
        self.conn.execute(query)
        self.conn.commit()
        self.conn.close()
        return True




if __name__ == "__main__":
    print("Good")
