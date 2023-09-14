import pyautogui as gui

from PIL import Image, ImageGrab
import time
import math
from pynput.keyboard import Key, Listener
import threading


def get_pixel(image, x, y):
     
    px = image.load()
    return px[x, y]
 
monitor_width, monitor_hight = 1920,1080
screenshot =ImageGrab.grab(xdisplay="", bbox=(0,0,monitor_width,monitor_hight)) 
#screenshot.show()
gui.moveTo(10,650)
gui.click()
gui.press("space")
#gui.click()

exit_signal = threading.Event()

def on_press(key):
    global running
    try:
        if key == Key.esc:                    
            print("Dingle Dongle")
            exit_signal.set()
    except AttributeError:
        # Some special keys like 'Ctrl' and 'Space' don't have a direct attribute
        print(f"The key '{key}' is pressed.")




def main():
    counter = 0
    normal_dino_color = (83, 83, 83)
    reversed_dino_color = (172, 172, 172)
    #background_color_dict = {(255,255,255):(83, 83, 83),(254, 254, 254): (254, 254, 254), (252, 252, 252): (252, 252, 252),(251, 251, 251): (84, 84, 84),(250, 250, 250): (250, 250, 250),(248, 248, 248): (248, 248, 248), (246, 246, 246): (86, 86, 86), (244, 244, 244): (87, 87, 87), (241, 241, 241): (88, 88, 88), (238, 238, 238): (89, 89, 89), (234, 234, 234): (90, 90, 90), (229, 229, 229): (92, 92, 92), (224, 224, 224): (94, 94, 94), (219, 219, 219): (96, 96, 96), (208, 208, 208): (99, 99, 99), (200, 200, 200): (102, 102, 102), (191, 191, 191): (105, 105, 105), (181, 181, 181): (109, 109, 109), (169, 169, 169): (113, 113, 113), (155, 155, 155): (118, 118, 118), (141, 141, 141): (123, 123, 123), (125, 125, 125): (128, 128, 128), (110, 110, 110): (134, 134, 134), (95, 95, 95): (139, 139, 139), (81, 81, 81): (144, 144, 144), (69, 69, 69): (148, 148, 148), (64, 64, 64): (150, 150, 150), (49, 49, 49): (155, 155, 155), (41, 41, 41): (158, 158, 158), (34, 34, 34): (160, 160, 160), (28, 28, 28): (162, 162, 162), (23, 23, 23): (164, 164, 164), (19, 19, 19): (165, 165, 165), (15, 15, 15): (167, 167, 167), (12, 12, 12): (168, 168, 168), (9, 9, 9): (169, 169, 169),(8, 8, 8): (169, 169, 169), (7, 7, 7): (170, 170, 170), (5, 5, 5): (170, 170, 170), (3, 3, 3): (171, 171, 171), (2, 2, 2): (171, 171, 171), (1, 1, 1): (172, 172, 172), (0, 0, 0): (172, 172, 172)}
    background_color_dict = {(255,255,255):(83, 83, 83), (251, 251, 251): (84, 84, 84), (246, 246, 246): (86, 86, 86), (244, 244, 244): (87, 87, 87), (241, 241, 241): (88, 88, 88), (238, 238, 238): (89, 89, 89), (234, 234, 234): (90, 90, 90), (229, 229, 229): (92, 92, 92), (224, 224, 224): (94, 94, 94), (219, 219, 219): (96, 96, 96), (208, 208, 208): (99, 99, 99), (200, 200, 200): (102, 102, 102), (191, 191, 191): (105, 105, 105), (181, 181, 181): (109, 109, 109), (169, 169, 169): (113, 113, 113), (155, 155, 155): (118, 118, 118), (141, 141, 141): (123, 123, 123), (125, 125, 125): (128, 128, 128), (110, 110, 110): (134, 134, 134), (95, 95, 95): (139, 139, 139), (81, 81, 81): (144, 144, 144), (69, 69, 69): (148, 148, 148), (64, 64, 64): (150, 150, 150), (49, 49, 49): (155, 155, 155), (41, 41, 41): (158, 158, 158), (34, 34, 34): (160, 160, 160), (28, 28, 28): (162, 162, 162), (23, 23, 23): (164, 164, 164), (19, 19, 19): (165, 165, 165), (15, 15, 15): (167, 167, 167), (12, 12, 12): (168, 168, 168), (9, 9, 9): (169, 169, 169),(8, 8, 8): (169, 169, 169), (7, 7, 7): (170, 170, 170), (5, 5, 5): (170, 170, 170), (3, 3, 3): (171, 171, 171), (2, 2, 2): (171, 171, 171), (1, 1, 1): (172, 172, 172), (0, 0, 0): (172, 172, 172)}


    while not exit_signal.is_set() :
        counter += 0.003  
        #print(counter)
        screenshot =ImageGrab.grab(xdisplay="", bbox=(0,0,monitor_width,monitor_hight))
        background_color = get_pixel(screenshot,250,250) 
        
        if background_color in background_color_dict:
            dino_color = background_color_dict[background_color]
        #if background_color == (255,255,255):
        #    dino_color = normal_dino_color

        #else:
        #    dino_color = reversed_dino_color


        pixels_to_check = []
        counter_pixel_to_check = [] # Pixel used to check if there is a flying bird
        for i in range(300+int(counter)):
            current_pixel = get_pixel(screenshot,250+counter+i,650)
            counter_pixel = get_pixel(screenshot,250+counter+i,570)
            pixels_to_check.append(current_pixel)
            counter_pixel_to_check.append(counter_pixel)


        if dino_color in pixels_to_check:
            gui.press("space")

        elif dino_color in counter_pixel_to_check:
            print("Vogel")
            gui.keyDown("down")
            with gui.hold("down"):
                gui.sleep(0.3)
                gui.keyUp("down")



# Create a listener to monitor key presses in a separate thread
keyboard_listener = Listener(on_press=on_press)
keyboard_thread = threading .Thread(target=keyboard_listener.run)

# Create a thread for the second while loop
second_loop_thread = threading.Thread(target=main)

# Start both threads
keyboard_thread.start()
second_loop_thread.start()

# Wait for both threads to complete (you can modify this as needed)
keyboard_thread.join()
second_loop_thread.join()                            