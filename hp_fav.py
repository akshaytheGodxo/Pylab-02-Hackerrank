#This is the solution no. 2 for the GLA pylab02 contest held at hackerank

n = int(input("Enter the key : "))

l = []
a = 1
b = 2
new_value = 0
i = 1
while i < n*2:
    if i%3 == 0:
        i = i+1
    elif i//10 == 3:
        i = i+1

    else:
        l.append(i)
        i = i+1

#Optional == print(l) (Just to make sure)
index = n - 1

print(l[index])
#Enjoy :D
