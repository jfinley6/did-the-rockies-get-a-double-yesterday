from datetime import date, timedelta, datetime
import requests
from bs4 import BeautifulSoup
from markupsafe import Markup
import sys
import pytz
import time

def get_yesterdays_date():
    tz = pytz.timezone('America/Denver')
    now = datetime.now(tz)
    yesterday = now - timedelta(days=1)
    return yesterday

# get_yesterdays_date() returns a leading zero if the day is less than 10, e.g. May 01
# so I made this method so that strips the zero so it can be 
# compared with the Rockies date from scrape_rockies_stats('date_game') which returns May 1
def strip_leading_zero_from_day(date_str):
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

# Returns month and day as a string
def format_date(date_string):
    date_object = datetime.strptime(date_string, "%A, %B %d")
    formatted_date = date_object.strftime('%B %d')

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


def scrape_rockies_stats():
    url = f'https://www.baseball-reference.com/teams/tgl.cgi?team=COL&t=b&year={get_yesterdays_date().year}'
    page = requests.get(url)

    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'lxml')
        row = soup.select_one('#div_team_batting_gamelogs tbody tr:last-of-type')
        if row:
            data = {
                'opp_team': row.find('td', {'data-stat': 'opp_ID'}).text,
                'amount_of_doubles': int(row.find('td', {'data-stat': '2B'}).text),
                'yesterdays_game_date': row.find('td', {'data-stat': 'date_game'}).text
            }
            return data


def get_next_game_data():
    url = f'https://www.baseball-reference.com/teams/COL/{get_yesterdays_date().year}-schedule-scores.shtml'
    page = requests.get(url)

    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'lxml')
        # This row will be the first game with a preview section since it hasn't happened yet
        next_game_row = soup.find('td', {'data-stat': 'preview'}).parent
        next_game_data = {
            'date': next_game_row.find('td', {'data-stat': 'date_game'}).get_text(),
            'opponent': next_game_row.find('td', {'data-stat': 'opp_ID'}).get_text()
        }

    return next_game_data

# 'yesterdays_game_date' scrapped from scrape_rockies_data() comes back in 3 letter variants
# so this method returns the full team name
def get_full_team_name(shortened_name):
    baseball_teams = {
        "ARI": "Arizona Diamondbacks",
        "ATL": "Atlanta Braves",
        "BAL": "Baltimore Orioles",
        "BOS": "Boston Red Sox",
        "CHC": "Chicago Cubs",
        "CHW": "Chicago White Sox",
        "CLE": "Cleveland Guardians",
        "DET": "Detroit Tigers",
        "HOU": "Houston Astros",
        "KCR": "Kansas City Royals",
        "ANA": "Los Angeles Angels",
        "LAD": "Los Angeles Dodgers",
        "FLA": "Miami Marlins",
        "MIL": "Milwaukee Brewers",
        "MIN": "Minnesota Twins",
        "NYM": "New York Mets",
        "NYY": "New York Yankees",
        "OAK": "Oakland Athletics",
        "PHI": "Philadelphia Phillies",
        "PIT": "Pittsburgh Pirates",
        "SDP": "San Diego Padres",
        "SFG": "San Francisco Giants",
        "SEA": "Seattle Mariners",
        "STL": "St. Louis Cardinals",
        "TBD": "Tampa Bay Rays",
        "TEX": "Texas Rangers",
        "TOR": "Toronto Blue Jays",
        "WSN": "Washington Nationals"
    }
    return baseball_teams[shortened_name]


def is_double_yesterday():
    # Promotion Link
    link = "https://www.milehighonthecheap.com/rockies-special-deal-free-chicken-nuggets-mcdonalds-denver/"
    yesterdays_date = strip_leading_zero_from_day(get_yesterdays_date())
    rockie_data = scrape_rockies_stats()

    # Check to see if Rockies played yesterday
    if rockie_data['yesterdays_game_date'] != yesterdays_date:
        next_game_data = get_next_game_data()
        next_rockies_game_date = format_date(next_game_data['date'])
        day_after_next_game = get_day_after_next_game(next_rockies_game_date)
        next_opposing_team = get_full_team_name(next_game_data['opponent'])

        double = {
            "answer": "NO",
            "details": "The Rockies Didn't Play Yesterday...",
            "moreDetails": Markup(f"The Rockies play again on {add_ordinal_suffix(next_rockies_game_date)} \
                            against the {next_opposing_team}. Check back here on {add_ordinal_suffix(day_after_next_game)} \
                            to see if the Rockies got a double for the \
                            <a target='_blank' href={link}>McDonald's Promotion</a>."),
            "yesterdays_date": yesterdays_date,
            "last_rockie_game_date": rockie_data['yesterdays_game_date']
        }
        return double

    # Check if Number of Doubles is Greater Than 0
    if rockie_data['amount_of_doubles'] > 0:
        double = {
            "answer": "YES",
            "details": f"The Rockies Got a Double Yesterday against the {get_full_team_name(rockie_data['opp_team'])}!",
            "moreDetails": Markup(f"That means people in Colorado can score a double cheeseburger \
                            today at McDonald's for 1$. Details about this promotion can be found \
                            <a target='_blank' href={link}>here.</a>"),
            "yesterdays_date": yesterdays_date,
            "last_rockie_game_date": rockie_data['yesterdays_game_date']
        }
    else:
        double = {
            "answer": "NO",
            "details": f"The Rockies Did Not Get a Double Yesterday against the {get_full_team_name(rockie_data['opp_team'])}...",
            "moreDetails": Markup("That means no 1$ double cheeseburger from McDonald's today. \
                                  Details about this promotion can be found \
                                <a target='_blank' href={link}>here.</a> "),
            "yesterdays_date": yesterdays_date,
            "last_rockie_game_date": rockie_data['yesterdays_game_date']
        }
    return double
