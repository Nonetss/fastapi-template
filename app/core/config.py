from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SSO_ISSUER = os.getenv("SSO_ISSUER")
SSO_INTROSPECT = f"{SSO_ISSUER}/oauth/v2/introspect"
SSO_AUDIENCE = os.getenv("SSO_AUDIENCE")
