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

i=0

while(clipboard_content):  # While there is content in the clipboard
    
    # Switch to Firefox
    pg.hotkey("alt", "tab")
    time.sleep(0.2)


    if(i==0):
        #home
        pg.press("home")
            
        # click product
        pg.click(x=1004, y=610)  
        time.sleep(0.2)
        # Page Down
        pg.press("pgdn")
        time.sleep(0.2)
        # Click change
        pg.click(x=1506, y=531)  
        time.sleep(0.2)


    #Click the input box
    pg.click(x=686, y=597)
    pg.click(x=686, y=597)    
    time.sleep(0.2)

      
    # Paste the copied value
    pg.hotkey("ctrl", "v")
    time.sleep(0.1)

    pg.press("enter")
    time.sleep(1)

    # Click the "Add Value" button 
    pg.click(x=1075, y=650)  
    time.sleep(0.2)
    i=i+1

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
    if i == 40 or not clipboard_content:
        time.sleep(1)
        i = 0
        # Click save changes
        pg.click(x=1580, y=1085)
        pg.click(x=1581, y=1084)
        time.sleep(3)

        

    


