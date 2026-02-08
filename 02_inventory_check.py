# 2026-02-08_Inventory_Check_v1
import os
import json

VAULT = r"C:\Users\Danny\Desktop\00_DaN_EMPIRE_VAULT_2026"

def create_inventory():
    print("📊 DaN OS: Erstelle Inventur-Bericht...")
    report = {}

    for item in os.listdir(VAULT):
        item_path = os.path.join(VAULT, item)
        if os.path.isdir(item_path):
            report[item] = {}
            for sub in os.listdir(item_path):
                sub_path = os.path.join(item_path, sub)
                if os.path.isdir(sub_path):
                    count = len(os.listdir(sub_path))
                    report[item][sub] = count
                else:
                    report[item]["LOSE_DATEIEN"] = report[item].get("LOSE_DATEIEN", 0) + 1

    with open("vault_inventory.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
    
    print("✅ Inventur abgeschlossen. Datei 'vault_inventory.json' wurde erstellt.")

if __name__ == "__main__":
    create_inventory()