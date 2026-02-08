# 2026-02-08_Empire_Power_Sorter_v4
import os
import shutil

# --- CONFIG ---
SOURCE = r"C:\Users\Danny\Desktop\GOOGLE_DRIVE_MASTER"
VAULT = r"C:\Users\Danny\Desktop\00_DaN_EMPIRE_VAULT_2026"
PRIVATE_OUTSIDE = r"C:\Users\Danny\Desktop\00_PRIVAT_QUARANTÄNE_BAU"

PROJECTS = ["PRINZESSIN", "SCHERBENHAUFEN", "ES_KOMMT", "MAGNET", "MEER", "RENE"]

def get_sub_folder(fn):
    """Bestimmt die Säule basierend auf dem Dateityp/Namen."""
    fn = fn.upper()
    if any(ex in fn for ex in [".WAV", ".MP3", ".ALS", ".LOGIC", "BEAT", "INSTRUMENTAL"]):
        return "03_PRODUKTION"
    if any(ex in fn for ex in [".JPG", ".PNG", ".MP4", ".MOV", "COVER", "PROMO"]):
        return "05_MARKETING"
    if any(ex in fn for ex in [".TXT", ".DOC", "LYRICS", "TEXT"]):
        return "02_KREATIV"
    if "MASTER" in fn or "FINAL" in fn:
        return "04_FINALS"
    return "01_STRATEGIE"

def start_sorting():
    print("🚀 DaN OS: Power-Sort V4 startet...")
    os.makedirs(PRIVATE_OUTSIDE, exist_ok=True)

    for root, dirs, files in os.walk(SOURCE):
        for file in files:
            if ".git" in root: continue # Git-Ordner ignorieren
            
            old_path = os.path.join(root, file)
            fn = file.upper()
            
            # 1. RADIKALE BAU-TRENNUNG
            if any(x in (fn + root.upper()) for x in ["BAU", "RECHNUNG", "HAUS", "PLAN", "STATIK"]):
                shutil.move(old_path, os.path.join(PRIVATE_OUTSIDE, file))
                continue

            # 2. PROJEKT-CHECK
            target_project = None
            for p in PROJECTS:
                if p in (fn + root.upper()):
                    target_project = p
                    break
            
            # 3. ZIEL-PFAD BAUEN
            sub = get_sub_folder(file)
            if target_project:
                dest_dir = os.path.join(VAULT, target_project, sub)
            else:
                dest_dir = os.path.join(VAULT, sub) # Globaler Säulen-Ordner

            os.makedirs(dest_dir, exist_ok=True)
            try:
                shutil.move(old_path, os.path.join(dest_dir, file))
                print(f"✅ Verschiebe: {file} -> {dest_dir}")
            except: pass

if __name__ == "__main__":
    start_sorting()