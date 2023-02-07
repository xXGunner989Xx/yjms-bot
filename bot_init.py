import discord
from messaging import remove_user, add_user, get_users, update_moves, get_moves
import sys, getopt, asyncio
import sched, time
from api_hooks import get_player_stars

# ideas: 
# post daily stats in special channel each day
# only message users that haven't made a move yet (look at cfbrisk api)
#

TEST_MODE = True if sys.argv[1].lower() == "test" else False
TOKEN = sys.argv[2] if sys.argv[2] else None
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
guilds = []
roles = []

@client.event
async def on_ready():
    print(f'{client.user} is now running')
    guilds = [guilds async for guilds in client.fetch_guilds()]
    print(guilds)

@client.event
async def on_message(message: discord.Message):
    # if bot sends message, don't do anything
    if message.author == client.user:
        return

    # read move orders
    if (message.channel.name == "diplo-squad" 
        and len(message.attachments) != 0
        and message.attachments[0].url.endswith('csv')):
        user_roles = message.author.roles
        for role in user_roles:
            if role.name == "TECHnicians":
                print("hi")
                csv_contents = await(message.attachments[0].read())
                update_moves(csv_contents)

    if client.user in message.mentions:
        print("user add command")
        try:
            add_user(message.author, message.content)
            await(send_orders())
        except:
            await(message.reply("Please try again. Usage is <@mention username>"))
    
    if message.content.startswith("show"):
        out = get_player_stars(message.content.split()[1])
        await(message.reply(out))

async def send_orders():
    users = get_users()
    moves = get_moves()
    for user in users.keys():
        if user in moves.keys():
            await(users[user].send("This is the YJMS reminding you to please make your move " +
            "on " + moves[user]))


client.run(TOKEN)
