import json

class Message_handling():

    def __init__(self,to_user_id,from_user_id):
        self.to_user_id = to_user_id
        self.from_user_id= from_user_id


    def read_message(self):
        with open(r'G:\Compare\message_db.json', "r") as read_it:
            data = json.load(read_it)
        # [[print(item["messages"][i]["message"]) for i in range(len(item["messages"])) if item["messages"][i]["from"] == '1267'] for item in data if item["user_id"] == '1234' ]
        for item in data:
            if item["user_id"] == self.to_user_id:
                for i in range(len(item["messages"])):
                    if item["messages"][i]["from"] == self.from_user_id:
                        print(item["messages"][i]["message"])
                        item["messages"][i]["read_flag"] = 'Y'

        with open(r'G:\Compare\message_db.json', 'w') as outfile:
            json.dump(data, outfile,indent=2)

    def write_message(self,message_write):
        with open(r'G:\Compare\message_db.json', "r") as read_it:
            data = json.load(read_it)
        write = True
        for item in data:
            if item["user_id"]==self.to_user_id:
                item["messages"].append({'from': self.from_user_id, 'date': '2020-14-05', 'message': message_write,'read_flag':'N'})
                break
        if write:
            data.append({'user_id': self.to_user_id,
                         'messages': [{'from': self.from_user_id, 'date': '2020-08-05', 'message': message_write, 'read_flag': 'N'}]})
        with open(r'G:\Compare\message_db.json', 'w') as outfile:
            json.dump(data, outfile,indent=2)



if __name__ == "__main__":
    Message_handling(input("please enter user id"),input("please enter user id")).write_message("kire")