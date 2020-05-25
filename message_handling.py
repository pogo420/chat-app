import sqlite3
from DB_connector import DB_connector

class Message_handling:

    def __init__(self,to_user_id=None,from_user_id=None,message_Write=None):
        self.to_user_id = to_user_id
        self.from_user_id= from_user_id
        self.message_Write=message_Write

    def read_message(self):
        '''Reading unread message from data base and updating the read_flag'''

        db='G:\Git_Code\chat-app\db\mydb.db'
        column_name='message'
        table_name='message_table'
        condition= "sender='{0}' and receiver='{1}' and read_flag='N'".format(self.to_user_id,self.from_user_id)
        obj=DB_connector(db)
        rows=obj.read_from_db(column_name,table_name,condition)
        column_name='read_flag'  #for updating read_flag
        obj.update_rows(table_name,column_name,'Y',condition) #for updating read_flag
        obj.close_db()
        return (rows)

    def write_message(self):
        """writes chat message in the database table"""
        db = 'G:\Git_Code\chat-app\db\mydb.db'
        table_name = 'message_table'
        inserted_row ="{0},{1},'2020-05-19','N','{2}'".format(self.to_user_id,self.from_user_id,self.message_Write)
        obj = DB_connector(db)
        obj.insert_message(table_name,inserted_row)
        obj.close_db()
        return 1



    def delete_message(self):
        """deletes already read message"""
        db = 'G:\Git_Code\chat-app\db\mydb.db'
        table_name = 'message_table'
        condition = "read_flag='Y'"
        obj = DB_connector(db)
        obj.delete_message_DB(table_name,condition)
        obj.close_db()
        return 1


if __name__ == "__main__":
    message1=Message_handling(1254, 2548)
    #print(message1.write_message())
    print(message1.read_message())
    #Message_handling(1254,2548,'Hello Lovebird!!').write_message()
    #print(message1.delete_message())
#input("please enter user id"),input("please enter user id")