import requests
from bs4 import BeautifulSoup

url = 'https://www.forexfactory.com/calendar.php'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting event titles
events = soup.find_all('div', class_='calendar__event-title')
for event in events:
    print(event.get_text(strip=True))
