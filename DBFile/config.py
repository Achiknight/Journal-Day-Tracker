# This file takes your Txt config and makes them into python variables
# I did this solely bcs i forgot how to use file handeling




fg = ""
hv = ""
txt = ""
brd = ""
Ft1 = ""
Ft2 = ""

short = {"background_color": "fg", "hover_color": "hv", "text_color": "txt", "border_color": "brd", "Font_style1": "Ft1", "Font_style2": "Ft2"}
bruh =  {"background_color": "fg", "hover_color": "hv", "text_color": "txt", "border_color": "brd", "Font_style1": "Ft1", "Font_style2": "Ft2"}




file = open(r"config.txt","r")
lines = [line.strip() for line in file.readlines()]


for line in lines:
    
    if line.startswith("#") or not line:
        continue
    line = line.split("=",1)
    key = str(line[0]).strip()
    if key in short.keys():
        value = str(line[1]).strip()
        
        globals()[bruh[key]] = value
        #print("works")

#print(fg)

        
