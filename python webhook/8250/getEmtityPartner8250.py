import requests
from refreg8250 import recovery_token

from getInfoStatus8250 import getInfoStatus
from emtityLeads8250 import getEmtityLead
from getCompany8250 import getCompany

# скрипт поиска лида в воронке привлечение


def getPartner(idPartner):
    id = idPartner
    company = {}

    with open('../access_token.txt', 'r') as access:
        access_token = access.read()

    header = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/hal+json",
        "Content-Type": "application/json"
    }

    params = {
        'with': 'catalog_elements'
    }

    url = f'https://fortunaperm.amocrm.ru/api/v4/leads/{id}/links'
    res = requests.get(url, headers=header, params=params)
  
    if res.status_code == 200:
        result = res.json()
        # print(result)
        # write_json(result)
        for link in result['_embedded']['links']:
            if link['to_entity_type'] == 'companies':
                company = getCompany(link['to_entity_id'])
        return company


# getPartner('29228397')
