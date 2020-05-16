import json

class Message_handling():

    def __init__(self,to_user_id,from_user_id):
        self.to_user_id = to_user_id
        self.from_user_id= from_user_id


    def read_message(self):
        with open(r'G:\Compare\Chat_db.json', "r") as read_it:
            data = json.load(read_it)

        for item in data['message_db']:
            if item['user_id'] == self.to_user_id:
                for mess in item['messages']:
                    if mess['from']== self.from_user_id:
                        print(mess['message'])

    def write_message(self,message_write):
        with open(r'G:\Compare\Chat_db.json', "r") as read_it:
            data = json.load(read_it)

        for item in data['message_db']:
            if item['user_id'] == self.to_user_id:
                item["messages"].append({'from': self.from_user_id, 'date': '2020-14-05', 'message': message_write})
                break
        with open(r'G:\Compare\Chat_db.json', 'w') as outfile:
            json.dump(data, outfile,indent=2)



if __name__ == "__main__":
    Message_handling(input("please enter user_id"),input("please enter the sender user id")).write_message("kire")