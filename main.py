import time
import sys
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def progress_bar(duration, message):
    print(f"\n\033[96m{message}\033[0m")
    bar_length = 50
    
    for i in range(bar_length + 1):
        percent = (i / bar_length) * 100
        filled = '█' * i
        empty = '░' * (bar_length - i)
        sys.stdout.write(f'\r\033[92m[{filled}{empty}] {percent:.0f}%\033[0m')
        sys.stdout.flush()
        time.sleep(duration / bar_length)
    
    print()

def main():
    if os.name == 'nt':
        os.system('title VRModz APK')
    
    clear()
    
    print("\033[95m")
    print("╔════════════════════════════════════════════════════╗")
    print("║                                                    ║")
    print("║              ██╗   ██╗██████╗ ███╗   ███╗          ║")
    print("║              ██║   ██║██╔══██╗████╗ ████║          ║")
    print("║              ██║   ██║██████╔╝██╔████╔██║          ║")
    print("║              ╚██╗ ██╔╝██╔══██╗██║╚██╔╝██║          ║")
    print("║               ╚████╔╝ ██║  ██║██║ ╚═╝ ██║          ║")
    print("║                ╚═══╝  ╚═╝  ╚═╝╚═╝     ╚═╝          ║")
    print("║                                                    ║")
    print("║                  VRModz APK v1.0                   ║")
    print("║                                                    ║")
    print("╚════════════════════════════════════════════════════╝")
    print("\033[0m")
    
    code = input("\n\033[93mEnter code: \033[0m").strip().upper()
    
    if code != "QIIX":
        print("\n\033[91m╔════════════════════════════════════════════════════╗")
        print("║  ❌ ERROR: Invalid code! This code does not exist. ║")
        print("╚════════════════════════════════════════════════════╝\033[0m\n")
        sys.exit(1)
    
    print("\n\033[92m✓ Code accepted!\033[0m")
    time.sleep(0.5)
    
    progress_bar(3, "Searching for Quest...")
    
    progress_bar(8, "Meta Quest 3 found! Downloading APK...")
    
    print("\n\033[92m╔════════════════════════════════════════════════════╗")
    print("║         ✓ APK successfully downloaded!             ║")
    print("╚════════════════════════════════════════════════════╝\033[0m\n")
    
    input("\033[96mPlaytime: 00:37:46\033[0m\n")

if __name__ == "__main__":
    main()
