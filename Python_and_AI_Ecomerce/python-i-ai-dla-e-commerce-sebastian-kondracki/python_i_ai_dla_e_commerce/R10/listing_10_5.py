def f_generator(i):
    j = 10
    for i in range(i):
        j += 10
        print("j =", j)
        yield j + i
      
for k in f_generator(3):
    print("k =", k)