from flask_restful import reqparse
import requests

BASE = "http://127.0.0.1:5000/"

# data = [
#     {"likes": 10, "name": "video 1", "views": "100"},
#     {"likes": 20, "name": "video 2", "views": "200"},
#     {"likes": 30, "name": "video 3", "views": "300"}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# response = requests.delete(BASE + "video/0")
# print(response)

response = requests.put(BASE + "video/100",
                        {"views": 1, "likes": 1, "name": "video I am going to delete"})
print(response.json())

response = requests.patch(BASE + "video/2", {"views": 99, "likes": 99})
print(response.json())

response = requests.delete(BASE + "video/100")
print(response.json())

# response = requests.put(
#     BASE + "video/3", {"likes": 10, "name": "video 1", "views": "100"})
# print(response.json())

# response = requests.get(BASE + "video/6")
# print(response.json())
