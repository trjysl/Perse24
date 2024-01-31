#task 1

x = int(input())
y = int(input())
z = int(input())


total_cost = ( x + (12*y*z))

print(total_cost)

#task 2

given = int(input())
cost = int(input())

rides = ( given//cost )

print(rides)

#task 3

encrypted = input('')
front = encrypted[:2]
back = encrypted[2:]

decrypted = back + front

print(decrypted)
