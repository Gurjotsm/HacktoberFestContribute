import time
import sympy as sp
start_time = time.time()
prime_list = []
required_list = []
for i in range(1000, 1000001):
    if sp.isprime(i):
        prime_list.append(i)
list_length = len(prime_list)
for j in range(list_length):
    for char in str(prime_list[j]):
        if str(prime_list[j]).count(char) == 3:
            length = len(str(prime_list[j]))
            if char != str(prime_list[j])[length-1]:
                required_list.append(prime_list[j])
                break
    number = str(prime_list[j])
    for char in number:
        if number.count(char) == 3:
            n = []
            for i in range(10):
                a1 = number.replace(char, str(i))
                a = int(a1)
                if sp.isprime(a) and a1[0] != '0':
                    n.append(a)
            if len(n) == 8:
                print("Smallest Prime no required: ", n[0])
                print("--- %s seconds ---" % (time.time() - start_time))
                exit(0)
