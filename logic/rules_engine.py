import json

def suggest_tactic(team_name):
    data = json.load(open('data/teams.json'))
    if team_name in data:
        team = data[team_name]
        weakness = team['weaknesses']
        tactics = []
        for w in weakness:
            
            if "counter" in w:
                tactics.append("Use fast counter attacks after absorbing pressure.") 
            if "deep block" in w:
                tactics.append("Sit deep in a compact shape and frustrate their attackers.")
            if "spaces behind" in w or "wide overloads" in w:
                tactics.append("Exploit the wings with fast wide players.")
            
        # Step 6: Default tactic if no weakness matched
        if tactics:
            return "Recommended Tactics:\n" + "\n".join(tactics)
        else:
            return "Play a balanced game and wait for mistakes."
    else:
        return "Not Found" 
    
    