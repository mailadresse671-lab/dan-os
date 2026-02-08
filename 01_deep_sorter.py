# 2026-02-08_Empire_Enforcer_v6_DIAGNOSE
import os
import shutil

SOURCE = r"C:\Users\Danny\Desktop\DESKTOP_INBOX\GOOGLE_DRIVE_MASTER"
VAULT = r"C:\Users\Danny\Desktop\00_DaN_EMPIRE_VAULT_2026"
PRIVATE_OUTSIDE = r"C:\Users\Danny\Desktop\00_PRIVAT_QUARANTÄNE_BAU"

# Erweitere diese Liste, falls Songs anders geschrieben werden!
PROJECTS = ["PRINZESSIN", "SCHERBENHAUFEN", "ES_KOMMT", "MAGNET", "MEER", "RENE", "DAN"]

def get_target_pillar(filename):
    fn = filename.upper()
    if any(ex in fn for ex in [".WAV", ".MP3", ".ALS", ".LOGIC", "BEAT"]): return "03_PRODUKTION"
    if any(ex in fn for ex in [".JPG", ".PNG", ".MP4", ".MOV", "COVER"]): return "05_MARKETING"
    if any(ex in fn for ex in [".TXT", ".DOC", "LYRICS"]): return "02_KREATIV"
    if "MASTER" in fn or "FINAL" in fn: return "04_FINALS"
    return "01_STRATEGIE"

def start_sorting():
    print(f"🔍 DIAGNOSE: Scanne {SOURCE}...")
    count = 0
    
    if not os.path.exists(SOURCE):
        print("❌ PFAD NICHT GEFUNDEN!")
        return

    for root, dirs, files in os.walk(SOURCE):
        if ".git" in root: continue
        for file in files:
            old_path = os.path.join(root, file)
            fn_upper = file.upper()
            
            # BAU-CHECK
            if any(x in (fn_upper + root.upper()) for x in ["BAU", "RECHNUNG", "HAUS"]):
                dest = PRIVATE_OUTSIDE
            else:
                # PROJEKT-SUCHE
                target_project = next((p for p in PROJECTS if p in (fn_upper + root.upper())), None)
                pillar = get_target_pillar(file)
                
                if target_project:
                    dest = os.path.join(VAULT, target_project, pillar)
                else:
                    dest = os.path.join(VAULT, pillar)

            os.makedirs(dest, exist_ok=True)
            try:
                shutil.move(old_path, os.path.join(dest, file))
                print(f"Moved: {file} -> {dest}")
                count += 1
            except Exception as e:
                print(f"Skipped: {file} (Error: {e})")
    
    print(f"--- SCAN FERTIG. {count} Dateien verarbeitet. ---")

if __name__ == "__main__":
    start_sorting()