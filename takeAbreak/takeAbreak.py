import ctypes
import time


def main():

    interval = int(raw_input("Enter time interval(in minutes): "))
    interval *= 60
    while True:
        time.sleep(interval)
        ctypes.windll.user32.MessageBoxA(0, "You've been sitting for "+str(interval/60)+ " minute(s). Time to take a break and take a walk! NOW!", "Ibrahim says:", 0)



if __name__ == '__main__':
    main()
