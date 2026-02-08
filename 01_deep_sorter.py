# YYYY-MM-DD_Deep_Sorter_v1
import os
import shutil

# --- KONFIGURATION (Deine Master-Pfade) ---
SOURCE = r"C:\Users\Danny\Desktop\GOOGLE_DRIVE_MASTER"
VAULT = r"C:\Users\Danny\Desktop\00_DaN_EMPIRE_VAULT_2026"

def start_sorting():
    print("🕵️ DaN OS: Starte Tiefenscan...")
    
    # Sicherstellen, dass die Zielstruktur existiert (Phase 2 deines Plans)
    categories = ["01_STRATEGIE", "02_KREATIV", "03_PRODUKTION", "04_FINALS", "05_MARKETING", "99_PRIVAT_BAU"]
    for cat in categories:
        os.makedirs(os.path.join(VAULT, cat), exist_ok=True)

    # Rekursiver Scan durch alle Unterordner
    for root, dirs, files in os.walk(SOURCE):
        for file in files:
            old_path = os.path.join(root, file)
            fn = file.upper()
            
            # --- SORTIER-LOGIK ---
            # 1. Privat/Bau Filter
            if any(x in (fn + root.upper()) for x in ["BAU", "RECHNUNG", "HAUS", "PLAN"]):
                dest = os.path.join(VAULT, "99_PRIVAT_BAU")
            # 2. Audio/Produktion
            elif any(fn.endswith(ext) for ext in [".WAV", ".MP3", ".ALS", ".LOGIC"]):
                dest = os.path.join(VAULT, "03_PRODUKTION")
            # 3. Marketing/Visuals
            elif any(fn.endswith(ext) for ext in [".JPG", ".PNG", ".MP4", ".MOV"]):
                dest = os.path.join(VAULT, "05_MARKETING")
            # 4. Rest nach Strategie/Kreativ
            else:
                dest = os.path.join(VAULT, "02_KREATIV")

            try:
                shutil.move(old_path, os.path.join(dest, file))
                print(f"✅ Verschoben: {file} -> {os.path.basename(dest)}")
            except Exception as e:
                print(f"❌ Fehler bei {file}: {e}")

if __name__ == "__main__":
    start_sorting()