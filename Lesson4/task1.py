from rich.console import Console
from time import sleep
from random import random
from config_sys import *

def pathFile():
    return "C:\\Users\\User\\Desktop\\pcinfo.txt"    

def writeInfoInFile(parametersMenu):
    path = pathFile()
    with console.status("[magenta]Waiting...", spinner="point", spinner_style="pink"):
        while parametersMenu.keys() != False:
            match parametersMenu:
                case {"CPU INFO": True}:
                    writeProccesorInfo(path)
                    parametersMenu["CPU INFO"] = False
                case {"RAM INFO": True}:
                    writeRamInfo(path)
                    parametersMenu["RAM INFO"] = False
                case {"OS INFO": True}:
                    writePCInfo(path)
                    parametersMenu["OS INFO"] = False
                case {"STORAGE INFO": True}:
                    writeStorageInfo(path)
                    parametersMenu["STORAGE INFO"] = False
                case _:
                    endWork()

def endWork():
    console.rule(style="yellow")
    console.print("[green]Program completed successfully! Exiting...")
    proccesTime()
    exit()

def askParameter():
    return int(console.input("[yellow bold]Choose: ")) - 1

def selectParameter(choice):
    parMenu = list(parametersMenu)
    if choice >= 0 and choice < len(parametersMenu): 
        parametersMenu[parMenu[choice]] = not parametersMenu[parMenu[choice]]
    elif choice == -1:
        writeInfoInFile(parametersMenu)
        exit()
    else:
        console.print("[red underline]Unknown parameter")
        sleep(2)

def proccesTime():
    return sleep(random())

def logicConverterOptions(parameter):
    return "[green bold]yes" if parameter else "[red bold]no"

def showOptions():
    with console.status("[magenta]Waiting...", spinner="point", spinner_style="pink"):
        for parameter in parametersMenu:
            console.print("[not bold magenta]" + str(list(parametersMenu).index(parameter) + 1) + ") [/not bold magenta]" + \
                 "[", str(parameter), "]: " + \
                 "[", str(logicConverterOptions(parametersMenu[parameter])), "]",style="purple")
            proccesTime()
    console.print("[red bold]0)[/red bold] [green bold underline]Continue with selected parameters.\n")

def startMenu():
    console.clear()
    console.rule("[red bold]Choosing an parameter", style="yellow", align="right")
    showOptions()
    selectParameter(askParameter())

console = Console()
parametersMenu = {
    "CPU INFO": False,
    "RAM INFO": False,
    "OS INFO": False,
    "STORAGE INFO": False
}

def main():
    while True:
        startMenu()

main()