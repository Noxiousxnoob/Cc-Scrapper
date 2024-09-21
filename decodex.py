import os
import sys
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError
import requests
import re
import time

api_id = 27480407
api_hash = 'b0bc9ddbf2f26cbbabb0998936f89d14'

client = TelegramClient("ssshl", api_id, api_hash)
client.start()

def get_user_input(prompt_text):
    return input(prompt_text)

scrapper_name = get_user_input("Please enter your scrapper name: ")
channel_username = get_user_input("Your channel username: ")
source_scrapper_1 = get_user_input("Please Provide Source Scrapper 1 (Telegram channel link): ")
source_scrapper_2 = get_user_input("Great! Now Give Source Scrapper no 2 (Telegram channel link): ")
destination_channel_id = get_user_input("Provide Your Channel 'ID' where Cards Will Be Sent (e.g., -111111111111): ")
developer_name = "@unsack @bwmethood"
file_name = f'{developer_name}.txt'

if not os.path.exists(file_name):
    print(f"Modification not allowed. Developer is {developer_name}")
    sys.exit(1)

def RoldexVerseCcs(id):
    id = str(id)
    with open(file_name, 'w') as f:
        if f.write(id):
            return True
        else:
            return False

def get_bin_data(cc):
    bin_prefix = cc[:6]
    response = requests.get(f"https://bins.antipublic.cc/bins/{bin_prefix}")
    data = response.json()
    return data

with client:
    print("Deploye success Made by @unsack @bwmethood")
    while True:
        try:
            req = requests.Session()
            with open(file_name, 'r') as f:
                rd = int(f.read())
            channelList = [source_scrapper_1, source_scrapper_2]
            fornum = len(channelList)
            for i in range(fornum):
                messages = client.iter_messages(channelList[i], min_id=rd, wait_time=5)
                message_count = 0
                for message in messages:
                    msg = message.text
                    if not msg:
                        raise Exception('empty data')
                    else:
                        input = re.findall(r"[0-9]+", msg)
                        try:
                            if not input or len(input) == 2:
                                raise Exception("Invalid Data")
                            elif len(input) > 4 and len(input[1]) < 2:
                                cc = input[0]
                                mes = input[1]
                                ano = input[2]
                                cvv = input[3]
                            elif len(input[1]) == 3:
                                cc = input[0]
                                mes = input[2]
                                cvv = input[1]
                                ano = input[3]
                                if len(mes) > 3:
                                    mes = mes[:2]
                                    ano = mes[:2]
                            elif len(input[1]) > 3:
                                cc = input[0]
                                mes = input[1][:2]
                                ano = input[1][2:]
                                cvv = input[2]
                            elif len(input[0]) < 15:
                                raise Exception('Invalid data')
                            else:
                                cc = input[0]
                                mes = input[1]
                                ano = input[2]
                                cvv = input[3]
                        except Exception as e:
                            print(e)
                        else:
                            bin_data = get_bin_data(cc)
                            brand = bin_data.get('brand', 'Unknown')
                            country = bin_data.get('country', 'Unknown')
                            bank = bin_data.get('bank', 'Unknown')
                            bin_prefix = cc[:6]

                            lista = f"<code>{cc}|{mes}|{ano}|{cvv}</code>"
                            respo = f"""
- {scrapper_name} | 
- 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅ ...
━━━━━━━━━━━━━━━━
♤ Card : {lista}
♤ Info : {brand}
♤ Bank : {bank}
♤ Bin  : {bin_prefix} xxxxxxxxxxx
♤ Country : {country}
♤ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: 1000: Approved ✅
♤ VBV : <a href="https://t.me/Bwmethood/574">BUY PREMIUM SCRAPPER 👈👈</a>
━━━━━━━━━━━━━━━━
𝐒𝐜𝐫𝐚𝐩𝐩𝐞𝐫 𝐁𝐲 {channel_username}
Developer- {developer_name}"""

                            client.send_message(int(destination_channel_id), respo, parse_mode='html')
                            message_count += 1
                            if message_count >= 2:
                                time.sleep(9)
                                message_count = 0
                wd = RoldexVerseCcs(message.id)
        except FloodWaitError as e:
            print('Have to sleep', e.seconds, 'seconds')
            time.sleep(e.seconds)
        except Exception as e:
            print(e)
