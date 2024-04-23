import numpy as np
import json

games = []
with open("./games_cleared.json", encoding="utf-8") as file:
    file_contents = file.read()
    games = json.loads(file_contents)

media = lambda x: np.mean(x)
mediana = lambda x: np.median(x)
dp_amostral = lambda x: np.std(x, ddof=1)
dp_populacional = lambda x: np.std(x, ddof=1)
cv_amostral = lambda x: np.std(x, ddof=1) / np.mean(x) * 100
cv_populacional = lambda x: np.std(x) / np.mean(x) * 100

all_net_revenue = []
for game in games:
    all_net_revenue.append(game["netRevenue"])

games_minimo = min(all_net_revenue)
games_maximo = max(all_net_revenue)
games_media = media(all_net_revenue)
games_mediana = mediana(all_net_revenue)
games_dp_amostral = dp_amostral(all_net_revenue)
games_dp_populacional = dp_populacional(all_net_revenue)
games_cv_amostral = cv_amostral(all_net_revenue)
games_cv_populacional = cv_populacional(all_net_revenue)

with open("./dados.json", "w+") as file:
    file_contents = json.dumps({
        "minimo": games_minimo,
        "maximo": games_maximo,
        "amplitude": games_maximo - games_minimo,
        "media": games_media,
        "mediana": games_mediana,
        "desvioPadraoAmostral": games_dp_amostral,
        "desvioPadraoPopulacional": games_dp_populacional,
        "coeficienteVariacaoAmostral": games_cv_amostral,
        "coeficienteVariacaoPopulacional": games_cv_populacional
    }, indent=2)
    file.write(file_contents)