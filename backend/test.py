import requests
from bs4 import BeautifulSoup


def check_yesterdays_stats(team):
    url = f"https://www.baseball-reference.com/leagues/daily.fcgi?request=1&type=b&dates=lastndays&lastndays=1&since=2024-03-01&fromandto=2024-05-01.2024-05-31&level=mlb&franch={team}"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    data = dict()

    # # Name of Opposing Team
    data['opp_team'] = soup.find('td', attrs={'data-stat': 'opp_ID'}).text

    # Amount of Doubles Hit by the Rockies
    data['amount_of_doubles'] = sum(
        int(stat.text) for stat in soup.find_all('td', attrs={'data-stat': '2B'})
    )

    # Yesterdays Date
    data['yesterdays_date'] = soup.find(
        'td', attrs={'data-stat': 'date_game'}).text

    return data


print(check_yesterdays_stats('COL'))  # Check doubles
