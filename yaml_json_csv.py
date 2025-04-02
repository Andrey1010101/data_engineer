
import yaml
import json
data_yaml = [
    {
        "user_name": "elt_user",
        "passvord": "123"
    },
    {
        "user_name": "elt_user2",
        "passvord": "1234"
    },
    {
        "user_name": "elt_user3",
        "passvord": "12345"
    }
]

data_json = {
    "name": "Stas",
    "login": "Stas143",
    "Password": "143"
}

#with open(r'connection.yaml', 'a') as file:
#    documents = yaml.dump(data_yaml, file)

#with open(r'connection.yaml') as file:
#    data = yaml.load(file, Loader=yaml.FullLoader)

json_object = json.dumps(data_json, indent=4)

with open(r'date.json', 'w') as file:
    file.write(json_object)

with open(r'date.json', 'r') as file:
    data = json.load(file)

print(data)