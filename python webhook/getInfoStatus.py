#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from refreg import recovery_token
from writejson import write_json
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

    url = f'https://fortunaperm.amocrm.ru/api/v4/leads/pipelines/{pipeline_id}/statuses/{status_id}'
    res = requests.get(url, headers=header)
    if res.status_code != 200:
        recovery_token()
        getInfoStatus(pipeline_id, status_id)
    else:
        result = res.json()
        # print(result)
        if result['name'] == 'На подтверждении у партнера':
            return 'Новая заявка'
        elif result['id'] == 15921508:
            return 'Одобрено'
        elif result['id'] == 19569811:
            return 'Авторизовано'
        elif result['id'] == 143:
            return 'Отказ'        
        else:
            return result['name']