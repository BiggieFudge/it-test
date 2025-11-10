from flask import Flask
import json
import os

app = Flask(__name__)
AWS_ACCESS_KEY_ID = "AKIAEXAMP1EACCESSKEY"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
GITHUB_TOKEN = "ghp_0123456789EXAMPLETOKENforTesting"
SLACK_BOT_TOKEN = "xoxb-123456789012-EXAMPLETOKEN-abcdef"
API_KEY = "AIzaSyEXAMPLEGOOGLEAPIOKEYforTesting"

# Multi line private key example to test key block detectors
FAKE_RSA_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIFakeKeyEXAMPLE1234567890abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+/=
-----END RSA PRIVATE KEY-----"""

# Example Google service account JSON snippet, fake values only
GOOGLE_SA_JSON = {
    "type": "service_account",
    "project_id": "example-project-123",
    "private_key_id": "0123456789abcdefEXAMPLEKEYID",
    "private_key": FAKE_RSA_PRIVATE_KEY,
    "client_email": "example-sa@example-project-123.iam.gserviceaccount.com",
    "client_id": "12345678901234567890",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token"
}

def write_frogbot_test_file():
    """
    Writes a helper file that contains the example secret patterns.
    Some scanners inspect non-source files as well, so this improves coverage.
    """
    payload = []
    payload.append(f"AWS_ACCESS_KEY_ID={AWS_ACCESS_KEY_ID}")
    payload.append(f"AWS_SECRET_ACCESS_KEY={AWS_SECRET_ACCESS_KEY}")
    payload.append(f"GITHUB_TOKEN={GITHUB_TOKEN}")
    payload.append(f"SLACK_BOT_TOKEN={SLACK_BOT_TOKEN}")
    payload.append(f"API_KEY={API_KEY}")
    payload.append("")
    payload.append("==== FAKE RSA PRIVATE KEY ====")
    payload.append(FAKE_RSA_PRIVATE_KEY)
    payload.append("")
    payload.append("==== GOOGLE SERVICE ACCOUNT JSON ====")
    payload.append(json.dumps(GOOGLE_SA_JSON, indent=2))
    content = "\n".join(payload)

    try:
        with open("frogbot-test.txt", "w", encoding="utf-8") as f:
            f.write(content)
        # Restrict file permissions where supported
        try:
            os.chmod("frogbot-test.txt", 0o600)
        except Exception:
            pass
        return True
    except Exception:
        return False

@app.route("/")
def home():
    return "Hello, World! This is a vulnerable app."# Do NOT use real credentials in this file

# Single line secret patterns
AWS_ACCESS_KEY_ID = "AKIAEXAMP1EACCESSKEY"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
GITHUB_TOKEN = "ghp_0123456789EXAMPLETOKENforTesting"
SLACK_BOT_TOKEN = "xoxb-123456789012-EXAMPLETOKEN-abcdef"
API_KEY = "AIzaSyEXAMPLEGOOGLEAPIOKEYforTesting"

# Multi line private key example to test key block detectors
FAKE_RSA_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIFakeKeyEXAMPLE1234567890abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+/=
-----END RSA PRIVATE KEY-----"""

# Example Google service account JSON snippet, fake values only
GOOGLE_SA_JSON = {
    "type": "service_account",
    "project_id": "example-project-123",
    "private_key_id": "0123456789abcdefEXAMPLEKEYID",
    "private_key": FAKE_RSA_PRIVATE_KEY,
    "client_email": "example-sa@example-project-123.iam.gserviceaccount.com",
    "client_id": "12345678901234567890",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token"
}

def write_frogbot_test_file():
    """
    Writes a helper file that contains the example secret patterns.
    Some scanners inspect non-source files as well, so this improves coverage.
    """
    payload = []
    payload.append(f"AWS_ACCESS_KEY_ID={AWS_ACCESS_KEY_ID}")
    payload.append(f"AWS_SECRET_ACCESS_KEY={AWS_SECRET_ACCESS_KEY}")
    payload.append(f"GITHUB_TOKEN={GITHUB_TOKEN}")
    payload.append(f"SLACK_BOT_TOKEN={SLACK_BOT_TOKEN}")
    payload.append(f"API_KEY={API_KEY}")
    payload.append("")
    payload.append("==== FAKE RSA PRIVATE KEY ====")
    payload.append(FAKE_RSA_PRIVATE_KEY)
    payload.append("")
    payload.append("==== GOOGLE SERVICE ACCOUNT JSON ====")
    payload.append(json.dumps(GOOGLE_SA_JSON, indent=2))
    content = "\n".join(payload)

    try:
        with open("frogbot-test.txt", "w", encoding="utf-8") as f:
            f.write(content)
        # Restrict file permissions where supported
        try:
            os.chmod("frogbot-test.txt", 0o600)
        except Exception:
            pass
        return True
    except Exception:
        return False

@app.route("/")
def home():
    return "Hello, World! This is a vulnerable app."
# NOTE: All values below are fake examples for testing only


if __name__ == "__main__":
    # Create the test file for Frogbot to scan, do not use real secrets
    success = write_frogbot_test_file()
    if success:
        print("frogbot-test.txt created with fake secret patterns")
    else:
        print("failed to create frogbot-test.txt, check permissions")

    app.run(host="0.0.0.0", port=5000)
