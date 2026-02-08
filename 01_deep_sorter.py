# 2026-02-08_Empire_Enforcer_v5_1
import os
import shutil

# --- KORRIGIERTER PFAD ---
SOURCE = r"C:\Users\Danny\Desktop\DESKTOP_INBOX\GOOGLE_DRIVE_MASTER"
VAULT = r"C:\Users\Danny\Desktop\00_DaN_EMPIRE_VAULT_2026"
PRIVATE_OUTSIDE = r"C:\Users\Danny\Desktop\00_PRIVAT_QUARANTÄNE_BAU"

PROJECTS = ["PRINZESSIN", "SCHERBENHAUFEN", "ES_KOMMT", "MAGNET", "MEER", "RENE"]

def get_target_pillar(filename):
    fn = filename.upper()
    if any(ex in fn for ex in [".WAV", ".MP3", ".ALS", ".LOGIC", ".FLAC", "BEAT", "INSTRUMENTAL"]):
        return "03_PRODUKTION"
    if any(ex in fn for ex in [".JPG", ".PNG", ".MP4", ".MOV", "COVER", "PROMO", "TIKTOK"]):
        return "05_MARKETING"
    if any(ex in fn for ex in [".TXT", ".DOC", ".DOCX", "LYRICS", "TEXT"]):
        return "02_KREATIV"
    if "MASTER" in fn or "FINAL" in fn:
        return "04_FINALS"
    return "01_STRATEGIE"

def start_sorting():
    print(f"🚀 DaN OS: Scanne jetzt: {SOURCE}")
    if not os.path.exists(SOURCE):
        print("❌ FEHLER: Der Pfad existiert nicht. Bitte prüfen!")
        return

    os.makedirs(PRIVATE_OUTSIDE, exist_ok=True)

    for root, dirs, files in os.walk(SOURCE):
        if ".git" in root or "dan-os" in root: continue
            
        for file in files:
            old_path = os.path.join(root, file)
            fn_upper = file.upper()
            context = (fn_upper + root.upper())
            
            if any(x in context for x in ["BAU", "RECHNUNG", "HAUS", "PLAN", "STATIK", "STEUER"]):
                dest_dir = PRIVATE_OUTSIDE
            else:
                pillar = get_target_pillar(file)
                target_project = next((p for p in PROJECTS if p in context), None)
                dest_dir = os.path.join(VAULT, target_project, pillar) if target_project else os.path.join(VAULT, pillar)

            os.makedirs(dest_dir, exist_ok=True)
            try:
                shutil.move(old_path, os.path.join(dest_dir, file))
                print(f"✅ {file} verschoben.")
            except Exception: pass

if __name__ == "__main__":
    start_sorting()