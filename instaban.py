import time
from instabot import Bot

USUARIO ='saturnet'
PASSWORD ='Saquito1.1'


total_seguidores = []

bot = Bot()
bot.login(username=USUARIO, password=PASSWORD)

followers = bot.get_user_followers(USUARIO)
contador = 0
for follower in followers:
    contador = contador +1
    print(contador)
    mi_dic = {}
    mi_dic = bot.get_user_info(follower)
    total_seguidores.append(mi_dic["username"])
    if contador ==10:
        break

print('Personas a las que se les va a mandar el mensaje')
print(total_seguidores)

bot.send_message("Hola por favor sigue nuestra cuenta de instagram:https://www.instagram.com/codeecuadoroficial/ ",total_seguidores)
print('adios!')
