#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from refreg8250 import recovery_token

import json
from getContact8250 import getContact

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

   

    url = f'https://8250.amocrm.ru/api/v4/leads/{entity_id}/links'
    res = requests.get(url, headers=header)

    if res.status_code != 200:
        recovery_token()
        getEmtityLead(entity_id)
    else:
        result = res.json()
        # print(result)
        
        id_contact = result['_embedded']['links'][0]['to_entity_id']
        contact_info = getContact(id_contact)

        # return contact_info


# getEmtityLead('25624455')
