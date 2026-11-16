import shutil
from pathlib import Path

try:
    # NAPRAWA: Dodano Path() oraz przedrostek 'r' przed cudzysłowem, aby Python ignorował znaki specjalne w ścieżce Windows
    sciezka_haha = Path(r"C:\Users\n.wieczorek\VirtualBox VMs")
    
    if not sciezka_haha.exists():
        print(f"Folder {sciezka_haha} nie istnieje.")
    else:
        # Iteracja po zawartości i usuwanie plików/folderów
        for element in sciezka_haha.iterdir():
            try:
                if element.is_file() or element.is_symlink():
                    element.unlink()
                elif element.is_dir():
                    shutil.rmtree(element)
                print(f"Usunięto: {element.name}")
            except Exception as e:
                print(f"Nie udało się usunąć {element.name}: {e}")
                
        print("\nZawartość folderu została pomyślnie usunięta.")
    
except Exception as e:
    print(f"Wystąpił błąd ogólny: {e}")

# Zatrzymanie okna konsoli, aby zdążyć przeczytać komunikaty
input("\nNaciśnij Enter, aby zamknąć program...")
