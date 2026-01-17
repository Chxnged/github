import time
import sys

print("Beta not released")

for i in range(5, 0, -1):
    sys.stdout.write(f'\r{i}')
    sys.stdout.flush()
    time.sleep(1)

print("\n")
sys.exit(0)
