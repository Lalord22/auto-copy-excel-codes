import pyautogui as pg

print("Move your mouse to the button and wait for the coordinates...")
pg.sleep(5)  # Gives you time to position your mouse
x, y = pg.position()
print(f"Mouse Position: x={x}, y={y}")
