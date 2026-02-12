import os
import shutil

VAULT = os.path.expanduser("~/EMPIRE_PROJECTS/00_DaN_EMPIRE_VAULT_2026")
TRASH = ["untitled", "test2", "CHECK", "OH_OH_OH"]

def run_cleanup():
    print("🧹 Automatischer Cleanup startet...")
    for root, dirs, files in os.walk(VAULT):
        for f in files:
            if any(k in f.upper() for k in TRASH):
                trash_dir = os.path.join(VAULT, "99_SYSTEM_ARCHIV", "TRASH")
                os.makedirs(trash_dir, exist_ok=True)
                shutil.move(os.path.join(root, f), os.path.join(trash_dir, f))
                print(f"✅ Entfernt: {f}")
    print("✨ Vault ist blitzsauber.")

if __name__ == "__main__":
    run_cleanup()
