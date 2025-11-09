from flask import Flask
import json
import os

app = Flask(__name__)

# NOTE: All values below are fake examples for testing only
# Do NOT use real credentials in this file

# Single line secret patterns


if __name__ == "__main__":
    # Create the test file for Frogbot to scan, do not use real secrets
    success = write_frogbot_test_file()
    if success:
        print("frogbot-test.txt created with fake secret patterns")
    else:
        print("failed to create frogbot-test.txt, check permissions")

    app.run(host="0.0.0.0", port=5000)
