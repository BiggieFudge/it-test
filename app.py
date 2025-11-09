from flask import Flask

app = Flask(__name__)

AWS_ACCESS_KEY_ID = "AKIAEXAMP1EACCESSKEY"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
GITHUB_TOKEN = "ghp_0123456789EXAMPLETOKENforTesting"
SLACK_BOT_TOKEN = "xoxb-123456789012-EXAMPLETOKEN-abcdef"
API_KEY = "AIzaSyEXAMPLEGOOGLEAPIOKEYforTesting"


@app.route("/")
def home():
    return "Hello, World! This is a vulnerable app."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
