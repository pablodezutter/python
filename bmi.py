"""weight= input(int())
height = input(float())
result = float(weight/(height ** 2))"""

weight = float(input())
height = float(input())
result = weight /( height**2 )


if result <= 18.5:
	print('underweight',result)
elif result >= 18.5 and result < 25:
	print('normal', result)
elif result >= 25 and result <30:
	print('overweight', result)
else:
	print('obese',result)