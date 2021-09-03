import discord
import random
import json
import os
from datetime import date, datetime, timedelta
import time
import asyncio
import aioschedule as schedule
import sqlite3
from sqlite3 import Error


path = os.getcwd()
print(path)
os.chdir(path)


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

        # reagiert nicht auf eigene Botnachrichten
        if message.author == client.user:
            return


        if message.content.startswith("!cringe"):
            cringe = ["🇹", "🇭", "🇦", "🇹", "🇸", "🇨", "🇷", "🇮", "🇳", "🇬", "🇪"]
            await message.delete()
            await message.channel.send("🇹 🇭 🇦 🇹 🇸 🇨 🇷 🇮 🇳 🇬 🇪")

        if message.content.startswith("!help"):
            embed_help = discord.Embed(colour=discord.Colour(0x9999))

            embed_help.set_author(name="Snensbot Befehle")

            embed_help.add_field(name="!now", value="Gibt die aktuelle Stunde mit Zoomlink im Namen!!!! und Infos zum Fach zurück",
                                 inline=False)
            embed_help.add_field(name="!Fach <fach> ", value="Gibt das ausgewählte Fach (Zoomlink im Namen!!) mit Infos zurück",
                                 inline=False)
            embed_help.add_field(name="!spe oder !SPE",
                                 value="Gibt den derzeitigen SPE Link an (Gründer schaut drauf)",
                                 inline=False)
            embed_help.add_field(name="!spe edit <link> ",
                                 value="Ändert den SPE link",
                                 inline=False)
            embed_help.add_field(name="!link> ", value="link",
                                 inline=False)
            embed_help.add_field(name="reagiere mit :poop:", value="und es wird durch THAT'S CRINGE ersetzt",
                                 inline=False)
            embed_help.add_field(name="schreibe was in war-kacken-channel", value="und es wird kommentiert. Und btw hast du eine kleine Chance auf den Goldenen Shit",
                                 inline=False)
            embed_help.add_field(name="!e",value="ECONOMY",inline=False)
            embed_help.add_field(name="coin heads <zahl>", value="Coinflip", inline=False)
            embed_help.add_field(name="transfer <zahl> <user>", value="Geld Senden", inline=False)
            embed_help.add_field(name="banktransfer <zahl>", value="Geld in deine Bank", inline=False)
            embed_help.add_field(name="wallettransfer <zahl>", value="Geld in deinen Geldbeutel", inline=False)
            embed_help.add_field(name="balance", value="Zeigt dein Geld an", inline=False)
            embed_help.add_field(name="payday", value="Zahltag alle 6h", inline=False)

            await message.channel.send(embed=embed_help)

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


#====================================================================================================================================================================================================

    # Wenn mit :poop: reacted wird, wird es durch THATSCRINGE ersetzt
    async def on_raw_reaction_add(self, payload):
        if str(payload.emoji) == "💩": #emoji ändern zu sowas wie das cringe emoji
            user = client.get_user(payload.user_id)
            channel = client.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            await message.clear_reaction("💩")  #emoji ändern zu sowas wie das cringe emoji
            cringe = ["🇹", "🇭", "🇦", ":t2:849167204678631425", "🇸", "🇨", "🇷", "🇮", "🇳", "🇬", "🇪"]
            for i in cringe:
                await message.add_reaction(i)


client = MyClient()
with open("keys.json", "r") as f:
    keys = json.load(f)
client.run(keys["key"])
