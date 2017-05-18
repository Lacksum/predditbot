import praw
import config
import time
import os
import random
import csv

#Strings for quick editing
bot_commands = "Current commands:\n\n- truth or dare\n\n- tell me a joke\n\n- make me a sandwich\n\n- info\n\n- help"
bot_info = "Hi!  I'm ploungebot v0.1.3\n\nI run on python and use [reddit API](https://www.reddit.com/dev/api/) to interact with reddit and you\n\nTo see a command list try \"!ploungebot commands\"\n\n---\n\n ^^To ^^report ^^a ^^problem ^^or ^^issue ^^[message](https://www.reddit.com/message/compose?to=Lacksum&subject=&message=) ^^my ^^creator."
bot_name = "!ploungebot"
pony_string = ['fluttershy','rainbow','rarity','pinkie','twilight','applejack']
tord_list = ['Truth','Dare']

def bot_login():                                                                #log into reddit
    print("Logging in....")
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "ploungebot by /u/Lacksum v0.1")
    print("sucessfully logged in!")
    return r

def run_bot(r, comments_replied_to_v2):                                         #search and post comment

    print("Searching for comment")
    for comment in r.subreddit('randomcss').comments(limit=5):                 #Subreddit goes here

            if "!ploungebot tell me a joke"  in comment.body and comment.id not in comments_replied_to_v2 and not comment.author == r.user.me():
                print ("Joke string found!")
                with open('Joke.txt', newline='') as inputfile:
                    results = list(csv.reader(inputfile))
                print("Randomising")
                results2 = random.choice(results)                                   #random for row
                resultfinal = random.choice(results2)                               #random for collum
                comment.reply(resultfinal)
                print("Replied to comment")
                comments_replied_to_v2.append(comment.id)
                with open ("comments_replied_to_v2.txt", "a") as f:
                    f.write(comment.id + "\n")

            if "!ploungebot commands" in comment.body and comment.id not in comments_replied_to_v2 and not comment.author == r.user.me():
                print("Commands requested!")
                comment.reply(bot_commands)
                print("Replied to command request")
                comments_replied_to_v2.append(comment.id)
                with open ("comments_replied_to_v2.txt", "a") as f:
                    f.write(comment.id + "\n")

            if "!ploungebot help" in comment.body and comment.id not in comments_replied_to_v2 and not comment.author == r.user.me():
                print("Help requested!")
                comment.reply("try using \"!ploungebot commands\" or \"!ploungebot info\"")
                print("Replied to help request")
                comments_replied_to_v2.append(comment.id)
                with open ("comments_replied_to_v2.txt", "a") as f:
                    f.write(comment.id + "\n")

            if "!ploungebot info" in comment.body and comment.id not in comments_replied_to_v2 and not comment.author == r.user.me():
                print("Info requested!")
                comment.reply(bot_info)
                print("Replied to info request")
                comments_replied_to_v2.append(comment.id)
                with open ("comments_replied_to_v2.txt", "a") as f:
                    f.write(comment.id + "\n")

            if "!ploungebot make me a sandwich" in comment.body and comment.id not in comments_replied_to_v2 and not comment.author == r.user.me():
                print("sandwich requested!")
                comment.reply("[Here's your sandwich](http://i.imgur.com/5jAchta.png)")
                print("Replied to sandwich request")
                comments_replied_to_v2.append(comment.id)
                with open ("comments_replied_to_v2.txt", "a") as f:
                    f.write(comment.id + "\n")

            if "!ploungebot truth or dare" in comment.body and comment.id not in comments_replied_to_v2 and not comment.author == r.user.me():
                print("T or D requested!")
                comment.reply(random.choice(tord_list))
                print("Replied to T or D request")
                comments_replied_to_v2.append(comment.id)
                with open ("comments_replied_to_v2.txt", "a") as f:
                    f.write(comment.id + "\n")

            if "!ploungebot" in comment.body and comment.id not in comments_replied_to_v2 and not comment.author == r.user.me():
                print("USER INPUT ERROR")
                comment.reply("I don't understand that command.\n\nFor a list of commands type \"!ploungebot commands\"")
                print("Replied to USER INPUT ERROR")
                comments_replied_to_v2.append(comment.id)
                with open ("comments_replied_to_v2.txt", "a") as f:
                    f.write(comment.id + "\n")

#Script for counting ponies if statement.  Needs new def line seprate statements for while true statements
            if any(x in comment.body for x in pony_string):
                if comment.id not in comments_replied_to_v2 and not comment.author == r.user.me():
                    print("pony found")
                    print("comment ID is:", comment.id)
                    if "twilight" in comment.body:
                        print("found twilight")
                        comment.reply("Did I hear you say twilight?")
                    if "fluttershy" in comment.body:
                        print("found fluttershy")
                        comment.reply("Did I hear you say fluttershy?")
                    if "rarity" in comment.body:
                        print("found rarity")
                        comment.reply("Did I hear you say rarity?")
                    if "rainbow" in comment.body:
                        print("found rainbow")
                        comment.reply("Did I hear you say rainbow dash?")
                    if "pinkie" in comment.body:
                        print("found pinkie")
                        comment.reply("Did I hear you say pinkie pie?")
                    if "applejack" in comment.body:
                        print("found applejack")
                        comment.reply("Did I hear you say applejack?")

                    comments_replied_to_v2.append(comment.id)
                    with open("comments_replied_to_v2.txt", "a") as f:
                        f.write(comment.id + "\n")

    print("No more comments found\nSleeping for 5 seconds\n ---------------------")
    time.sleep(5)

def get_saved_comments():
                                                                                #cmmnt check for previous reply
    if not os.path.isfile("comments_replied_to_v2.txt"):
        comments_replied_to_v2 = []

    else:
        with open("comments_replied_to_v2.txt", "r") as f:
            comments_replied_to_v2 = f.read()
            comments_replied_to_v2 = comments_replied_to_v2.split("\n")

    return comments_replied_to_v2

r = bot_login()
comments_replied_to_v2 = get_saved_comments()
print("comments_replied_to_v2")

while True:
    run_bot(r, comments_replied_to_v2)
