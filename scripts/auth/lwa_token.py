"""LWA token helper (stub).

Replace with real LWA token retrieval.
Store secrets in env vars:
- AMAZON_LWA_CLIENT_ID
- AMAZON_LWA_CLIENT_SECRET
- AMAZON_LWA_REFRESH_TOKEN
"""

import os
import requests

def get_access_token() -> str:
    raise NotImplementedError("Implement LWA token retrieval (client_id/secret + refresh_token).")
