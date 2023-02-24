import discord
from api_hooks import get_player_stars
class Player:
    def __init__(self, discord_name: discord.User, reddit_name: str):
        self.discord_name = discord_name
        self.reddit_name = reddit_name
        self.stats = self.init_stats()
        self.latest_move = ""
    
    def init_stats(self):
        return get_player_stars(self.reddit_name)

    def set_latest_move(self, move: str):
        self.latest_move = move
    
    def get_latest_move(self) -> str:
        return self.latest_move

    def get_discord_name(self) -> discord.User:
        return self.discord_name

    def get_reddit_name(self) -> str:
        return self.reddit_name

    def get_stats(self) -> dict:
        return self.stats

    def serialize(self) -> dict:
        json_dict = {
            "id": self.discord_name.id,
            "reddit_name": self.reddit_name,
            "stats": self.stats,
            "latest_move": self.latest_move
        }
        print(json_dict)
        return json_dict

# deserialize a json dict from file into a player class
async def deserialize(client: discord.Client, player_data: dict):
    return Player(
        await(client.fetch_user(player_data["id"])),
        player_data["reddit_name"],
        player_data["stats"],
        player_data["latest_move"],
    )