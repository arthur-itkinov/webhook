import requests
from refreg import recovery_token
from writejson import write_json


def getCompany(idCompany):
    id = idCompany
    company = dict.fromkeys(
        ['agreement', 'whatsapp', 'telegram'])

    with open('access_token.txt', 'r') as access:
        access_token = access.read()

    header = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/hal+json",
        "Content-Type": "application/json"
    }
    url = f'https://fortunaperm.amocrm.ru/api/v4/companies/{id}'
    res = requests.get(url, headers=header)
    if res.status_code != 200:
        recovery_token()
        getCompany(id)
    else:
        result = res.json()
        # print(result)
        # write_json(result)
        if result['custom_fields_values']:
            for contact in result['custom_fields_values']:
                if contact['field_id'] == 568437:
                    company['telegram'] = contact['values'][0]['value']
                elif contact['field_id'] == 568545:
                    company['whatsapp'] = contact['values'][0]['value']
                elif contact['field_id'] == 568687:
                    company['agreement'] = contact['values'][0]['value']

        return company


# getCompany('47226527')
