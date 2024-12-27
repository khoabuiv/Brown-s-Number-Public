import requests
from bs4 import BeautifulSoup
import re
from nordvpn_switcher import initialize_VPN,rotate_VPN,terminate_VPN
        
def get_page_contents(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    page = requests.get(url, headers=headers)

    if page.status_code == 200:
        return page.text

    return None

def getRawData(page_contents):
    try:
        soup = BeautifulSoup(page_contents, features="lxml")
        partial_summary = soup.find("div", {"data-template": "Partials/Teams/Summary"})
        output = partial_summary.find_all("a", {"href": re.compile(r"^/coaches/.*")})
        parent = []
        for i in output:
            parent.append(i.parent.get_text())

        parent = set(parent)
        return parent

    except TypeError:
        return None

file = open("teams.csv", "r")
f = open("preclean_data.txt", "a")
f.write("Team,Year,Data\n")

range_servers = range(0,1000)
server_list = ["nl"+str(number) for number in range_servers]
instructions = initialize_VPN(area_input = server_list)
rotate_VPN(instructions)

for line in file:
    List = line.strip().split(',')
    for i in range(int(List[1]),int(List[2])):
        url = 'https://www.pro-football-reference.com/teams/{team}/{year}.htm'.format(team=List[0], year=i)
        print(url)
        page_contents = get_page_contents(url)
        if page_contents is not None:
            rawData = getRawData(page_contents)
            f.write("{team},{year},{data}\n".format(team=List[0], year=i,data=rawData))
            print("{team},{year},{data}\n".format(team=List[0], year=i,data=rawData))
        if page_contents is None:
            rotate_VPN(instructions)
            
terminate_VPN(instructions)
f.close()
file.close()
