N = int(input('Students? '))
K = int(input('Apples? '))
korzina = 0
apple = K//N
korzina = K%N
print('По ' + str(apple) + ' яблок каждый студент')
print('В корзине осталось ' + str(korzina) + ' яблок')