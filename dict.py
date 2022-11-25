"""
Tipe data Dictionary
"key": "value"
tidak diperkenankan mengisi key dengan tipe angka
standart string python menggunakan petik tunggal '
JSON Format tanda kuting ganda "
"""
import json

# Intro
users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}
print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"])
print(users["address"]["street"])
print(users["address"]["geo"])
print(users["address"]["geo"]["lat"])
print(users["address"]["geo"]["lng"])

"""
convert Dictionary to JSON
using package JSON
"""

print(users)
print(type(users))
print('\nUbah dict to JSON')
# Get a JSON formatted string
print('Konversi Dict to Object String JSON')
result = json.dumps(users, indent=4)
print(result)
print(type(result))

print('\nMembuat dan menulis json ke sebuah file')
print('Menulis Object to String JSON')
with open("result.json", 'w') as file:
    json.dump(result, file)
