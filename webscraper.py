from bs4 import BeautifulSoup
import requests

url_link = 'https://www.skysports.com/premier-league-table'
response = requests.get(url_link)
soup = BeautifulSoup(response.text, 'html.parser')
league_table = soup.find('table', class_ = 'standing-table__table')

for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    
    for row in rows:
        league_team = row.find('td', class_ ='standing-table__cell standing-table__cell--name').text.strip()
        league_points = row.find_all('td', class_ = 'standing-table__cell')[9].text
        league_gd = row.find_all('td', class_ = 'standing-table__cell')[8].text
        
        # print team name, league points, goal difference
        print(league_team, league_points, league_gd)