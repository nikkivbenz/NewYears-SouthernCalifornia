import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage you want to scrape
url = 'https://example.com/new-years-events-2023'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Search for information about New Year's events
    events = []

    # Replace 'event_info' and 'event_date' with the appropriate HTML elements or classes
    event_info_elements = soup.find_all(class_='event_info')
    event_date_elements = soup.find_all(class_='event_date')

    for info, date in zip(event_info_elements, event_date_elements):
        event = {
            'event_info': info.text.strip(),
            'event_date': date.text.strip()
        }
        events.append(event)

    # Print the list of events found
    for event in events:
        print(event)
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
