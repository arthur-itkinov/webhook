import requests


def recovery_token():

    client_id = "69439ee6-8449-45e6-b299-c6b5a0520d25"
    client_secret = "EpoJ6fERvthiaHpqY8GSqcYeWz0YwmucvZ9EE5mtkqBjlN8p6WkLPZPqnzcNqjTi"
    subdomain = "fortunaperm"
    redirect_url = "https://aktivkredit.ru/"
    with open('./refresh_token.txt', 'r') as access:
        refresh_token = access.read()
        access.close()
    url = f'https://fortunaperm.amocrm.ru/oauth2/access_token'
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "redirect_uri": redirect_url
    }
    header = {
        "Content-Type": "application/json",
    }

    res = requests.post(url, headers=header, json=params)
    token = res.json()
    with open("./access_token.txt", "w") as file:
        file.write(token['access_token'])
    with open("./refresh_token.txt", "w") as file:
        file.write(token['refresh_token'])
# recovery_token()