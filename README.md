## FIFA Ultimate Team Grapher

### Background Info

The best squads in fifa ultimate team are the ones with the highest overall ratings of players and highest chemistry between each player. Chemistry between players depends on the following similarities:

1. Same Club
2. Same League
3. Same Nationality

If one attribute is similar there is a orange link, if there are two similar attributes then there is a green link. The more green and orange links are there, the higher chemistry the fifa ultimate team has.

![Fifa 18 Ultimate Team](/screenshots/fifa18_UT.jpg)

### Problem

Therefore, it is in the player's interest to form a team with the best overalls and the best chemistry. However it becomes really tedious to find such a squad from the long list of random players.

### Solution

I turned this into a graph problem to find the best squads by using players as nodes and edges as similarities.

Make a credentials.json with the FUT details:
`{
"email": "",
"password": "",
"secret": "",
"platform": ""
}``

Run `python squad_graph.py`

![Squad suggestions](/screenshots/squad_suggestions.png)

### Legend

Brown node: Goalkeeper
Yellow node: Defender
Green node: Midfielder
Red node: Attacker

Orange edge: Orange Chemistry Link
Green edge: Green Chemistry Link
