from datetime import datetime

import requests

pixela_endpoint="https://pixe.la/v1/users"
USERNAME="harshsh013"
TOKEN="1h3a2r0s0h2"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes",
}

# responce= requests.post(url=pixela_endpoint,json=user_params)
# print(responce.text)

graph_endpont=f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPH_ID="graph01"
graph_config={
    "id":GRAPH_ID,
    "name":"Running Graph",
    "unit":"Km",
    "type":"float",
    "color":"shibafu",
}
headers={
    "X-USER-TOKEN":TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)


#x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x


# graph_id="graph01"
# graph_config={
#     "id":graph_id,
#     "name":"Running Graph",
#     "unit":"Km",
#     "type":"float",
#     "color":"shibafu",
# }
# headers={
#     "X-USER-TOKEN":TOKEN,
# }
# # response=requests.post(url=graph_endpont,json=graph_config,headers=headers)
# # print(response.text)
# today=datetime.now()
# # print(today.strftime("%Y%m%d"))
# pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
# pixel_config={
#     "date":today.strftime("%Y%m%d"),
#     "quantity": input("How many kilometers did you cycle today? "),
# }
# response=requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
# print(response.text)
# update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
# new_pixel_data = {
#     "quantity": "4"
# }
#
# # PUT
# # response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# # print(response.text)
#
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
#
# #
# # ## DELETE
# # response = requests.delete(url=delete_endpoint, headers=headers)
# # print(response.text)

