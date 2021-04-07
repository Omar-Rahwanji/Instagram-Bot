# Done By Omar Rahwanji 0780985363
import shutil
from instabot import Bot

shutil.rmtree("config", ignore_errors=True)                               # delete config folder
bot = Bot()                                                               # create a bot
bot.login(username="AddYourUserNameHere", password="AddYourPasswordHere")          # log in
# Sending a single message to a user
bot.send_message(text="AddTheMessageHere",user_ids=bot.get_user_id_from_username("AddYourUserNameHere"))

# ----------------------------------------------------------------------------

# Following each user on the request list + Sending them a welcome message
newFollowers = bot.get_pending_follow_requests()                          # get a list of IDs of users in request list
for follower in newFollowers:
    bot.follow(follower)                                                  # follow each user
    bot.send_message(text="Thanks for Following Us!", user_ids=follower)  # send each user a message

# ----------------------------------------------------------------------------
