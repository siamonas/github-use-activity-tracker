# GitHub User Activity Tracker

## Description
The GitHub User Activity Tracker is a Python-based tool designed to fetch and display the latest events for a specified GitHub user. It leverages the GitHub API to retrieve various types of user activities, such as commits, comments, and repository creations. The tool supports pagination and allows users to interactively load more events.

It is inspired from the [GitHub User Activity](https://roadmap.sh/projects/github-user-activity) project featured in the [Backend Roadmap](https://roadmap.sh/backend) from [roadmap.sh](https://roadmap.sh/).

## Features
- **Fetch Latest Events**: Retrieve the latest events for a specified GitHub user.
- **Event Details**: Display detailed information about different types of events.
- **Interactive Pagination**: Prompt the user to load more events or stop.
- **Environment Variable Support**: Load GitHub API tokens from a `.env` file for authenticated requests.

## Prerequisites
- Python 3.6+
- Git

## Installation
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/github-user-activity-tracker.git
   cd github-user-activity-tracker
2. Create and Activate a Virtual Environment
   ```sh
   python -m venv venv

   # On Windows:
   .\venv\Scripts\activate

   # On macOS and Linux:
   source venv/bin/activate
3. Install Dependencies
   ```sh
   pip install -r requirements.txt
5. Set Up Environment Variables **(optional)**
   - Create a `.env` file in the project root and add your GitHub token
  
## Usage
1. Run the application
   ```sh
   python github-activity username
2. Example
   ```sh
   python github-activity siamonas
