fpath = r"C:\Users\hardh\Downloads\Actual_Import_3678_2026-09-23.csv"

with open(fpath,'r+') as file:
    content = file.read()
     
with open(fpath,'a') as file:
    file.seek(0)
    if content:
        file.write("Hi, Vamshi!\n")
        print("Write Complete")
       
    else:
        print("Content Present.")



