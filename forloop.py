cart = [15, 42, 120, 9, 5, 380]
discount = int(input())
total = 0 

for y in cart:
   total = total + (y -(y * discount / 100))
print(total)
