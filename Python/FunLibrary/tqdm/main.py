# Instantly make your loops show a smart progress meter - just wrap any iterable with tqdm(iterable), and you’re done!

import time
from tqdm import tqdm, trange

for i in tqdm(range(100)):
    time.sleep(0.1)

for i in tqdm(range(100), desc="1st loop"):
    time.sleep(0.1)

text = ""
for char in tqdm(["a", "b", "c", "d"], desc="concat strings"):
    time.sleep(0.25)
    text = text + char

print('text value -',text)

# trange(i) is a special optimised instance of tqdm(range(i)):
for i in trange(100):
    time.sleep(0.01)

# Instantiation outside of the loop allows for manual control over tqdm(): 
pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    time.sleep(0.25)
    pbar.set_description("Processing %s" % char)

pbar = tqdm(total=100)
for i in range(10):
    time.sleep(0.1)
    pbar.update(10)
pbar.close()