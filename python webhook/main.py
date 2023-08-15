from writejson import write_json
from flask import Flask, abort
from flask import request
from flask import jsonify
from pyngrok import conf, ngrok
from werkzeug.datastructures import ImmutableMultiDict
from getinfolead import getInfoLead
from sendmessage import sendwhatsapp, sendtelegram, sendwhatsappdeveloper
import sys
sys.path.insert(1, '../8250')
from main8250 import main8250


app = Flask(__name__)
ngrok.set_auth_token('2RTtt0IeuqmzNFKESbDHTe4lKvF_7uQejiESyx5rfK6rZcspk')
public_url = ngrok.connect(5000).public_url
conf.get_default().region = "ru"




@app.route("/fortuna", methods=['GET', 'POST'])
def webhook():

    if request.method == 'POST':

        r = ImmutableMultiDict(request.form)

        # write_json(request.form)
        
        data_res = getInfoLead(r.getlist('leads[status][0][id]')[0])
        # print(data_res)

        if data_res['partner']['agreement'] == 'да, через WhatsApp' and data_res['partner']['whatsapp'] != None:
            sendwhatsapp(data_res)
        elif data_res['partner']['agreement'] == 'да, через Telegram' and data_res['partner']['telegram'] != None:
            sendtelegram(data_res)
        else:
            sendwhatsappdeveloper(data_res)
        return 'ОК'
    return '<h1>webhook</h1>'

@app.route('/8250', methods=['GET', 'POST'])
def amo8250():
    if request.method == 'POST':

        r = ImmutableMultiDict(request.form)

        # write_json(request.form)
        
        data_res = main8250(r.getlist('leads[status][0][id]')[0])
        # print(data_res)

        if data_res['partner']['agreement'] == 'да, через WhatsApp' and data_res['partner']['whatsapp'] != None:
            sendwhatsapp(data_res)
        elif data_res['partner']['agreement'] == 'да, через Telegram' and data_res['partner']['telegram'] != None:
            sendtelegram(data_res)
        else:
            sendwhatsappdeveloper(data_res)
     
        return 'ОК'
    return '<h1>сюда приходят 8250</h1>'


@app.route('/')
def index():

    # if request.method == 'POST':
    #     r = request.get_json()
    #     write_json(r)
    #     print(jsonify(r))
    #     return jsonify(r)
    return f"Это страница для тестирования вебхуков <a href={public_url}>{public_url}</a> для фортуны <a href={public_url}/fortuna>{public_url}/fortuna</a> "


def main():
    pass


if __name__ == "__main__":
    app.run(port=5000)
