import pandas as pd

test = xl("Select Cell")
start = 0
end = 0
Flag = False
for x in range(0,len(test)):
    if test[x]=="(":
        Flag = True
        start = x+1
    if test[x]=="s" and Flag==True:
        end = x+1
    if test[x]==")" and Flag==True:
        break
test[start:end]
