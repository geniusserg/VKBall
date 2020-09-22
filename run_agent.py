import vk_api
import random
import time 
import getpass

####Variables############################
access_token_app = "" #Application token 
access_token_user = "" #Fake group here
group_hse_id = 0 #Id of group with which we work
user_vk_id = 0 #Real user id, need to send notifications
comment_message = "" #Here you write the comment
latest_record = 0

####Code#################################
print("VK Volleyball initial")
vk = vk_api.VkApi(token=access_token_app, scope=4096+8192)
vk_user = vk_api.VkApi(token=access_token_user, scope=4096+8192)
api = vk.get_api()
api_user = vk_user.get_api()
start_script_execution=1
###Fetch
for i in range(0, 3):
	print("Fetch latest record from public")
	latest_record_tmp = api.wall.get(owner_id=group_hse_id, count=1)
	print("Message: "+str(latest_record_tmp["items"][0]["id"])+" >>>  "+latest_record_tmp["items"][0]["text"])
	if (latest_record_tmp["items"][0]["id"]!=latest_record):
		print("Got new post!")
		latest_record = latest_record_tmp["items"][0]["id"]
		if start_script_execution==1: 
			print("This is a start of the work of application")
			start_script_execution = 0
		else:
			print("Leave comment")
			api_user.wall.createComment(owner_id=group_hse_id, post_id=latest_record, message=comment_message)
			private_message = "ВНИМАНИЕ!!! Вы были записаны на волейбол на "+latest_record_tmp["items"][0]["text"].split("\n")[0]+" \nПроверьте комментарий во избежание черезвычайной ситуации"
			print("Send message: \n"+private_message)
			api_user.messages.send(user_id=user_vk_id, random_id=random.randint(0,100), message=private_message)
	time.sleep(10)
