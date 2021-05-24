import os

import discord
from dotenv import load_dotenv
import random
import string
import re

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")


class DustyClient(discord.Client):
    async def on_ready(self):
        guild = discord.utils.get(self.guilds, name=GUILD)
        print(f'{self.user} has connected to 'f'{guild.name} (id: {guild.id}\n)')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
                f'Mrrrow welcome to tEp, {member.name}'
                )

    async def on_message(self, message):
        if message.author == self.user:
            return

        pet_head_quotes = ['Dusty rolls onto his back, inviting you to pet his belly.', 'Dusty purrs contently.', 'Dusty jumps onto your lap.', 'Dusty bunts your hand.', 'Dusty closes his eyes and purrs.', 'Dusty gets annoyed and struts away.', 'Dusty bites your hand.']
        good_food = ["kibble", "fish", "mayonnaise", "grilled_chees", "mayo", "anarchy"]
        food_quotes = ["Dusty eats contently.", "Dusty refuses your food."]

        message_lower = message.content.lower()

        if message_lower.startswith("dusty."):
            parsed = message_lower[6:]
            print(parsed)
            if parsed == "pet()": 
                response = random.choice(pet_head_quotes)
                await message.channel.send(response)
            elif parsed.startswith("feed(") and parsed.endswith(")"):
                food = re.sub("[^\w]", " ",parsed[5:-1]).split()
                print("food:", food)
                if not food[0]:
                    await message.channel.send("Dusty munches on the oxygen you offered.")
                    return
                for f in food:
                    if f not in good_food:
                        response = "Dusty does not like {} and barfs on the piano.".format(f)
                        await message.channel.send(response)
                        return
                response = random.choice(food_quotes)
                await message.channel.send(response)
            elif parsed == "giveDustyThreeExtraLegs()":
                await message.channel.send("Dusty writhes in pain...")
                await message.channel.send("His two back legs have sprouted legs, and another leg flaps limply from his forehead like a sail in the wind.")
                await message.channel.sned("The forehead leg flaps faster and faster until Dusty hovers above the ground. He proceeds to fly to Pyongyang to enjoy government-mandated blackouts.")


client = DustyClient()
client.run(TOKEN)
