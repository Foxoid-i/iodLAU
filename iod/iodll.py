#Версия 1.0
import minecraft_launcher_lib
import subprocess
import sys
from os import listdir
import json
print("\ i o d  \\" \
    "\ i o d \\" \
        "\ i o d \\")
print("Welcome to iod launcher!")
print("\ i o d  \\" \
    "\ i o d \\" \
        "\ i o d \\")
setdir = input("Нужно ли указывать dir?(Папка Versios) (да/нет) : ")
setdir
if setdir == "да":
    verdir = input("Путь до versios(Полностью!): ")
    verdir
    with open("patchtodir.json", "w", encoding="utf-8") as f:
     json.dump(verdir, f, indent=4, ensure_ascii=False)
else:
    pass
minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
watdir = input("Хотите ли просмотреть свои версии? (да/нет) : ")
watdir
if watdir == "да":
    with open("patchtodir.json", "r", encoding="utf-8") as f:
     data = json.load(f)
    shdir = listdir(data)
    print(shdir)
else:
    pass
verch = input("На какой версии вы хотите играть?(Например 1.12.2) ")
minecraft_launcher_lib.install.install_minecraft_version(verch, minecraft_directory)
setmodld = input("Нужно ли устанавливать модлоадер? (да/нет) : ")
setmodld
if setmodld == "да":
    mdld = input("Какой загрузчик модов вы хотите скачать(ЗАПУСК БУДЕТ БЕЗ НЕГО)? 1) forge 2) fabric 3) neoforge : ")
    mdld
    if mdld == "1":
        modload =  minecraft_launcher_lib.mod_loader.get_mod_loader("forge")
    elif mdld == "2":
        modload =  minecraft_launcher_lib.mod_loader.get_mod_loader("fabric")
    elif mdld == "3":
        modload =  minecraft_launcher_lib.mod_loader.get_mod_loader("neoforge")
    modload.install(verch, minecraft_directory)
else:
    pass
import uuid
usern = input("Впишите ваше имя пользователя(Любое): ")
ram_gb = input("Сколько ГБ оперативной памяти выделить игре? ")
ram_gb
jvm_args = ["-Xmx" + ram_gb + "G", "-Xms" + ram_gb + "G"]
options = {
    "username": usern,
    "uuid": str(uuid.uuid4()),
    "token": "0",
    "customResolution": True,
    "resolutionWidth": "1920",
    "resolutionHeight": "1080",
    "jvmArguments": jvm_args
}
iodakt = minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(verch, minecraft_directory, options)
subprocess.run(iodakt)