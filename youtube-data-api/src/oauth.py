import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

flow = InstalledAppFlow.from_client_secrets_file(
    os.path.join(os.path.dirname(__file__), "../client_secrets.json"),
    scopes=[
        "openid",
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
    ],
)

flow.run_local_server()
credentials = flow.credentials

service = build("calendar", "v3", credentials=credentials)

# Optionally, view the email address of the authenticated user.
user_info_service = build("oauth2", "v2", credentials=credentials)
user_info = user_info_service.userinfo().get().execute()
print(user_info["email"])
