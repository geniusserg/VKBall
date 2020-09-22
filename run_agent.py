import vk_api
import random
import time 

####Variables############################
access_token = ""
group_user_id = ""
group_hse_id = ""
message = "Данилов Сергей 18ПИ-2"
latest_record = {}

####Code#################################

print("VK Volleyball initial")
vk = vk_api.VkApi(token=access_token, scope=4096)
if not (vk):
	print ("Failed auth")
	wait = input()
	exit()
api = vk.get_api()
print("Authentication successful")

for i in range(0, 3):
	print("Fetch latest record from public")
	latest_record = api.wall.get(owner_id=group_hse_id, count=1)
	print("Message: "+latest_record[0]["id"]+" >>>  "+latest_record[0]["text"])
	time.sleep(60)
wait = input()