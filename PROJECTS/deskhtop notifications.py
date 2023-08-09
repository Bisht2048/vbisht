from plyer import notification
import time

# if __name__ == '__main__':
while True:
    notification.notify(title="***Take Rest ***",
                        message="its 1'o clock. Take Rest.",
                        timeout=5)
    time.sleep(10)