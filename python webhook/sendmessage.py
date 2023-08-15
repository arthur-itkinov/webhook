import requests


def sendwhatsapp(result):
    URL = 'https://api.wazzup24.com/v3/message'
    API = "61b976dbc76d4b308f4775fbd74f0bca"
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API}"
    }
    parapms = {
        "channelId": "8b9d956a-7289-43fb-8400-0b9abe5c7e2d",
        "chatType": "whatsapp",  # Тип чата.
        "chatId": result['partner']['whatsapp'],
        "text": f"Статус: {result['status']} \nКлиент: {result['contact']['name']} {result['contact']['phone']} {result['contact']['email']} \nСрок: {result['credit_term']} мес. \nСумма заявки: {result['price']} \n№ кредитного договора: {result['dogovor']} \nКомментарий: {result['comment']}",
    }
    r = requests.post(URL, headers=header, json=parapms)
    print(r.status_code)

def sendwhatsappdeveloper(data):
    URL = 'https://api.wazzup24.com/v3/message'
    API = "61b976dbc76d4b308f4775fbd74f0bca"
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API}"
    }
    parapms = {
        # Id канала (uuidv4), через который нужно отправить сообщение.
        "channelId": "8b9d956a-7289-43fb-8400-0b9abe5c7e2d",
        "chatType": "whatsapp",  # Тип чата.
        # Id чата (аккаунт контакта в мессенджере):
        # "chatId": f"{result['partner']['whatsapp']}",
        "chatId": "+79129800566",

        # Текст сообщения в зависимости от статуса
        "text": f"Информация не может быть отправлена партнеру. \nИнфа о лиде: {data}",
    }
    r = requests.post(URL, headers=header, json=parapms)

def sendtelegram(result):
    URL = 'https://api.wazzup24.com/v3/message'
    API = "61b976dbc76d4b308f4775fbd74f0bca"
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API}"
    }
    parapms = {
        "channelId": "597ec2bf-1ac6-41a7-8ea5-535d5d8954e9",
        "chatType": "telegram",  # Тип чата.
        "phone": result['partner']['telegram'],
        "text": f"Статус: {result['status']} \nКлиент: {result['contact']['name']} {result['contact']['phone']} {result['contact']['email']} \nСрок: {result['credit_term']} мес. \nСумма заявки: {result['price']} \nКомментарий: {result['comment']}",
    }
    r = requests.post(URL, headers=header, json=parapms)


