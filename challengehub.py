import discord
import os
import requests
import json
client = discord.client()
msg = message.content
def update_challenges(challenge):
	if challenges in db.keys():
		challenges = db["challenges"]
		challenges.append(challenge)
		db["chllenges"] = challenges
	else
		db["challenges"] = [challenge]
@client.event
async def on ready():
	print("{0.user} logged in".format(client))
@client.event
async def on message(message):
	if message.author == client.user:
		return
	if msg.startwith("hi" || "hello" || "hey"):
		first = print(""" Wlecome to the server , i'm the subjecthub bot how can i help you ?
			          1 - /challenge : get a challenge
			          2 - /push language challenge : add a challenge """)
	elif msg.startwith("/challenge"):
		await msg.send(challenge)
	elif msg.startwith("/push"):
		new_challenge = msg.split("/push ",1)[1]
		update_challenges(new_challenge)
		await msg.send("Challenge added successfuly")
client.run(os.getenv('TOKEN'))