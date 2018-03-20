import fut, json

def refresh_club_data(email,password,secret_answer,platform):
	session = fut.Core(email,password,secret_answer,platform = platform)
	club_data = session.club()
	leagues = session.leagues
	leagues_short = {}
	for k,v in json.load(open('leagues_short.json')).items():
		leagues_short[int(k)] = v
	teams = session.teams
	nations = session.nations
	players = session.players

	filter = ['assetId','leagueId','teamid','nation','position','rareflag']
	filtered = []
	for i in club_data:
		filtered.append({ key: i[key] for key in filter})

	clean_data = []
	for i in range(len(filtered)):
		position = filtered[i]['position']
		rating = players[filtered[i]['assetId']]['rating']
		last_name = players[filtered[i]['assetId']]['lastname']
		nation = nations[filtered[i]['nation']]
		league = leagues_short[filtered[i]['leagueId']]
		clean_data.append({
			'id':filtered[i]['assetId'],
			'pos_name_rating':position+'|'+last_name+'|'+str(rating),
			'pos_rating':position+'|'+str(rating),
			'pos_nation_league':position+'|'+nation[:4]+'|'+league+'|'+str(rating),
			'last_name':last_name,
			'rating':rating,
			'position':position,
			'league':league,
			'country':nation,
			'team':teams[filtered[i]['teamid']],
			'rare':filtered[i]['rareflag']
			})

	with open('club_data.json', 'w') as fp:
		json.dump(clean_data, fp)