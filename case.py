from math import ceil

information = {'АИ-80': [1, 3], 'АИ-92': [3, 4, 2, 2], 'АИ-95': [3, 4], 'АИ-98':[3, 4]}
# первая - номер автомата вторая - кол во человек

base = []
with open('input.txt') as data:
    for line in data:
        line_list = list(line.split())
        base.append(line_list)

base_2 = []
for item in base:
    hours, minut = item[0].split(':')
    hours = int(hours)
    minut = int(minut)
    l = item[1]
    need_time = ceil(int(l) / 10)
    if (need_time + minut) >= 60:
        hours_base2 = hours + 1
        minut_base2 = 60 - (need_time + minut)
        if len(str(hours_base2)) != 2:
            hours_base2 = '0' + str(hours_base2)
            if len(str(minut_base2)) != 2:
                minut_base2= '0' + str(minut_base2)
        elif len(str(minut_base2)) != 2:
            minut_base2 = '0' + str(minut_base2)
            if len(str(hours_base2)) != 2:
                hours_base2= '0' + str(hours_base2)

        time_base2 = str(hours_base2) + ':' + str(minut_base2)
        base_2.append([time_base2, item[1], item[2]])

    elif (need_time + minut) < 60:
        hours_base2 = hours
        minut_base2 = need_time + minut
        if len(str(hours_base2)) != 2:
            hours_base2 = '0' + str(hours_base2)
            if len(str(minut_base2)) != 2:
                minut_base2= '0' + str(minut_base2)
        elif len(str(minut_base2)) != 2:
            minut_base2 = '0' + str(minut_base2)
            if len(str(hours_base2)) != 2:
                hours_base2= '0' + str(hours_base2)
        time_base2 = str(hours_base2) + ':' + str(minut_base2)
        base_2.append([time_base2, item[1], item[2]])

base_result = sorted(base_2 + base) #наш итоговый словарь

people_leave = 0
l_80 = 0
l_92 = 0
l_95 = 0
l_98 = 0

a1 = []
a2 = []
a3 = []

for car in base_result:
    AI = car[2]
    need_time_2 = str(ceil(int(car[1]) / 10))

    if AI == 'АИ-80':
        if len(a1) < 3:
            if car[1:] not in a1:
                print('В ' + car[0] + ' новый клиент: ' + car[0] + ' ' + AI + ' ' + car[1] + ' ' + need_time_2 + ' встал в очередь к автомату ' + '№1')
                a1.append(car[1:])
                l_80 += int(car[1])
            elif car[1:] in a1:
                a1.remove(car[1:])
                print('В ' + car[0] + ' клиент: ' + car[0] + ' ' + AI + ' ' + car[1] + ' ' + need_time_2 + ' заправил свой автомобиль и покинул АЗС.')
        elif len(a1) > 3:
            print('В ' + car[0] + ' клиент: ' + car[0] + ' ' + AI + ' ' + car[1] + ' ' + need_time_2 + 'не смог заправить автомобиль и покинул АЗС')
            people_leave += 1


    if AI == 'АИ-92':
        if car[1:] not in a2 and car[1:] not in a3:
            if len(a2) < 2:
                print('В ' + car[0] + ' новый клиент: ' + car[0] + ' ' + AI + ' ' + car[1] + ' ' + need_time_2 + ' встал в очередь к автомату ' + '№2')
                a2.append(car[1:])
                l_92 += int(car[1])

            elif len(a3) < 4:
                print('В ' + car[0] + ' новый клиент: ' + car[0] + ' ' + AI + ' ' + car[
                    1] + ' ' + need_time_2 + ' встал в очередь к автомату ' + '№3')
                a3.append(car[1:])
                l_92 += int(car[1])

            elif len(a2) > 2 and len(a3) > 4:
                print('В ' + car[0] + ' клиент: ' + car[0] + ' ' + AI + ' ' + car[
                    1] + ' ' + need_time_2 + 'не смог заправить автомобиль и покинул АЗС')
                people_leave += 1


        elif car[1:] in a2 or car[1:]  in a3:
            if car[1:] in a2:
                a2.remove(car[1:])
            elif car[1:] in a3:
                a3.remove(car[1:])
            print('В ' + car[0] + ' клиент: ' + car[0] + ' ' + AI + ' ' + car[
                    1] + ' ' + need_time_2 + ' заправил свой автомобиль и покинул АЗС.')


    if AI == 'АИ-95' or AI == 'АИ-98':

        if len(a3) < 4:
            if car[1:] not in a3:
                print('В ' + car[0] + ' новый клиент: ' + car[0] + ' ' + AI + ' ' + car[1] + ' ' + need_time_2 + ' встал в очередь к автомату ' + '№3')
                a3.append(car[1:])
                if AI == 'АИ-95':
                    l_95 += int(car[1])
                elif AI == 'АИ-98':
                    l_98 += int(car[1])
            elif car[1:] in a3:
                a3.remove(car[1:])
                print('В ' + car[0] + ' клиент: ' + car[0] + ' ' + AI + ' ' + car[1] + ' ' + need_time_2 + ' заправил свой автомобиль и покинул АЗС.')
        elif len(a3) > 3:
            print('В ' + car[0] + ' клиент: ' + car[0] + ' ' + AI + ' ' + car[1] + ' ' + need_time_2 + 'не смог заправить автомобиль и покинул АЗС')
            people_leave += 1

print('Количество литров, проданное за сутки по каждой марке бензина: ')
print('АИ-80 = ' + str(l_80))
print('АИ-92 = ' + str(l_92))
print('АИ-98 = ' + str(l_98))
print('АИ-95 = ' + str(l_95))
print('Общая сумма продаж за сутки: ' + str(l_80 + l_92 + l_95 + l_98))
print('На сумму: ' + str(float(l_80 * 38.95 + l_92 * 41.20 + l_95 * 44.45 + l_98 * 45.85)) + ' рублей.')
print('Количество клиентов, которые покинули АЗС не заправив автомобиль из-за «скопившейся» очереди = ' + str(people_leave))