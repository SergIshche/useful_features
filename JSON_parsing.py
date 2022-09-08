#Зберігаємо дані в JSON
import json
dictData = { "ID"       : 310450,
             "login"    : "admin",
             "name"     : "James Bond",
             "password" : "root",
             "phone"    : 3330303,
             "email"    : " bond@mail.com",
             "online"   : True }
jsonData = json.dumps(dictData)
print(jsonData)


#розпарсити JSON!!!!!!!!!!!
import json

# строка которую будем парсить
json_string = """ {
  "orderID": 42,
  "customerName": "John Smith",
  "customerPhoneN": "555-1234",
  "orderContents": [
    {
      "productID": 23,
      "productName": "keyboard",
      "quantity": 1
    },
    {
      "productID": 13,
      "productName": "mouse",
      "quantity": 1
    }
  ],
  "orderCompleted": true
} """

# распарсенная строка
parsed_string = json.loads(json_string)

print(parsed_string)