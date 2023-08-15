#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from refreg import recovery_token
from writejson import write_json
from getInfoStatus import getInfoStatus
from emtityLeads import getEmtityLead
from olap import olap


def getInfoLead(idlead):
    id = idlead
    info_lead = dict.fromkeys(
        ['status', 'idLead', 'price', 'contact', 'partner', 'dogovor', 'comment', 'credit_term'])
    info_lead['credit_term'] = '0'
    info_lead['dogovor'] = 'Договора пока нет'
    info_lead['comment'] = 'Комментария к сделке нет'

    with open('access_token.txt', 'r') as access:
        access_token = access.read()

    header = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/hal+json",
        "Content-Type": "application/json"
    }

    params = {
        'with': 'catalog_elements'
    }

    url = f'https://fortunaperm.amocrm.ru/api/v4/leads/{id}'
    res = requests.get(url, headers=header, params=params)
    if res.status_code != 200:
        recovery_token()
        getInfoLead(id)
    else:
        result = res.json()
        # print('result', result)
        # write_json(result)
        info_lead['idLead'] = result['id']
        info_lead['status'] = getInfoStatus(
            result['pipeline_id'], result['status_id'])
        info_lead['price'] = result['price']
        info_lead['contact'] = getEmtityLead(id)
        for field in result['custom_fields_values']:
            if field['field_id'] == 567605:
                info_lead['dogovor'] = field['values'][0]['value']
            elif field['field_id'] == 568491:
                info_lead['partner'] = olap(field['values'][0]['value'])
            elif field['field_id'] == 568539:
                info_lead['credit_term'] = field['values'][0]['value']
            elif field['field_id'] == 568541:
                info_lead['comment'] = field['values'][0]['value']
        # print(info_lead)
        return info_lead


# getInfoLead('12864245')
