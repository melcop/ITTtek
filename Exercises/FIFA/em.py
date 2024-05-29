import random
from collections import defaultdict

teams = {
    "Gruppe A": ["Tyskland", "Skotland", "Ungarn", "Schweiz"],
    "Gruppe B": ["Spanien", "Italien", "Kroatien", "Albanien"],
    "Gruppe C": ["Slovenien", "Serbien", "Danmark", "England"],
    "Gruppe D": ["Polen", "Holland", "Østrig", "Frankrig"],
    "Gruppe E": ["Belgien", "Slovakiet", "Rumænien", "Ukraine"],
    "Gruppe F": ["Tyrkiet", "Georgien", "Portugal", "Tjekkiet"]
}

def play_match(team1, team2):
    result = random.choice([team1, team2, "Draw"])
    if result == "Draw":
        return (team1, 1), (team2, 1)
    else:
        return (result, 3), (team1 if result == team2 else team2, 0)

def play_group(group):
    points = defaultdict(int)
    matches = [(group[i], group[j]) for i in range(len(group)) for j in range(i+1, len(group))]
    for team1, team2 in matches:
        result1, result2 = play_match(team1, team2)
        points[result1[0]] += result1[1]
        points[result2[0]] += result2[1]
    sorted_teams = sorted(points.items(), key=lambda x: x[1], reverse=True)
    return sorted_teams[:2]

group_winners = []
for group_name, group_teams in teams.items():
    winners = play_group(group_teams)
    group_winners.extend([team for team, points in winners])

champion = random.choice(group_winners)

print("Vindere af hver gruppe:")
for group_name, group_teams in teams.items():
    winners = play_group(group_teams)
    print(f"{group_name}: {', '.join([team for team, points in winners])}")

print(group_winners)