import time
import os

print("os and time work!")
#this pings it with a mb of data
data = os.urandom(1024 * 1024)
print(f"Successfully created {len(data) / (1024*1024):.1f} MB of data")
