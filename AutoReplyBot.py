import pyautogui
import time
import pyperclip
import google.generativeai as genai
import re
from openai import OpenAI

genai.configure(api_key="AIzaSyCMNwO-7FgxvUgVEwmxNQx-L6QNZ6__dK8")


def is_last_message_from_sender(chat_log, sender_name="Mama."):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True
    return False

    # Step 1: Click on the chrome icon at coordinates (1639, 1412)


pyautogui.click(1009, 1055)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo(685, 240)
    pyautogui.dragTo(1288, 940, duration=2.0)  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(1337, 837)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        model = genai.GenerativeModel("gemini-1.5-flash")
        chat = model.start_chat(
            history=[
                {"role": "user", "parts": chat_history},
                {"role": "model", "parts": "You are a person named Afraz who speaks Urdu as well as english. He is from Pakistan and is a coder. You analyze chat history and respond like human Afraz  Write simple , small, and humanly reply of the message"},
                # {"role": "model", "parts": "Do not start like this [02:04, 10/09/2024] Syed Afraz: "}
            ]
        )
        response = chat.send_message(chat_history)
        text_message = response._result.candidates[0].content.parts[0].text



        cleaned_message = re.sub(r'\[\d{2}:\d{2}, \d{2}/\d{2}/\d{4}\] [^:]+: ', '', text_message).strip()

        pyperclip.copy(cleaned_message)

        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(954, 971)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')