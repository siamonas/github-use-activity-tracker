import requests
from .events import print_event_details
from rich import print

def get_latest_events(username, page, events_per_page, token):
    url = f"https://api.github.com/users/{username}/events"
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    if token:
        headers["Authorization"] = f"token {token}"

    params = {
        "page": page,
        "per_page": events_per_page
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        events = response.json()

        number_of_events = len(events)
        if number_of_events == 0:
            print(f"No events found for user [bold red]{username}[/bold red].")
            return

        for event in events:
            print_event_details(event)

        if number_of_events == events_per_page:
            while True:
                user_input = input("Show more events? (y/n): ")
                if user_input.lower() == 'y':
                    get_latest_events(username, page + 1, events_per_page, token)
                    break
                elif user_input.lower() == 'n':
                    break
                else:
                    print("Invalid input. Please enter 'y' to continue or 'n' to stop.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching events - [bold red]{e}[/bold red]")