import vk_api
import random
import time 

print("VK Volleyball initial")

vk = vk_api.VkApi(token="", scope=4096)
if not (vk):
	print ("Failed auth")
	wait = input()
	exit()
api = vk.get_api()
print("Authentication successful")
api.messages.send(user_id="", message= "[ " + str(time.time()) + " ] API v0.1 notification: service works", random_id=random.randint(1,1000000))
print("Message sent successfully")
wait = input()