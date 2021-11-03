
import ctypes

class music():
    def __init__(self,sound):
        self.sound = sound
    def withoutmask(self):
        if self.sound == True :
            p = ctypes.windll.kernel32
            p.Beep(1046,700)
            
