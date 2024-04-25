from datetime import date, timedelta

def get_yesterdays_date():
    yesterday = date.today() - timedelta(days=1)
    return yesterday.strftime('%b %d')