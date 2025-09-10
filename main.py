from openai import OpenAI
from ai import *

import pyautogui
import time
import pyperclip
# Samakami
n=input("Enter Reciever name:  ")

def is_last_message_from_sender(chat_history: str) -> bool:
    # Split into lines and remove empty ones
    lines = [line.strip() for line in chat_history.split("\n") if line.strip()]
    
    if not lines:
        return False  # No messages in history
    
    if lines[-1].startswith(n) or lines[-2].startswith(n) or lines[-3].startswith(n):
    
    # Check if last line starts with "You"
        return 1>0





# def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
#     # Split the chat log into individual messages
#     messages = chat_log.strip().split("/2024] ")[-1]
#     if sender_name in messages:
#         return True 
#     return False
    
    

    # Step 1: Click on the chrome icon at coordinates (1639, 1412)


time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo(592,206)
    pyautogui.dragTo(1855, 940, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(900, 976)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()
    

    if is_last_message_from_sender(chat_history):

        response = a(chat_history)
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(900, 976)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')