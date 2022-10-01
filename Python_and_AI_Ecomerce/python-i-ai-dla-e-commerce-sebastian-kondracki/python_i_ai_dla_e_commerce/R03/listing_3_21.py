import time
from rich.progress import track

max_step = 10
      
def hard_calculation(n):
    time.sleep(n)
    return True
      
for i in track(range(max_step), description="Processing..."):
    hard_calculation(i)