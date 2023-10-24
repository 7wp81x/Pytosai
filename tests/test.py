import time
import sys

def welcome_animation():
    frames = [
        " Welcome 7wp     ",
        " Welcome 7wp .   ",
        " Welcome 7wp ..  ",
        " Welcome 7wp ... ",
        " Welcome 7wp ..  ",
        " Welcome 7wp .   ",
    ]
    for x in range(0,4):
        for i in range(232,255):
            frame = frames[i % len(frames)]
            sys.stdout.write(f"\r\033[38;5;{i}m{frame}")
            sys.stdout.flush()
            time.sleep(0.05)

if __name__ == "__main__":
    welcome_animation()
    print()
