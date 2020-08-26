from pynput.keyboard import Key, Controller
import time
import keyboard

keyboards = Controller()

print('''press key Backspace to continue and
remember ctrl + c to exit program''')
while True:
    keyboard.wait(Key.backspace)
    print("Starting Bot")
    while True:
        keyboards.press(Key.enter)
        keyboards.release(Key.enter)

        time.sleep(0.2)

        keyboards.press(Key.enter)
        keyboards.release(Key.enter)

        time.sleep(0.2)

        keyboards.press(Key.enter)
        keyboards.release(Key.enter)

        time.sleep(2.5)

        keyboards.press(Key.enter)
        keyboards.release(Key.enter)

        keyboards.press(Key.enter)
        keyboards.release(Key.enter)

        keyboards.press(Key.esc)
        keyboards.release(Key.esc)


