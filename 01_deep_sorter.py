# 2026-02-08_Empire_Architect_Sorter_v3
import os
import shutil

# --- CONFIG ---
SOURCE = r"C:\Users\Danny\Desktop\GOOGLE_DRIVE_MASTER"
VAULT = r"C:\Users\Danny\Desktop\00_DaN_EMPIRE_VAULT_2026"
PRIVATE_OUTSIDE = r"C:\Users\Danny\Desktop\00_PRIVAT_QUARANTÄNE_BAU" # Komplett getrennt!

PROJECTS = ["PRINZESSIN", "SCHERBENHAUFEN", "ES_KOMMT", "MAGNET", "MEER", "RENE"]

SUB_STRUCTURE = [
    "01_STRATEGIE_BIZ",
    "02_KREATIV_LAB",
    "03_PRODUKTION_FACTORY",
    "04_RELEASES_FINALS",
    "05_MARKETING_PROMO"
]

def build_structure(project_name):
    path = os.path.join(VAULT, project_name)
    for sub in SUB_STRUCTURE:
        os.makedirs(os.path.join(path, sub), exist_ok=True)
    return path

def start_sorting():
    print("🏗️  DaN OS: Radikale Trennung aktiv. BAU wird isoliert...")
    
    # Sicherstellen, dass der externe Bau-Ordner existiert
    os.makedirs(PRIVATE_OUTSIDE, exist_ok=True)

    for root, dirs, files in os.walk(SOURCE):
        for file in files:
            old_path = os.path.join(root, file)
            fn = file.upper()
            context = (fn + root.upper())
            
            try:
                # --- 1. BAU-FILTER (EXTERNE ISOLATION) ---
                if any(x in context for x in ["BAU", "RECHNUNG", "HAUS", "PLAN", "IMMOBILIE", "STATIK"]):
                    dest = PRIVATE_OUTSIDE
                    print(f"🚫 PRIVAT-ISOLATION: {file} -> {dest}")
                
                # --- 2. MUSIK-PROJEKT ZUORDNUNG ---
                else:
                    target_project = None
                    for p in PROJECTS:
                        if p in context:
                            target_project = p
                            break
                    
                    if target_project:
                        project_path = build_structure(target_project)
                        # Unterordner-Logik
                        if any(fn.endswith(ex) for ex in [".WAV", ".MP3", ".ALS", ".LOGIC"]):
                            sub = "03_PRODUKTION_FACTORY"
                            if "MASTER" in fn: sub = "04_RELEASES_FINALS"
                        elif any(fn.endswith(ex) for ex in [".JPG", ".PNG", ".MP4", ".MOV"]):
                            sub = "05_MARKETING_PROMO"
                        elif any(fn.endswith(ex) for ex in [".TXT", ".DOC", ".PDF"]):
                            sub = "02_KREATIV_LAB"
                        else:
                            sub = "01_STRATEGIE_BIZ"
                        dest = os.path.join(project_path, sub)
                    else:
                        dest = os.path.join(VAULT, "98_UNSORTIERT_MUSIC")
                        os.makedirs(dest, exist_ok=True)

                shutil.move(old_path, os.path.join(dest, file))
            except Exception as e:
                pass

if __name__ == "__main__":
    start_sorting()