from recoil_manager import RecoilManager
import win32api
import win32con
import threading
import time 

def listen_input(manager):
    while True:
        if win32api.GetAsyncKeyState(win32con.VK_F1) & 0x8000:  
            manager.activate_recoil()
        elif win32api.GetAsyncKeyState(win32con.VK_F2) & 0x8000:  
            manager.deactivate_recoil()

def monitor_shooting(manager):
    while True:
        if manager.shooting:
            print("Sedang menembak...")
        time.sleep(0.1)

def main():
    manager = RecoilManager()
    manager.start()

    input_thread = threading.Thread(target=listen_input, args=(manager,))
    input_thread.start()

    shooting_thread = threading.Thread(target=monitor_shooting, args=(manager,))
    shooting_thread.start()

    input_thread.join()
    shooting_thread.join()

if __name__ == "__main__":
    main()
