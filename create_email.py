import requests

payload = {
    "requestor": "YourNameAppName",
    "version": "1.0"
}
response = requests.post('https://api.nodemailer.com/user', json=payload)
if response.status_code == 200:
    account = response.json()
else:
    raise Exception(f'Could not crete Ethereal account: {response.text}')


