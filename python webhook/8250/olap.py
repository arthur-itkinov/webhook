import requests
from getEmtityPartner8250 import getPartner


# скрипт получения id партнера в воронке привлечения id
def olap(id):
    url = 'https://ak-i.ru/.assets/php/api/olap_parthners.php?olap=true'
    res = requests.get(url)
    result = res.json()
   
    partner = {}
    partner['idPartnerOlap'] = id
    if id in result['succsess']:
       
        idPartner = result['succsess'][id]

        partner = getPartner(idPartner)

    return partner


# olap('957301')
