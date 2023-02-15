for i in range(8):
    for j in range(8):
        if (i+j)%2:
            print("█", end="")
        else:
            print(" ", end="")
    print("") # nová řádka