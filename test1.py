counter = 0

for i in range(100):
    for j in range(4):
        print(i % (j+1))
        counter += 1
        print("This is loop " + str(counter))

