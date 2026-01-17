import time
import sys

print("\033[91mBeta not released\033[0m\n")

for i in range(5, 0, -1):
    sys.stdout.write(f'\rClosing in {i} seconds...')
    sys.stdout.flush()
    time.sleep(1)

print("\n")
sys.exit(0)
