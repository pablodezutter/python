"""weight= input(int())
height = input(float())
result = float(weight/(height ** 2))"""

weight = input()
height = input()
result = float(weight/ float(height **2))


if result <=  18.5:
	print('underweight')
elif result >= 18.5 and result < 25:
	print('normal')
elif result >= 25 and result <30:
	print('overweight')
else:
	print('obese')