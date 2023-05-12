f = open('integers.txt','r')
sum = 0
cont = 0
for line in f:
    line = line.strip()
    if line != '':
        number = int(line)
        print(number)
        cont += 1
    sum += number
print ('El promedio es', sum/cont)
f.close()