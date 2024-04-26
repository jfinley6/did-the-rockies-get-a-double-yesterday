from datetime import date, timedelta
import requests
from bs4 import BeautifulSoup
from markupsafe import Markup
import sys

def get_yesterdays_date():
    yesterday = date.today() - timedelta(days=1)
    return yesterday

def check_html_response(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.content
        return html_content
    else:
        return ("Failed to Retrieve Rockies Results")

def scrape_rockies_stats(target_stat):
    url = f'https://www.baseball-reference.com/teams/tgl.cgi?team=COL&t=b&year={get_yesterdays_date().year}'
    
    html_content = check_html_response(url)

    if html_content:
        # Locate the div element by ID
        soup = BeautifulSoup(html_content, 'html.parser')
        div_id = 'div_team_batting_gamelogs'
        div = soup.find('div', id=div_id)

        if div:
            # Find the first tbody element inside the div (assuming there's only one)
            tbody = div.find('tbody')

            if tbody:
                # Find all tr elements within the tbody
                rows = tbody.find_all('tr')

                if rows:
                    # Access the last tr element (using negative index) to get
                    # the most game
                    last_row = rows[-1]

                    # Get the text of the targeted stat
                    stat_text = last_row.find(
                        'td', attrs={'data-stat': target_stat}
                    )

                    return stat_text.get_text()
                        
def is_double_yesterday():
    #Check to see if Rockies played yesterday
    if scrape_rockies_stats('date_game') != get_yesterdays_date().strftime('%b %d'):
        double = {
            "answer": "NO",
            "details": "The Rockies Did Not Play Yesterday"
        }
        return double
    
    #Check if Number of Doubles is Greater Than 0
    if int(scrape_rockies_stats('2B')) > 0:
        link = "https://www.milehighonthecheap.com/rockies-special-deal-free-chicken-nuggets-mcdonalds-denver/"
        double = {
            "answer": "YES",
            "details": "The Rockies Got a Double Yesterday!",
            "moreDetails": Markup(f"That means people in Colorado can score a free double cheeseburger \
                            today at McDonalds. Details about this promotion can be found \
                            <a target='_blank' href={link}>here.</a>")
        }
    else:
        link = "https://www.milehighonthecheap.com/rockies-special-deal-free-chicken-nuggets-mcdonalds-denver/" 
        double = {
            "answer": "NO",
            "details": "The Rockies Did Not Get a Double Yesterday...",
            "moreDetails": "lol"
        }
    return double