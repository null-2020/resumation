from lib.main import run
import os

import platform

VERSION = "0.0.0"

if __name__ == "__main__":
    try:
        os.system('cls||clear')
        print("Starting Program...")
        operating_system = platform.system()
        print(f"Operating System: {operating_system}")
        run(VERSION)
    except KeyboardInterrupt:
        print("Process killed by user")
