#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from refreg8250 import recovery_token

import json
from getInfoStatus8250 import getInfoStatus


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

    url = f'https://8250.amocrm.ru/api/v4/contacts/{id}'
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
            if field['field_id'] == 223671:
                contact['phone'] = field['values'][0]['value']
            elif field['field_id'] == 223673:
                contact['email'] = field['values'][0]['value']

        return contact

# getContact('38639907')