# 2026-02-08_Empire_Sanitizer_v1_STABLE
import os
import shutil

# --- CONFIG ---
VAULT = r"C:\Users\Danny\Desktop\00_DaN_EMPIRE_VAULT_2026"
STRATEGY_DIR = os.path.join(VAULT, "DAN", "01_STRATEGIE")
ARCHIVE_DIR = os.path.join(VAULT, "97_SYSTEM_ARCHIV")

# Dateitypen, die definitiv System-Müll sind
JUNK_EXTENSIONS = [
    ".sqlite", ".sqlite-shm", ".sqlite-wal", ".db", 
    ".jsonlz4", ".bin", ".lock", ".ini", ".js", 
    ".dat", ".mozlz4", ".snapshot", ".txt" # Vorsicht mit .txt, aber im Browser-Kontext oft Müll
]

def clean_strategy_folder():
    print(f"🧹 DaN OS Sanitizer: Reinige {STRATEGY_DIR}...")
    
    if not os.path.exists(STRATEGY_DIR):
        print("❌ Pfad nicht gefunden. Reinigung abgebrochen.")
        return

    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    count = 0

    for file in os.listdir(STRATEGY_DIR):
        file_path = os.path.join(STRATEGY_DIR, file)
        
        # Nur Dateien prüfen (keine Ordner)
        if os.path.isfile(file_path):
            fn = file.lower()
            
            # Kriterium: Endung ist in der Junk-Liste ODER Name sieht kryptisch aus
            is_junk = any(fn.endswith(ext) for ext in JUNK_EXTENSIONS)
            
            # Ausnahmen für echte Business-Files (Schutz)
            is_protected = any(x in fn for x in ["plan", "report", "vertrag", "strategie", "inventory"])

            if is_junk and not is_protected:
                try:
                    shutil.move(file_path, os.path.join(ARCHIVE_DIR, file))
                    print(f"📦 Archiviert: {file}")
                    count += 1
                except Exception as e:
                    print(f"❌ Fehler bei {file}: {e}")

    print(f"\n✅ Reinigung abgeschlossen. {count} System-Dateien nach 97_SYSTEM_ARCHIV verschoben.")

if __name__ == "__main__":
    clean_strategy_folder()