import discord
import random
import json
import os
import requests
import pprint
from datetime import date, datetime, timedelta
import time
import asyncio
import aioschedule as schedule
import sqlite3
from sqlite3 import Error
import openai

path = os.getcwd()
print(path)
os.chdir(path)
apikey = "CMO8IJ4OTQFK"


with open("keys.json", "r") as f:
    keys = json.load(f)
openai.api_key = keys["openai"]
stop = "\n"
# chdir passt sich an, den String Path ändern, wenn du was machen willst

# Helper functions



class MyClient(discord.Client):

    # Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt.")
        with open("channels.json", "r") as f:
            channels = json.load(f)
        #channels["warkacken"] = 847741782225977354
        #with open("channels.json", "w") as f:
        #    json.dump(channels, f)
        #das hier vom erstellen von neuen jsons
        channel = client.get_channel((channels["bot"])) #Channel id wechseln wenn auf Siemens Server 848661221661999114 # channel id fürn testbot: 837716949240643634
        await channel.send('Bin stets zu Ihren Diensten')
    #Wenn Nachricht gepostet wird



    async def on_message(self, message):

        async def klopf(inhalt):
            satz = """-Knock knock
            -Who's there?
            -"""
            satz = satz + inhalt + """.
            -""" + inhalt + """ who?
            """
            anfrage = satz + "-"
            await message.channel.send(satz)
            antwort = openai.Completion.create(engine="curie", prompt=anfrage, stop=stop, temperature=0.3)
            choice = antwort["choices"][0]["text"]

            await message.channel.send("-"+choice)

        async def hitler():
            await message.delete()
            await message.channel.send("http://www.trunkworthy.com/wp-content/uploads/2016/03/a8ee99d84cd77f40824013f15c3b5c15e9f2b2c98d34eb73ff4c7e52f51d7e8b_1.gif")
        async def hehehehaw():
            await message.channel.send("https://tenor.com/view/clash-royale-emotes-laugh-smile-king-gif-14309345")
        async def grr():
            await message.channel.send("https://tenor.com/view/clash-royale-clashroyale-angry-gif-5302587")
        async def gifsuch(inhalt):
            #r = requests.get("https://api.tenor.com/v1/anonid?key=%s" % apikey)
            #await message.channel.send(json.loads(r.content)["anon_id"])
            r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&anon_id=%s" %
                (inhalt, apikey, 1, "248c90be1f634b3c810c6d060767f0a7"))
            top_8gifs = json.loads(r.content)
            await message.channel.send(top_8gifs["results"][0]["media"][0]["tinygif"]["url"])

        async def frage(inhalt):
            anfrage = "Q: " + inhalt + """
            A:"""

            antwort = openai.Completion.create(engine="curie", prompt=anfrage, stop=stop, temperature=0.3)
            choice = antwort["choices"][0]["text"]

            await message.channel.send(choice)
        # Andi-Arbeit1 Anfang
        async def frageGenau(inhalt):
            anfrage = "Q: " + inhalt + """
            A:"""

            antwort = openai.Completion.create(engine="curie", prompt=anfrage, stop=stop, temperature=0.0)
            choice = antwort["choices"][0]["text"]

            await message.channel.send(choice)
        # Andi-Arbeit1 Ende

        # reagiert nicht auf eigene Botnachrichten
        if message.author == client.user:
            return


        if message.content.startswith("!cringe"):
            cringe = ["🇹", "🇭", "🇦", "🇹", "🇸", "🇨", "🇷", "🇮", "🇳", "🇬", "🇪"]
            await message.delete()
            await message.channel.send("🇹 🇭 🇦 🇹 🇸 🇨 🇷 🇮 🇳 🇬 🇪")



        if message.content.startswith("!link"):
            link = ["http://donut.cf/", "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "http://donut.cf/wichtig.jpg", "http://www.republiquedesmangues.fr/", "http://endless.horse/", "https://heeeeeeeey.com/", "https://longdogechallenge.com/", "http://eelslap.com/", "https://thatsthefinger.com/", "https://puginarug.com/", "http://gurke.gq/", "https://stockx.com/de-de/adidas-yeezy-foam-rnnr-ararat", "https://i.imgur.com/4ipQcI8.jpg", "https://www.youtube.com/watch?v=5DlROhT8NgU", "https://www.youtube.com/watch?v=EuQfn-1Q09w&t=7s", "https://external-preview.redd.it/b25gXxDPv5T8UhpZLacaB1llx8Eul8S039j0LJzIswo.png?width=640&crop=smart&auto=webp&s=6e16f7e3e02612adfff312386f8bcb91d05a35d0","https://external-preview.redd.it/IyAa4qx3t-r5nmGbHQdTCUvNRRMwpZY2OZ6dXGXF0uo.png?auto=webp&s=0886e11a4333191958330c96f99bf04c2869faf2", "https://preview.redd.it/jx3yh2em89c61.jpg?width=640&crop=smart&auto=webp&s=422fd54a49c7eda8b6bdb03ef28c044f8d479cb9"] #hier gerne noch andere Links hinzufügen
            description = "do not click this [link](" + str(link[random.randrange(len(link))]) + ")!"
            embed_link = discord.Embed(colour=discord.Colour(0x9999), description=description)
            await message.channel.send(embed=embed_link)

        if message.content.startswith("!channel"):
            #channel = client.get_channel(id)
            #print(channel)
            print(message.channel.id)
        if message.content.startswith("!test"):
            1
        if message.content.startswith("!klopf"):
            mes = message.content.split(" ",1)
            try:
                zusatz2 = mes[1]
            except IndexError:
                zusatz2 = " "
            try:
                zusatz = mes[2]
            except IndexError:
                zusatz = " "
            mess = [mes[0].lower(), zusatz2.lower(), zusatz.lower()]
            if(zusatz2 != " "):
                await klopf(zusatz2)
        if message.content.startswith("!frage"):
            mes = message.content.split(" ", 1)
            try:
                zusatz2 = mes[1]
            except IndexError:
                zusatz2 = " "
            try:
                zusatz = mes[2]
            except IndexError:
                zusatz = " "
            mess = [mes[0].lower(), zusatz2.lower(), zusatz.lower()]
            if (zusatz2 != " "):
                await frage(zusatz2)
        #Andi-Arbeit2 Anfang
        if message.content.find("hitler"):
            zusatz = " "
        else:
            await hitler()
        if message.content.find("heheheha"):
            zusatz = " "
        else:
            await hehehehaw()
        if message.content.find("grr"):
            zusatz = " "
        else:
            await grr()

        if message.content.startswith("!gif"):
            mes = message.content.split(" ", 1)
            try:
                zusatz2 = mes[1]
            except IndexError:
                zusatz2 = " "
            try:
                zusatz = mes[2]
            except IndexError:
                zusatz = " "
            mess = [mes[0].lower(), zusatz2.lower(), zusatz.lower()]
            if (zusatz2 != " "):
                await gifsuch(zusatz2)
        if message.content.startswith("!frageGenau"):
            mes = message.content.split(" ", 1)
            try:
                zusatz2 = mes[1]
            except IndexError:
                zusatz2 = " "
            try:
                zusatz = mes[2]
            except IndexError:
                zusatz = " "
            mess = [mes[0].lower(), zusatz2.lower(), zusatz.lower()]
            if (zusatz2 != " "):
                await frageGenau(zusatz2)
        #Andi-Arbeit2 Ende
        if message.content.startswith("!Tamer"):
            await message.channel.send("Gamer ")
#====================================================================================================================================================================================================




client = MyClient()
with open("keys.json", "r") as f:
    keys = json.load(f)
client.run(keys["key"])
