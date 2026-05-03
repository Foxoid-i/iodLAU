#Версия 1.0
import minecraft_launcher_lib
import subprocess
import sys
print("\ i o d  \\" \
    "\ i o d \\" \
        "\ i o d \\")
print("Welcome to iod launcher!")
print("\ i o d  \\" \
    "\ i o d \\" \
        "\ i o d \\")
minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
verch = input("На какой версии вы хотите играть?(Например 1.12.2) ")
minecraft_launcher_lib.install.install_minecraft_version(verch, minecraft_directory)
#setin = input("Хотите изменить настройки?(да , нет) ")
#options = iodAU.customres , iodAU.reswid , iodAU.reshei
#if setin == "да":
# input("Разрешение экрана: 1) 1920x1080 2) нету" )
# if input == "1":
#  iodAU.customres
#  iodAU.reswid
#  iodAU.reshei
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