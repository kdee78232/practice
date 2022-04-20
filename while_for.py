food=('fish','steak','meatloaf','tuna')
for variable in food:
    print(variable)


number=344
val=input('Enter your number:\n ')
if int(val) == 344:
    print('you are correct')
elif int(val)<= 344:
    print('You are wrong')
else:
    print('try again')


for x in range(1,8):
    print(x)


for x in range(1,45,8):
    print(x)



while True:
    string=input('Enter your work status.\nWhat is your status  ')
    if string=='new hire':
        break
    print('try again')
print(f'Welcome Aboard')



attempts=1
while (attempts < 20):
    print('tries count is> ',attempts)
    attempts=attempts+1
else:
    print('you are done')







dataset=[1,2,3,4,5,6,6,7]
for i in dataset:
    print(i)
print('"You are number 1"')








while True:
    n=56
    numb=int(input('Enter you number: \nType your number  '))
    if numb == 56:
        break
    print(f'numer is  {numb}')
print('you are done')
