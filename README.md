# Trabalho do Jaisson

## Pré-requisitos

- Node 18+
- Python

## Como funciona

O Python e o Node ficam se trocando informações através dos JSON, cada JSON na pasta possui uma informação específica.

- `games.json`: Informações dos jogos;
- `games_with_revenue.json`: Informações de quanto os jogos ganharam;
- `games_cleared.json`: JSON sem os jogos de graça;
- `dados.json`: Nosso JSON final, ele possui os dados calculados.

## Como executar

Você deve seguir os seguintes passos para chegar no JSON final:

1. Execute o script getGames através do comando `node getGames.js`, isso nos dará o games.json.
1. Execute o script getGamesRevenue através do comando `node getGamesRevenue.js`, isso nos dará os jogos com os valores gerados por eles.
1. Execute o script clear_free_games através do comando `python clear_free_games.py`, isso tirará os jogos grátis que estão na base de dados.
1. Execute o script calculate através do comando `python calculate.py`, isso gerará o JSON com os dados finais (`dados.json`).