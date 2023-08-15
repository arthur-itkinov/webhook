#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from refreg import recovery_token
from writejson import write_json
import json
from getInfoStatus import getInfoStatus


def getContact(idContact):
    id = idContact
    contact = dict.fromkeys(['name', 'phone', 'email'])
    contact['name'] = 'Нет имени'
    contact['phone'] = 'Телефона нет'
    contact['email'] = 'email не указан'
    with open('access_token.txt', 'r') as access:
        access_token = access.read()

    header = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/hal+json",
        "Content-Type": "application/json"
    }

    url = f'https://fortunaperm.amocrm.ru/api/v4/contacts/{id}'
    res = requests.get(url, headers=header)
    if res.status_code != 200:
        recovery_token()
        getContact(id)
    else:
        result = res.json()
        # print('контакт', result)
        # write_json(result)
        contact['name'] = result['name']
        for field in result['custom_fields_values']:
            if field['field_id'] == 5759:
                contact['phone'] = field['values'][0]['value']
            elif field['field_id'] == 5761:
                contact['email'] = field['values'][0]['value']

        return contact

# getContact('47226271')