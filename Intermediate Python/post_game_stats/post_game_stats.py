# It can search for a team by id or name or it can search for a team randomly, then display it's most recent stats and players on the screen.
# The program ends when the user exits. It will allow the user to search N times for a team and display it's stats and players.
# It can also allow the user to edit the team's stats, like players. It will allow the user to add or remove players from the team's roster.
# It will retry the fetching of data three times if there was an error, then it'll show an error and ask the user if it should exit or not.

from prettytable import PrettyTable as pt
import sys as sy, random as rd, requests as rq



slugs = ("atlanta-falcons", "buffalo-bills", "chicago-bears", "cincinnati-bengals", "cleveland-browns", "dallas-cowboys", "denver-broncos", "detroit-lions", "green-bay-packers", "tennessee-titans", "indianapolis-colts", "kansas-city-chiefs", "las-vegas-raiders", "los-angeles-rams", "miami-dolphins", "minnesota-vikings", "new-england-patriots", "new-orleans-saints", "new-york-giants", "new-york-jets", "philadelphia-eagles", "arizona-cardinals", "pittsburgh-steelers", "los-angeles-chargers", "san-francisco-49ers", "seattle-seahawks", "tampa-bay-buccaneers", "washington-commanders", "carolina-panthers", "jacksonville-jaguars", "houston-texans", "baltimore-ravens" )


teams = (
    # AFC
    (
        # AFC North
        ("Baltimore Ravens", "Cincinnati Bengals", "Cleveland Browns", "Pittsburgh Steelers"),
        # AFC East
        ("Buffalo Bills", "Miami Dolphins", "New England Patriots", "New York Jets"),
        # AFC South
        ("Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Tennessee Titans"),
        # AFC West
        ("Denver Broncos", "Kansas City Chiefs", "Las Vegas Raiders", "Los Angeles Chargers")
    ),
    # NFC
    (
        # NFC North
        ("Chicago Bears", "Detroit Lions", "Green Bay Packers", "Minnesota Vikings"),
        # NFC East
        ("Dallas Cowboys", "New York Giants", "Philadelphia Eagles", "Washington Commanders"),
        # NFC South
        ("Atlanta Falcons", "Carolina Panthers", "New Orleans Saints", "Tampa Bay Buccaneers"),
        # NFC West
        ("Arizona Cardinals", "Los Angeles Rams", "San Francisco 49ers", "Seattle Seahawks")
    )
)


def view_menu(options):
    print("+{}+".format("-" * 90))
    print("\n+{:^90}+\n".format("Post-Game Stats Menu"))
    print("+{}+".format("-" * 90))

    for i in range(len(options)):
        print("+{:^90}+".format(f"{i + 1}. {options[i]}"))

    print("+{}+".format("-" * 90))

def get_team(team):
    data = rq.get(f'https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/{team}')
    data = data.json()

    file_name = f"{data['team']['displayName'].replace(' ', '_').lower()}.txt"

    with open(file_name, 'w') as file:
        file.write(str(data))

    return f"The data has been saved to '{file_name}' file."

def view_teams():
    view_menu(("AFC Divisions", "NFC Divisions", "Random Team Stats", "Back to Main Menu"))

    def show_afc():
        show_conf(0)
        return show_team()

    def show_nfc():
        show_conf(1)
        return show_team()

    def show_team():
        try:
            query = input('\nEnter the name of the team you want to view its status: ').replace(" ", "-").lower()

            assert [slug for slug in slugs if query in slug], 'The team name you entered is not valid. Try again.'
        except Exception as e:
            print(e)
        else:
            id = [index for index, slug in enumerate(slugs) if query in slug][0] + 1
            
            if "houston" in query or "texans" in query:
                id = 34
            elif "baltimore" in query or "ravens" in query:
                id = 33
           
            return get_team(id)
    def show_conf(conf):
        table = pt()

        for i in range(4):
            table.add_column(("North", "East", "South", "West")[i], teams[conf][i])

        print(table)

    def rnd_team():
        rnd_team = slugs.index(rd.choice(slugs)) + 1
        return get_team(rnd_team)

    opt = int(input('\nEnter an option: '))

    options = {
        1: show_afc,
        2: show_nfc,
        3: rnd_team,
        4: main
    }

    return options[opt]()

def exit_teams():
    print("+{}+".format("-" * 90))
    print("\n+{:^90}+\n".format("GOOD-BYE"))
    print("+{}+".format("-" * 90))

    sy.exit()

def main():
    view_menu(("View Team Stats", "Work In Progress", "Exit"))

    opt = int(input('\nEnter an option: '))

    options = {
        1: view_teams,
        #2: edit_teams,
        3: exit_teams
    }
    
    print(options[opt]())

if __name__ == '__main__':
    main()