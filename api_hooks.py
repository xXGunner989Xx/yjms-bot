import requests

def get_player_stars(player: str):
    response = requests.get("https://collegefootballrisk.com/api/player?player="+player)
    if not response:
        return "user not found"
    response = response.json()
    stars = response["ratings"]["overall"]
    total_turns = response["ratings"]["totalTurns"]
    round_turns = response["ratings"]["gameTurns"]
    mvps = response["ratings"]["mvps"]
    streak = response["ratings"]["streak"]
    return {
        "stars": stars,
        "total_turns": total_turns,
        "round_turns": round_turns,
        "mvps": mvps,
        "streak": streak
    }
    