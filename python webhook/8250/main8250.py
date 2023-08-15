import requests
from refreg8250 import recovery_token
from getInfoStatus8250 import getInfoStatus
from emtityLeads8250 import getEmtityLead
from olap import olap

def main8250(idLead):
    
    id = idLead
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

    url = f'https://8250.amocrm.ru/api/v4/leads/{id}'
    res = requests.get(url, headers=header, params=params)
    
    if res.status_code != 200:
        recovery_token()
        main8250(id)
    else:
        result = res.json()
        
        # write_json(result)
        info_lead['idLead'] = result['id']
        info_lead['status'] = getInfoStatus(
            result['pipeline_id'], result['status_id'])
        info_lead['price'] = result['price']
        info_lead['contact'] = getEmtityLead(id)
        for field in result['custom_fields_values']:
            if field['field_id'] == 563479:
                info_lead['partner'] = olap(field['values'][0]['value'])
            elif field['field_id'] == 564903:
                info_lead['credit_term'] = field['values'][0]['value']
            elif field['field_id'] == 568571:
                info_lead['comment'] = field['values'][0]['value']
        # print(info_lead)
        return info_lead
    
# main8250('25631375')