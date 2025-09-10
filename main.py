from openai import OpenAI
from ai import *

import pyautogui
import time
import pyperclip

n=input("Enter Reciever name:  ")

def is_last_message_from_sender(chat_history: str) -> bool:
   
    lines = [line.strip() for line in chat_history.split("\n") if line.strip()]
    
    if not lines:
        return False  
    
    if lines[-1].startswith(n) or lines[-2].startswith(n) or lines[-3].startswith(n):
    

        return 1>0







time.sleep(1)  
while True:
    time.sleep(5)
    pyautogui.moveTo(592,206)
    pyautogui.dragTo(1855, 940, duration=2.0, button='left')  

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2) 
    pyautogui.click(900, 976)

    chat_history = pyperclip.paste()
    

    if is_last_message_from_sender(chat_history):

        response = a(chat_history)
        pyperclip.copy(response)

        pyautogui.click(900, 976)
        time.sleep(1)

  
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1) 
        pyautogui.press('enter')
