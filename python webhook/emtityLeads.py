#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from refreg import recovery_token
from writejson import write_json
import json
from getContact import getContact

# скипт получения связанных сущностей и затем получение контакта


def getEmtityLead(entity_id):
    entity_id = entity_id

    with open('access_token.txt', 'r') as access:
        access_token = access.read()

    header = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/hal+json",
        "Content-Type": "application/json"
    }

    params = {
        'filter[to_entity_id]': '567605'
    }

    url = f'https://fortunaperm.amocrm.ru/api/v4/leads/{entity_id}/links'
    res = requests.get(url, headers=header)

    if res.status_code != 200:
        recovery_token()
        getEmtityLead(entity_id)
    else:
        result = res.json()
        # print(result)
        # write_json(result)
        id_contact = result['_embedded']['links'][0]['to_entity_id']
        contact_info = getContact(id_contact)

        return contact_info


# getEmtityLead('29228079')
