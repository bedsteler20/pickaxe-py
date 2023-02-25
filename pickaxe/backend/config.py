import os
MS_CLIENT_ID = "@MS_CLIENT_ID@"
MS_REDIRECT_URL = "https://login.microsoftonline.com/common/oauth2/nativeclient"
MS_CLIENT_SECRET = "@MS_CLIENT_SECRET@"
DEVEL = os.environ.get("DEBUG_MODE") == "1"
