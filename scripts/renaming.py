import os

my_files = os.listdir()

this_file = os.path.basename(__file__)

for i, file in enumerate(my_files):
    if file == this_file:
        continue
    os.rename(file, f"sos_{i}.txt")