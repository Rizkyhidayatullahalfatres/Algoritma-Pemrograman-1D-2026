x = {2, 3, 4}

try :
    x.pop()
except KeyError as e:
    print("Error : ",e)