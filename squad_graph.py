import json
import refresh_club_data
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

def setup_graph(G, squad_formation = '442', rating_min = 0, rating_max = 100, display_label = 'pos_nation_league', only_rare = False):
	formation = json.load(open('formation.json'))
	players = json.load(open('club_data.json'))
	for i in range(len(players)):
		p = players[i]
		if p['rating'] >= rating_min and p['rating'] < rating_max and p['position'] in formation[squad_formation] and (p['rare'] or not only_rare):
			G.add_node(p[display_label])
			for s in players[i+1:]:
				if s['rating'] >= rating_min and s['rating'] < rating_max and (s['rare'] or not only_rare):
					if s['position'] in formation[squad_formation][p['position']]:
						rarity[p[display_label]] = p['rare']
						rarity[s[display_label]] = s['rare']

						if p['country'] == s['country']:
							G.add_edge(p[display_label], s[display_label], {'color': 'orange'})
							if p['league'] == s['league']:
								G.add_edge(p[display_label], s[display_label], {'color': 'green'})

						if p['league'] == s['league']:
							G.add_edge(p[display_label], s[display_label], {'color': 'orange'})
							if p['team'] == s['team'] or p['country'] == s['country']:
								G.add_edge(p[display_label], s[display_label], {'color': 'green'})


def position_color(name):
	position_colors = {
		'GK':'brown',
		'LB':'orange',
		'CB':'orange',
		'RB':'orange',
		'LM':'green',
		'CM':'green',
		'RM':'green',
		'CAM':'green',
		'LW':'red',
		'RW':'red',
		'ST':'red'
	}
	return position_colors[name.split('|')[0]]

def display_graph(G, show_rare = False):
	edges = G.edges()
	colors = [G[u][v]['color'] for u,v in edges]
	if show_rare:
		node_colors = ['blue' if show_rare and rarity[node] > 0 else 'red' for node in G.nodes()]
	else:
		node_colors = [position_color(node) for node in G.nodes()]
	pos = graphviz_layout(G)
	nx.draw(G,pos,edges=edges, width=1.0, edge_color=colors, node_color=node_colors, with_labels=True)
	plt.show()

credentials = {}
with open('credentials.json') as json_data:
	credentials = json.load(json_data)
	json_data.close()
user_email = credentials["email"]
user_password = credentials["password"]
user_secret = credentials["secret"]
user_platform = credentials["platform"]

refresh_club_data.refresh_club_data(user_email, user_password, user_secret, platform=user_platform)
G = nx.Graph()
rarity = {}
setup_graph(
	G,
	squad_formation = '451',
	rating_min = 70,
	rating_max = 100,
	display_label = 'pos_nation_league', #pos_name_rating, pos_rating, pos_nation_league
	only_rare = False
)

loan_players = [
'LW|Fran|Icons|90',
'LM|Chil|ENG1|89',
'CB|Engl|Icons|88',
'CM|Spai|ENG1|86',
'CAM|Spai|ESP1|84',
'RM|Port|ENG1|84',
'CAM|Japa|GER1|83',
'GK|Spai|ESP1|81',
'CF|Mexi|MLS|79',
'ST|Unit|MLS|71']

for p in loan_players:
	if p in G.nodes():
		G.remove_node(p)

display_graph(
	G,
	show_rare = False
)
