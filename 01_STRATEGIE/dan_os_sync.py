import os
import json
from datetime import datetime

DRIVE_PATH = r"C:\Users\Danny\Desktop\GOOGLE_DRIVE_MASTER"
OUTPUT_FILE = os.path.join(DRIVE_PATH, "dan_os_final_structure.json")

def create_manifest():
    print("📊 ERSTELLE ABSCHLUSS-INVENTUR...")
    if not os.path.exists(DRIVE_PATH): return
    
    inventory = {
        "status": "Systematisch Sortiert V21",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "projekte": {}
    }
    
    for project in os.listdir(DRIVE_PATH):
        proj_path = os.path.join(DRIVE_PATH, project)
        if os.path.isdir(proj_path):
            inventory["projekte"][project] = {
                sub: os.listdir(os.path.join(proj_path, sub))
                for sub in os.listdir(proj_path)
                if os.path.isdir(os.path.join(proj_path, sub))
            }
            
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, indent=4, ensure_ascii=False)
    print("✅ INVENTUR BEREIT.")

if __name__ == "__main__":
    create_manifest()