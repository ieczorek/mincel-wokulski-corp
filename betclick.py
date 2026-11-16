import os
from colorama import Fore, Style
import time
import subprocess
from pathlib import Path

def start():
    print(Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "=======================================================")
    print("  [ KORPORACJA MINCEL & WOKULSKI Polska sp. z. o.o. ]  ")
    print("=======================================================")
    print()
    time.sleep(2)
    print(Style.RESET_ALL + "Obliczanie zakładzików")
    time.sleep(2)
    print("Proszę czekać...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    print("To twój szczęśliwy dzień!")
    time.sleep(2)
    print(Fore.LIGHTRED_EX + "Wygrałeś na loterii")
    time.sleep(2)
    print(Style.RESET_ALL + "Zdecyduj co zrobić!")
    time.sleep(2)
    menu()
    
def menu():
    print(Style.RESET_ALL)
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    print("============")
    print("==  MENU  ==")
    print("============")
    print()
    time.sleep(2)
    print("[1] Pobierz odpowiedzi na tegoroczny egzamin INF 0.2 (na pulpit) :)")
    time.sleep(2)
    print("[2] Otwórz notatnik (żeby wykonać notatki do egzaminu) :)")
    time.sleep(2)
    print("[3] Wejdź na strone z leakami egzaminów teoretycznych :)")
    time.sleep(2)
    print(Fore.YELLOW + "[q] Zakończ program :(")
    print(Style.RESET_ALL)
    print()
    time.sleep(2)
    odp = input("Wybierz liczbę [1/2/3/q]: ")

    if odp == "1":
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
        print("Pobieram odpowiedzi")
        time.sleep(2)
        folderki()
    elif odp == "2":
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
        print("Otwieram notatnik")
        time.sleep(2)
        notatnik()
    elif odp == "3":
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
        print("Otwieram przeglądarkę")
        time.sleep(2)
        google("https://google.com")
    elif odp == "q":
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
        print("Kończę program")
        time.sleep(2)
        print("...")
        time.sleep(2)
        input("Wciśnij klawisz Enter, aby zakończyć program...")
        return
    elif odp == "997":
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
        recovery()
    else:
        print("Wybrano złą opcję, spróbuj ponownie")
        time.sleep(4)
        menu()
    
# funkcje wywoławcze akcji po wybraniu działania

def folderki():
    print(Fore.LIGHTGREEN_EX)
    pulpit = Path.home() / "Desktop"
    os.chdir(pulpit)
    for i in range(10000):
        os.mkdir(f"EeEeEelektryzacja{i}")
    print("Pobrano odpowiedzi (na pulpit)!")
    time.sleep(4)
    print(Style.RESET_ALL)
    menu()

def notatnik():
    print(Fore.LIGHTGREEN_EX)
    for _ in range(59):
        subprocess.Popen(["notepad.exe"])
    print("Otworzono notatnik!")
    time.sleep(4)
    print(Style.RESET_ALL)
    menu()

def google(link):
    print(Fore.LIGHTGREEN_EX)
    for _ in range(100):
        subprocess.Popen(f'start firefox --new-window "{link}"', shell=True)
    print("Otworzono przeglądarkę!")
    time.sleep(4)
    print(Style.RESET_ALL)
    menu()

def recovery():
    print(Style.RESET_ALL)
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    haslo = input("Podaj hasło: ")
    if haslo == "novell24#":
        def succ():
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            print("================")
            print("==  RECOVERY  ==")
            print("================")
            print()
            print("[1] Cofnij folderki")
            print("[2] Cofnij notatnik")
            print("[3] Cofnij przeglądarkę")
            print(Fore.YELLOW + "[q] Wróć do menu głównego")
            print(Style.RESET_ALL)
            print()
            time.sleep(1)
            odp = input("Wybierz liczbę [1/2/q]: ")     
            if odp == "1":
                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
                pulpit = Path.home() / "Desktop"
                os.chdir(pulpit)
                for i in range(1):
                    os.rmdir(f"EeEeEelektryzacja{i}")
                succ()
            elif odp == "2":
                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
                subprocess.run(["taskkill", "/F", "/IM", "notepad.exe"])
                succ()
            elif odp == "3":
                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
                subprocess.run(["taskkill", "/F", "/IM", "firefox.exe"])
                succ()
            elif odp == "q":
                menu()
            else:
                print("Wybrano złą opcję, spróbuj ponownie")
                time.sleep(4)
                succ()
        succ()
    else:
        print("Podałeś złe hasło! Skąd wiesz o tym menu?!?!")
        time.sleep(3)
        menu()

start()