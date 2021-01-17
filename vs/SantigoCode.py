from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MController
import time

mouse = MController()
keyboard = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

time.sleep(2)

# Set pointer position
mouse.position = (-30050, 200000)
print('Now we have moved it to {0}'.format(
    mouse.position))

time.sleep(2)

mouse.press(Button.left)
mouse.release(Button.left)

time.sleep(2)

keyboard.press('c')
keyboard.release('c')
time.sleep(0.5)
keyboard.press('o')
keyboard.release('o')
time.sleep(0.5)
keyboard.press('m')
keyboard.release('m')
time.sleep(0.5)
keyboard.press('m')
keyboard.release('m')
time.sleep(0.5)
keyboard.press('a')
keyboard.release('a')
time.sleep(0.5)
keyboard.press('n')
keyboard.release('n')
time.sleep(0.5)
keyboard.press('d')
keyboard.release('d')

keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(0.5)

keyboard.type('pkgmgr /iu:"TelnetClient')

time.sleep(0.5)

keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(0.5)

keyboard.press('t')
keyboard.release('t')
time.sleep(0.5)
keyboard.press('e')
keyboard.release('e')
time.sleep(0.5)
keyboard.press('l')
keyboard.release('l')
time.sleep(0.5)
keyboard.press('n')
keyboard.release('n')
time.sleep(0.5)
keyboard.press('e')
keyboard.release('e')
time.sleep(0.5)
keyboard.press('t')
keyboard.release('t')
time.sleep(0.5)

keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(0.5)

keyboard.press('o')
keyboard.release('o')

keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(1)

keyboard.type('towel.blinkenlights.nl')

time.sleep(1)

keyboard.press(Key.enter)
keyboard.release(Key.enter)



















