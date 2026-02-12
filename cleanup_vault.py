import os
import shutil

VAULT = os.path.expanduser("~/EMPIRE_PROJECTS/00_DaN_EMPIRE_VAULT_2026")
TRASH_KEYWORDS = ["untitled", "test", "check", "OH OH OH", "copy"]

def cleanup():
    print("🧹 Reinigung der Factory läuft...")
    for root, dirs, files in os.walk(VAULT):
        for file in files:
            # 1. Müll-Dateien erkennen und in 99_SYSTEM_ARCHIV schieben
            if any(k in file for k in TRASH_KEYWORDS) or file.endswith(".zip"):
                dest = os.path.join(VAULT, "99_SYSTEM_ARCHIV", "RESTORE_OR_TRASH")
                os.makedirs(dest, exist_ok=True)
                shutil.move(os.path.join(root, file), os.path.join(dest, file))
                print(f"♻️  Verschoben nach Archiv: {file}")

            # 2. Barcode-Check (Datum erzwingen)
            if not file[0:4].isdigit() and not file.startswith("dan_"):
                # Hier könnten wir automatisch umbenennen, aber wir loggen es erst mal
                print(f"⚠️  Kein Barcode-Format: {file}")

    print("✅ Vault ist jetzt sauber und strukturiert.")

if __name__ == "__main__":
    cleanup()
