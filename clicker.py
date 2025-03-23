import pyautogui as pg
import time
import pyperclip

print("Move your mouse to the excel to start...")
# Wait 10 seconds so you can switch to Excel before the script starts
time.sleep(10)
 # Copy selected cell
pg.hotkey("ctrl", "c")
time.sleep(0.2)

# Get clipboard content
clipboard_content = pyperclip.paste().strip()

while(clipboard_content):  # While there is content in the clipboard

    i=0

    # Stop if the copied content is empty
    if not clipboard_content:
        print("Empty cell detected. Stopping...")
        break

    # Switch to Firefox
    pg.hotkey("alt", "tab")
    time.sleep(0.2)

    # Page Down
    #pg.press("pgdn")

    # Click the "Input box button twice" button (adjust these coordinates)
    pg.click(x=1153, y=966)  # Replace with actual button coordinates
    pg.click(x=1153, y=966)  # Replace with actual button coordinates
    time.sleep(0.2)

    # Paste the copied value
    pg.hotkey("ctrl", "v")
    time.sleep(0.2)

    # Click the "Add Value" button (adjust these coordinates)
    pg.click(x=1386, y=961)  # Replace with actual button coordinates
    time.sleep(0.2)

    # Switch back to Excel
    pg.hotkey("alt", "tab")
    time.sleep(0.2)

    # Move down one cell in Excel
    pg.press("down")
    time.sleep(0.2)

    # Copy selected cell
    pg.hotkey("ctrl", "c")
    time.sleep(0.2)

    clipboard_content = pyperclip.paste().strip()

    # If gets to 20 then reset to 0, this is when it should save draft
    if(i==20):
        i=0

# Click "Save Draft" button in Firefox (adjust coordinates)
#pg.hotkey("alt", "tab")
#time.sleep(1)
#pg.click(x=600, y=500)  # Replace with actual coordinates
#print("Process completed!")
