#full screen messenger
import pyautogui
import time 
#have a couple seconds to switch to full screen messenger
#time.sleep(2)
def texter(phoneNumber:str, message:str):
    pyautogui.click(400,400,duration=0.25)
    pyautogui.hotkey('command','n')
    pyautogui.write(phoneNumber)
    pyautogui.click(600,875,duration=0.25)
    pyautogui.write(message)
    pyautogui.hotkey('enter')