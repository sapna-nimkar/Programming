import json
import string

with open("./handle_json.json", "r") as file_stream:
    data = json.load(file_stream)

with open("./updated_json.json", "w") as file_stream:
    updated = []
    for name in data:
        fname = name["fname"]
        lname = name["lname"]
        updated.append({
            "fname": fname,
            "lname": f"{lname} Samantray"
        })
    x = json.dump(updated, file_stream)
    print('ccccccccccc')
    print(x)
    print('ccccccccccc')

print(f"Number of items are: {len(data)}")

json_string = '{"loc": "Barwani", "staple": "Upale"}'

print(type(updated), type(json.dumps(updated)), json.dumps(updated))

data = json.loads(json_string)
print(data['staple'])

x = json.loads("[\"Barwani ke, upale\", \"Barwani ke, kande\"]")
print(x, len(x))
