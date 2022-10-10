##list = [3,4]
##list += [2,3]
##print(list[2] *list[1])

darkNess= input('Give me a level of darkness between 0 - 5')

switch = ['on','off']
light = [0,1]

if darkNess >= '4':
    print(light[1])
    print('The switch is ' + switch[0])
elif darkNess == '3':
    print('Do you want me to put the switch' + ' ' + switch[0] + '?')
else:
    print('The switch is' + switch[1])
    print(light[0])