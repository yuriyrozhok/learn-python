import random
from datetime import datetime
questions = 3
time_1q = 15
ca=0
total_time = 0
input('Когда будете готовы, нажмите ENTER')
for q in range(1, questions + 1):
    x=random.randint(10,50)
    y=random.randint (10,50)
    z = x + y
    print('********* ВОПРОС:', q)
    t1 = datetime.now()
    u = int(input('{0}+{1}=? '.format(x,y)))
    t2 = datetime.now()
    t = (t2 - t1).seconds
    total_time = total_time + t
    #z = input(str(x)+'+'+str(y)+'=?')
    if z == u :
        print('правильно!')
        ca=ca+1
    else:

        print('ошибка!')
    print('Правильный ответ:')
    print ('{0}+{1}={2}'.format(x,y,z))
    print('Время: {0} сек.'.format(t))
    q = q + 1
points = time_1q * ca - total_time
print('---------------------------------')
print('правильных ответов:', ca)
print('общее время: {0} сек.'.format(total_time))
print('Вы получаете {0} очок из {1}'.format(points, time_1q * questions))

