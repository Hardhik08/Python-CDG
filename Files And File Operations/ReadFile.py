fpath = r"ENTER YOUR FILE PATH"

with open(fpath,'r+') as file:
    content = file.read()
     
with open(fpath,'a') as file:
    file.seek(0)
    if content:
        file.write("ENTER YOUR TEXT\n")
        print("Write Complete")
       
    else:
        print("Content Present.")



