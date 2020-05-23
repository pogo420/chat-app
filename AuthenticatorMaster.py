import json
import sys
from uuid import uuid4
from DB_connector import DB_connector

from datetime import datetime,timedelta


class Utilitities:

    def current_date_time(self)-> str:
        return str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def current_date_time_plus_n(self, n: int) -> str:
        return str((datetime.now()+timedelta(days=n)).strftime('%Y-%m-%d %H:%M:%S'))


# class TestDB:
#
#     def __init__(self, database):
#         self.connection = sqlite3.connect(database)
#
#     def db_write(self, column_name, value, table_name, condition):
#         query = """UPDATE {0}
#         SET {1} = '{2}'
#         WHERE {3}""".format(table_name, column_name, value, condition)
#         # print(query)
#         self.connection.execute(query)
#         self.connection.commit()
#         self.connection.close()
#
#     def db_read(self, column_name, table_name, condition):
#         query = """SELECT {1}
#         FROM {0}
#         WHERE {2}""".format(table_name, column_name, condition)
#         cursor = self.connection.execute(query)
#         # self.connection.close()
#         return cursor.fetchall()


class AuthenticatorMaster:

    def __init__(self, user_id, access_key, file_name):
        self.user_id = user_id
        self.access_key = access_key
        self.json_data = self.read_config(file_name)

    def read_config(self, file_name: str)->dict:
        '''Method for reading config data'''
        json_data = None
        with open(file_name) as f:
            json_data = json.load(f)
        return json_data

    def read_access_key(self)->list:
        '''Method for reading acces key'''
        # getting data fron config
        db = self.json_data.get("database")
        column_name = self.json_data.get("access_key_column_name")
        condition_column_name = self.json_data.get("user_id_column_name")
        table_name = self.json_data.get("table_name")

        # Sending instruction for data read
        user_id = self.user_id
        condition = "{0} = '{1}'".format(condition_column_name, user_id)
        obj = DB_connector(db)
        obj.Read_from_DB(column_name, table_name, condition)
        return obj.Read_from_DB(column_name, table_name, condition)

    # def read_exp_date(self)->list:
    #     '''Method for reading exp date'''
    #     # getting data fron config
    #     db = self.json_data.get("database")
    #     column_name = self.json_data.get("exp_date_column_name")
    #     condition_column_name = self.json_data.get("user_id_column_name")
    #     table_name = self.json_data.get("table_name")
    #
    #     # Sending instruction for data read
    #     user_id = self.user_id
    #     condition = "{0} = '{1}'".format(condition_column_name, user_id)
    #     # obj = TestDB(db)
    #     obj = DB_connector(db)
    #     obj.db_read(column_name, table_name, condition)
    #     return obj.db_read(column_name, table_name, condition)
    #
    # def write_access_key(self)->None:
    #     '''Method for writing acces key'''
    #     # getting data fron config
    #     db = self.json_data.get("database")
    #     column_name = self.json_data.get("access_key_column_name")
    #     condition_column_name = self.json_data.get("user_id_column_name")
    #     table_name = self.json_data.get("table_name")
    #
    #     # Sending instruction for data write
    #     key = self.generate_key()
    #     user_id = self.user_id
    #     condition = "{0} = '{1}'".format(condition_column_name, user_id)
    #     # obj = TestDB(db)
    #     obj = DB_connector(db)
    #     obj.db_write(column_name, key, table_name, condition)
    #     return None
    #
    # def write_exp_date(self)->None:
    #     '''Method for writing expiry date'''
    #     # getting data fron config
    #     db = self.json_data.get("database")
    #     column_name = self.json_data.get("exp_date_column_name")
    #     condition_column_name = self.json_data.get("user_id_column_name")
    #     table_name = self.json_data.get("table_name")
    #
    #     # Sending instruction for data write
    #     user_id = self.user_id
    #     current_date = Utilitities().current_date_time_plus_n(10)
    #     condition = "{0} = '{1}'".format(condition_column_name, user_id)
    #     # obj = TestDB(db)
    #     obj = DB_connector(db)
    #     obj.db_write(column_name, current_date, table_name, condition)
    #     return None
    #
    # def generate_key(self)->str:
    #     '''Method to generate keys'''
    #     return str(uuid4())
    #
    # def is_user_present(self)->bool:
    #     '''Method to return if user is present in db'''
    #     # getting data fron config
    #     db = self.json_data.get("database")
    #     column_name = self.json_data.get("user_id_column_name")
    #     condition_column_name = self.json_data.get("user_id_column_name")
    #     table_name = self.json_data.get("table_name")
    #
    #     # Sending instruction for data read
    #     user_id = self.user_id
    #     condition = "{0} = '{1}'".format(condition_column_name, user_id)
    #     # obj = TestDB(db)
    #     obj = DB_connector(db)
    #     temp = obj.db_read(column_name, table_name, condition)
    #     # print(temp)
    #     if len(temp)==0:
    #         return False
    #     return True
    #
    # def authenticate(self):
    #     '''Method for authentication'''
    #     if not self.is_user_present():
    #         print("User id:{} not present in db".format(self.user_id))
    #         sys.exit(0)
    #
    #     access_data = self.read_access_key()[0][0]
    #
    #     if access_data == self.access_key:
    #         if True:  # checking dates
    #             return (True, "Access verified")
    #         return (False, "Access key expired")
    #     return (False, "Access validation failed")


if __name__ == "__main__":
    user_id = "1234"
    access_key = "41241111-faa6-4f77-9fec-5b5f2b9b9d69"
    file_name = "access_config.json"
    # print(AuthenticatorMaster(user_id, access_key, file_name).authenticate())
    # print(AuthenticatorMaster(user_id, access_key, file_name).generate_key())
    # AuthenticatorMaster(user_id, access_key, file_name).write_access_key()
    # AuthenticatorMaster(user_id, access_key, file_name).write_exp_date()
    print(AuthenticatorMaster(user_id, access_key, file_name).read_access_key())
    # print(AuthenticatorMaster(user_id, access_key, file_name).read_exp_date())
    # print(AuthenticatorMaster(user_id, access_key, file_name).is_user_present())
