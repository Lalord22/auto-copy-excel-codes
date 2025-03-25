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
adjustChangeButton = 0
adjustBar = 0

# Switch to Firefox
pg.hotkey("alt", "tab")
time.sleep(0.2)

while(clipboard_content):  # While there is content in the clipboard
    
    


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
        pg.click(x=1506, y=531-adjustChangeButton)  
        time.sleep(0.2)


    #Click the input box
    pg.click(x=686, y=597-adjustBar)
    pg.click(x=686, y=597-adjustBar)    
    time.sleep(0.2)

      
    # Paste the copied value
    pg.hotkey("ctrl", "v")
    time.sleep(0.1)

    pg.press("enter")
    time.sleep(1)

    # Click the "Add Value" button 
    pg.click(x=1075, y=650-adjustBar)  
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

    # Switch to Firefox
    pg.hotkey("alt", "tab")
    time.sleep(0.2)


    # If gets to 20 then reset to 0, this is when it should save draft
    if i == 10 or not clipboard_content:
        time.sleep(1)
        i = 0
        
        # Click save changes
        pg.click(x=1580, y=1085-adjustBar)
        pg.click(x=1581, y=1084-adjustBar)
        time.sleep(3)

        pg.click(x=2247, y=677)

        pg.press("end")
        time.sleep(1)

        adjustChangeButton = 123
        adjustBar = 113

        # Click "Save Draft" button in Firefox (adjust coordinates)
        pg.click(x=2185, y=1300)  
        time.sleep(3)

        

    


