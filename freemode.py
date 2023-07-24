from pymycobot.mycobot import MyCobot
import time
import keyboard

mc = MyCobot('/dev/ttyAMA0', 115200)
time.sleep(5)
print("> releasing all servos!")
mc.release_all_servos()
while True:
    print(mc.get_angles())
    time.sleep(2)    
    
