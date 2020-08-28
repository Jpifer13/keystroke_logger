from pynput.keyboard import Key, Controller
import time


class KeyEmulator():

    def __init__(self, timeout: int=5, key: Key=Key.insert):
        """
        This class will press a button on keyboard, key, and then sleep for 
        n amount of minutes, timeout.

        Args:
            timeout (int, optional): [Time between key presses in minutes]. Defaults to 5.
            key (str, optional): [Key that is automatically pressed]. Defaults to None.
        """
        self.timeout=timeout
        self.key=key

    def run(self):
        keyboard = Controller()
        running = True
        while running:
            keyboard.press(self.key)
            print(str(self.key))
            time.sleep(self.timeout*60)


if __name__ == "__main__":
    emulator = KeyEmulator(timeout=5)
    emulator.run()