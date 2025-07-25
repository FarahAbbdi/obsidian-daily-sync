import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Define required Google API scopes for Calendar and Sheets
SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/spreadsheets",
]

def get_credentials():
    """
    Authenticate the user with Google APIs (Calendar & Sheets) and return credentials.

    - Checks for existing credentials in 'token.json'.
    - Refreshes token if expired.
    - Initiates OAuth flow if no valid credentials are found.
    - Saves new credentials in 'token.json' for future use.

    Returns:
        Credentials: An authorized Google API credentials object.
    """
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds