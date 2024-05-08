import time
import win32api
import win32con
import threading

class RecoilManager:
    def __init__(self):
        self.recoil_active = False
        self.shooting = False

    def activate_recoil(self):
        self.recoil_active = True
        print("Recoil Activated!")

    def deactivate_recoil(self):
        self.recoil_active = False
        print("Recoil Deactivated!")

    def recoil_handler(self):
        while True:
            if win32api.GetKeyState(win32con.VK_LBUTTON) & 0x8000:  
                if self.recoil_active:
                    self.shooting = True
                    print("Mouse ditekan - Menahan recoil ke bawah")
                    self.move_mouse_down()  
                else:
                    self.shooting = False
            else:
                self.shooting = False
            time.sleep(0.1)

    def move_mouse_down(self):
        current_x, current_y = win32api.GetCursorPos()
        new_y = current_y + 10
        win32api.SetCursorPos((current_x, new_y))

    def start(self):
        recoil_thread = threading.Thread(target=self.recoil_handler)
        recoil_thread.start()
