import sys
from github_events.api import get_latest_events
from github_events.utils import get_token
from rich import print

EVENTS_PER_PAGE = 30

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
        token = get_token()
        current_page = 1  # Initialize the current page
        print(f"Latest events for [bold green]{username}[/bold green]:")
        get_latest_events(username, current_page, EVENTS_PER_PAGE, token)
    else:
        print("Please provide a valid GitHub username as an argument.")