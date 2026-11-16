from tkinter import *

# 1. Funkcja MUSI być na samej górze i mieć inną nazwę niż zmienna przycisku
def klikniecie():
    # Rysujemy nowy tekst trochę niżej (Y=60), żeby nie nakładał się na pierwszy
    canvas.create_text(100, 60, text="Jestem hakerem", fill="green", font=("Consolas", 12))
    print("Kliknięto!")

window = Tk()
window.geometry("420x420")
window.title("Betclick V4 - Mincel & Wokulski")
window.config(background="#32a852")

# UWAGA: Jeśli nie masz pliku "icon.ico" w folderze z kodem, 
# ta linijka wyrzuci błąd. Jeśli tak się stanie, zakomentuj ją dodając # na początku.
# window.iconbitmap("icon.ico") 

# Zmniejszyłem wysokość Canvas do 300, żeby na dole zmieścił się przycisk
canvas = Canvas(window, width=420, height=300, bg="#000000", highlightthickness=0)
canvas.pack()

# Zmieniłem Y z 10 na 30, żeby tekst był w pełni widoczny
canvas.create_text(100, 30, text="Witaj Świecie!!!!!!!", fill="green", font=("Consolas", 12))

# Tutaj command wskazuje na bezpieczną nazwę funkcji 'klikniecie'
przycisk_button = Button(
    window, 
    text="Postaw zakład", 
    command=klikniecie,
    font=("Arial", 12, "bold"),
    bg="#ffffff",          
    fg="#32a852",          
    activebackground="#e0e0e0", 
    padx=20,               
    pady=10                
)

przycisk_button.pack(pady=10)

window.mainloop()
