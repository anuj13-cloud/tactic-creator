from logic.rules_engine import suggest_tactic

if __name__ == "__main__":
    team_name = input("Enter the opponent team name: ")
    tactic = suggest_tactic(team_name)
    print(tactic)
