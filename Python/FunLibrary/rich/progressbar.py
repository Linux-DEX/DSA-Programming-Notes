from rich.progress import track
import time

for step in track(range(100), description="Processing..."):
    time.sleep(0.05)

for step in track(range(100), description="Completing..."):
    time.sleep(0.05)