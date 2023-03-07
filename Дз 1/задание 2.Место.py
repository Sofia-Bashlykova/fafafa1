x=int(input("Введите номер места: "))
if x%2==0 and x<=36:
    print('Вверхнее в купе')
elif x%2!=0 and x<=35:
    print ('Нижннее в купе')
elif x%2==0 and x>36:
    print('Вверхнее боковое')
else:
    print('Нижнее боковое')
