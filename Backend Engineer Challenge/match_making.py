import csv


def get_servers():
    with open('servers.csv') as serversfile:
        return list(csv.reader(serversfile))[1:]


def get_players():
    with open('players.csv') as playersfile:
        return list(csv.reader(playersfile))[1:]


def get_players_ban():
    with open('players_ban.csv') as playersfile:
        return list(csv.reader(playersfile))[1:]


def get_servers_ban():
    with open('servers_ban.csv') as serversfile:
        return list(csv.reader(serversfile))[1:]


def get_same_region_players(player: list, region: str):
    region_players = []
    players = get_players()
    for current_player in players:
        if current_player[0] == region and player != current_player:
            region_players.append(current_player)
    return region_players


def get_different_region_players(player: list):
    region_players = []
    players = get_players()
    for current_player in players:
        if current_player[0] != player[0] and player != current_player:
            region_players.append(current_player)
    return region_players


def get_player_ban_list(player: list):
    ban_list = []
    bans = get_players_ban()
    for current_ban in bans:
        if player[1] in current_ban:
            if current_ban[0] == player[1]:
                ban_list.append(current_ban[1])
            else:
                ban_list.append(current_ban[0])
    return ban_list


def get_server_ban_list(server: list):
    ban_list = []
    bans = get_servers_ban()
    for current_ban in bans:
        if server[2] in current_ban:
            if current_ban[0] == server[2]:
                ban_list.append(current_ban[1])
    return ban_list


players = get_players()
servers = get_servers()
players_ban = get_players_ban()
servers_ban = get_servers_ban()

# for player in players:
#     player_ban_list = get_player_ban_list(player)
#     players_region_list = get_same_region_players(player)
#     if len(players_region_list) == 0:
