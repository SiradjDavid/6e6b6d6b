import requests


token_me = "7731363478:AAHsVlMbi9XI5tzcdIg2NJAr_APna9kNmKE"
id_me = "1933020265"


me=f'''
Welcome to venom fb hunt
~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

[ ! ] - THE TOOL ACTIVETID

~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
by : @V_N_M_1
'''
requests.get("https://api.telegram.org/bot"+str(token_me)+"/sendMessage?chat_id="+str(id_me)+"&text="+str(me))
