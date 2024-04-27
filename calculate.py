import matplotlib.pyplot as plt
import numpy as np
import math
import json

games = []
with open("./games_cleared.json", encoding="utf-8") as file:
    file_contents = file.read()
    games = json.loads(file_contents)

moda = lambda x: max(set(x), key=x.count)
media = lambda x: np.mean(x)
mediana = lambda x: np.median(x)
variancia_amostral = lambda x: np.var(x, ddof=1)
variancia_populacional = lambda x: np.var(x)
dp_amostral = lambda x: np.std(x, ddof=1)
dp_populacional = lambda x: np.std(x)
cv_amostral = lambda x: np.std(x, ddof=1) / np.mean(x) * 100
cv_populacional = lambda x: np.std(x) / np.mean(x) * 100

all_net_revenue = []
for game in games:
    all_net_revenue.append(game["netRevenue"])

games_minimo = min(all_net_revenue)
games_maximo = max(all_net_revenue)
games_moda = moda(all_net_revenue)
games_media = media(all_net_revenue)
games_mediana = mediana(all_net_revenue)
games_var_amostral = variancia_amostral(all_net_revenue)
games_var_populacional = variancia_populacional(all_net_revenue)
games_dp_amostral = dp_amostral(all_net_revenue)
games_dp_populacional = dp_populacional(all_net_revenue)
games_cv_amostral = cv_amostral(all_net_revenue)
games_cv_populacional = cv_populacional(all_net_revenue)

jogo_minimo = games[all_net_revenue.index(games_minimo)]
jogo_maximo = games[all_net_revenue.index(games_maximo)]

games.sort(key=lambda d: d["netRevenue"])
all_net_revenue.sort()

jogos_moda = []
for game in games:
    if game["netRevenue"] == games_moda:
        jogos_moda.append(game)

jogos_mediana = [
    games[math.floor(len(games) / 2) - 1],
    games[math.floor(len(games) / 2)],
]

last_biggest_games = all_net_revenue[-10:]
first_smallest_games = all_net_revenue[:10]

with open("./dados.json", "w+") as file:
    file_contents = json.dumps({
        "minimo": games_minimo,
        "maximo": games_maximo,
        "amplitude": games_maximo - games_minimo,
        "moda": games_moda,
        "media": games_media,
        "mediana": games_mediana,
        "varianciaAmostral": games_var_amostral,
        "varianciaPopulacional": games_var_populacional,
        "desvioPadraoAmostral": games_dp_amostral,
        "desvioPadraoPopulacional": games_dp_populacional,
        "coeficienteVariacaoAmostral": games_cv_amostral,
        "coeficienteVariacaoPopulacional": games_cv_populacional,
        "jogoDoMinimo": jogo_minimo,
        "jogoDoMaximo": jogo_maximo,
        "jogosModa": jogos_moda,
        "jogosMediana": jogos_mediana
    }, indent=2)
    file.write(file_contents)

top_10 = [i + 1 for i in range(10)]
top_10.reverse()

fig, ax = plt.subplots()
ax.bar(top_10, first_smallest_games)
plt.title("Top 10 jogos menos rentáveis (acima de 5000 avaliações)")
fig.savefig("menoresJogos.png")

fig, ax = plt.subplots()
ax.bar(top_10, last_biggest_games)
plt.title("Top 10 jogos mais rentáveis")
fig.savefig("maioresJogos.png")
