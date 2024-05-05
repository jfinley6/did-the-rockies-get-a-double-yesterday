from datetime import date, timedelta, datetime
import requests
from bs4 import BeautifulSoup
from markupsafe import Markup
import sys


def get_yesterdays_date():
    yesterday = date.today() - timedelta(days=1)
    return yesterday

# get_yesterdays_date() returns a leading zero if the day is less than 10, e.g. May 01
# so I made this method so that strips the zero so it can be 
# compared with the Rockies date from scrape_rockies_stats('date_game') which returns May 1
def strip_leading_zero_from_day(date_str):
    print(date_str, file=sys.stdout)
    formatted_yesterday = date_str.strftime('%b %d')

    month, day = formatted_yesterday.split()
    if day.startswith("0") and len(day) > 1:
        day = day[1:]
    
    formatted_date = f"{month} {day}"

    return formatted_date

def get_day_after_next_game(game_date):
    input_date = datetime.strptime(game_date, '%b %d')
    # Add one day to the date
    next_day = input_date + timedelta(days=1)

    # Convert the result back to the desired string format
    next_day_str = next_day.strftime('%b %d')
    return next_day_str


def get_next_rockies_game_date():
    next_game_day_str = format_date(get_next_game_data()['date'])
    return next_game_day_str

# Returns month and day as a string


def format_date(date_string):
    date_object = datetime.strptime(date_string, '%b %d, %Y')
    formatted_date = date_object.strftime('%b %d')

    return formatted_date


def add_ordinal_suffix(date_str):
    # Define a dictionary to map month abbreviations to their full names
    month_names = {
        'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Apr': 'April',
        'May': 'May', 'Jun': 'June', 'Jul': 'July', 'Aug': 'August',
        'Sep': 'September', 'Oct': 'October', 'Nov': 'November', 'Dec': 'December'
    }

    # Split the input string into month and day
    month_abbr, day_str = date_str.split()

    # Convert day string to integer
    day = int(day_str)

    # Determine the ordinal suffix based on the day
    if 10 <= day % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')

    # Format the result
    result = f"{month_names[month_abbr]} {day}{suffix}"

    return result


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


def get_next_game_data():
    url = f'https://www.baseball-reference.com/teams/COL/{date.today().year}.shtml'

    html_content = check_html_response(url)

    next_game_data = {}

    if html_content:
        # Locate the div element by ID
        soup = BeautifulSoup(html_content, 'html.parser')
        target_class = 'teams'
        target_game = soup.find('table', class_=target_class)

        # Retrieve the date from the next game
        if target_game:
            date_row = target_game.find('tr', class_='date')
            innermost_element = date_row
            while innermost_element.find():
                innermost_element = innermost_element.find()
            next_game_date = innermost_element.get_text()
            next_game_data["date"] = next_game_date

        if target_game:
            team_rows = target_game.find_all('tr', class_='')
            for row in team_rows:
                innermost_element = row
                while innermost_element.find():
                    innermost_element = innermost_element.find()
                    if innermost_element.get_text() != 'Colorado Rockies':
                        next_game_data["opponent"] = innermost_element.get_text()

                # print(innermost_element.get_text(), file=sys.stdout)


    return next_game_data


def is_double_yesterday():
    # Promotion Link
    link = "https://www.milehighonthecheap.com/rockies-special-deal-free-chicken-nuggets-mcdonalds-denver/"
    yesterdays_date = strip_leading_zero_from_day(get_yesterdays_date())
    last_rockie_game_date = scrape_rockies_stats('date_game')

    # Check to see if Rockies played yesterday
    if last_rockie_game_date != yesterdays_date:
        next_rockies_game_date = get_next_rockies_game_date()
        day_after_next_game = get_day_after_next_game(next_rockies_game_date)
        opposing_team = get_next_game_data()['opponent']
        

        double = {
            "answer": "NO",
            "details": "The Rockies Didn't Play Yesterday...",
            "moreDetails": Markup(f"The Rockies play again on {add_ordinal_suffix(next_rockies_game_date)} \
                            against the {opposing_team}. Check back here on {add_ordinal_suffix(day_after_next_game)} \
                            to see if the Rockies got a double for the \
                            <a target='_blank' href={link}>McDonald's Promotion</a>.")
        }
        return double


    # Check if Number of Doubles is Greater Than 0
    if int(scrape_rockies_stats('2B')) > 0:
        double = {
            "answer": "YES",
            "details": "The Rockies Got a Double Yesterday!",
            "moreDetails": Markup(f"That means people in Colorado can score a free double cheeseburger \
                            today at McDonald's. Details about this promotion can be found \
                            <a target='_blank' href={link}>here.</a>")
        }
    else:
        double = {
            "answer": "NO",
            "details": "The Rockies Did Not Get a Double Yesterday...",
            "moreDetails": Markup("That means no free double cheeseburger from McDonald's today. \
                                  Details about this promotion can be found \
                                <a target='_blank' href={link}>here.</a> ")
        }
    return double
