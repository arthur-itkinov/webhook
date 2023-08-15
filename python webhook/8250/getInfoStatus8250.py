#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from refreg8250 import recovery_token

import json

# Получаю название статуса


def getInfoStatus(pipeline_id, id):
    pipeline_id = pipeline_id
    status_id = id
    with open('access_token.txt', 'r') as access:
        access_token = access.read()

    header = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/hal+json",
        "Content-Type": "application/json"
    }

    url = f'https://8250.amocrm.ru/api/v4/leads/pipelines/{pipeline_id}/statuses/{status_id}'
    # url = f'https://8250.amocrm.ru/api/v4/leads/pipelines/{pipeline_id}/statuses'
    res = requests.get(url, headers=header)
    
    if res.status_code != 200:
        recovery_token()
        getInfoStatus(pipeline_id, status_id)
    else:
        result = res.json()
        # print(result)
        # ульяновск, пенза, магнитогорск, ярославль, самара, уфа, кц пермь, кц ульяновск
        if result['id'] in [57190310, 57190250, 57190330, 57190354, 57190382, 57190414, 57190442, 57190514]:
            return 'Новая заявка'
        elif result['id'] in [26389036, 26389024, 28429402, 28432888, 28432915, 32166535, 38052454, 38052481]:
            return 'Одобрено'
        elif result['id'] in [26389102, 26389027, 28429405, 28432891, 28432918, 32166583, 38052457, 38052484]:
            return 'Авторизовано'
        elif result['id'] == 143:
            return 'Отказ'        
        else:
            return result['name']