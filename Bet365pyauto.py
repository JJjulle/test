#!/usr/bin/env python
# coding: utf-8

import time
import pyautogui
import subprocess

def press_cmd_space():
    """Simulate pressing Command + Space to open Spotlight."""
    pyautogui.keyDown('command')
    pyautogui.press('space')
    pyautogui.keyUp('command')
    time.sleep(1)  # Wait for Spotlight to open

def open_chrome():
    """Open Google Chrome using Spotlight or directly."""
    pyautogui.write('Google Chrome')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)  # Wait for Chrome to open

def open_website(url):
    """Open a website in Chrome."""
    pyautogui.write(url)
    pyautogui.press('enter')
    time.sleep(5)  # Wait for the page to load

def click_position(x, y):
    """Move the mouse to the specified (x, y) coordinates and click."""
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click()

def log_action(message):
    """Log action in a simple log file."""
    with open("action_log.txt", "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
    print(message)

def scroll_page(scroll_amount=-300):
    """Scroll the page."""
    pyautogui.scroll(scroll_amount)
    time.sleep(1)

def scroll_until_text_is_found_with_image(
    image_path, 
    max_scrolls=5, 
    scroll_amount=-300, 
    confidence=0.8
):
    """
    Scrolls the page until an image snippet is detected on screen
    or 'max_scrolls' is reached.
    """
    for i in range(max_scrolls):
        found = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if found:
            center_point = pyautogui.center(found)
            pyautogui.moveTo(center_point, duration=0.5)
            pyautogui.click()
            return True
        else:
            pyautogui.scroll(scroll_amount)
            time.sleep(1)
    return False

def save_current_page_as_webpage(filename="my_page"):
    """
    Saves the current page in Chrome as 'Web Page, Complete'.
    1. Press Cmd+S (Mac) to open Save dialog
    2. Type the filename
    3. Press Enter to save
    """
    # 1. Open Save As dialog
    pyautogui.keyDown('command')  # on Windows, use ctrl
    pyautogui.press('s')
    pyautogui.keyUp('command')
    time.sleep(2)  # wait for the Save As dialog
    
    # 2. Type the filename (and optionally clear existing text first)
    pyautogui.write(filename, interval=0.05)
    time.sleep(1)

    # 3. (Optionally set "Web Page, Complete" if needed.)
    #    This step is OS- and Chrome-dialog-specific. 
    # pyautogui.press('tab', presses=2, interval=0.25)
    # pyautogui.press('down', presses=2, interval=0.25)
    # pyautogui.press('enter')
    # time.sleep(1)

    # 4. Press Enter to confirm
    pyautogui.press('enter')
    time.sleep(2)  # let it save

def main():
    try:
        time.sleep(2)
        log_action("Opening Spotlight with Command + Space.")
        press_cmd_space()

        log_action("Opening Google Chrome.")
        open_chrome()

        log_action("Opening Bet365 website.")
        open_website('https://www.bet365.com/#/AC/B17/C20836572/D48/E972/F10')
        log_action("Waiting for Chrome and Bet365 to load.")

        # Example: Scroll down the page
        log_action("Scrolling down the page once.")
        scroll_page(scroll_amount=-300)

        # Example: Scroll until a text snippet is found
        # Make sure you have an image snippet "live_in_play.png" 
        # that shows the words you want to find on the screen.
        log_action("Scrolling until 'live_in_play.png' is found and clicking on it.")
        found_text = scroll_until_text_is_found_with_image(
            image_path='live_in_play.png',
            max_scrolls=10,
            scroll_amount=-300,
            confidence=0.8
        )

        if found_text:
            log_action("Found and clicked on the text snippet!")
        else:
            log_action("Could not find the text snippet within 10 scrolls.")

        # Example: Save the page
        log_action("Saving current page as 'bet365_page'.")
        save_current_page_as_webpage(filename="Bet365_current_pages/bet365_page")

        log_action("Completed the task successfully - continue from here")

    except Exception as e:
        log_action(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
