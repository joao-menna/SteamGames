import json

games = []
with open("./games_with_revenue.json", encoding="utf-8", errors="ignore") as file:
    file_contents = file.read()
    games = json.loads(file_contents)

for game in games:
    if game["price"] != 0:
        continue

    games.remove(game)

with open("./games_cleared.json", "w+") as file:
    file.write(json.dumps(games, indent=2))
