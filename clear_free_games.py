import json

games = []
with open("./games_with_revenue.json", encoding="utf-8", errors="ignore") as file:
    file_contents = file.read()
    games = json.loads(file_contents)

games_cleared = []
for game in games:
    if game["price"] == 0:
        continue

    games_cleared.append(game)

with open("./games_cleared.json", "w+") as file:
    file.write(json.dumps(games_cleared, indent=2))
