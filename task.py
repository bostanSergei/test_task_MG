from datetime import datetime, timedelta


busy = [
    {'start': '10:30', 'stop': '10:50'},
    {'start': '18:40', 'stop': '18:50'},
    {'start': '14:40', 'stop': '15:50'},
    {'start': '16:40', 'stop': '17:20'},
    {'start': '20:05', 'stop': '20:20'}
]

# индекс для движения по массиву закрытых слотов. Массив предварительно отсортируем
pattern, index = '%H:%M', 0
busy.sort(key=lambda data: datetime.strptime(data['start'], pattern))

start_time = datetime.strptime('09:00', pattern)
step_time = timedelta(minutes=30)

result_list = []

while start_time + step_time < datetime.strptime('21:00', pattern):
    end_time = start_time + step_time

    # сразу формируем словарь, который при удачном раскладе попадет в итоговый список
    curr_dict = {
        'start': datetime.strftime(start_time, pattern),
        'stop': datetime.strftime(end_time, pattern)
    }

    # не забываем выполнить проверку на выход за пределы списка закрытых слотов
    if index < len(busy):
        if end_time <= datetime.strptime(busy[index]['start'], pattern):
            result_list.append(curr_dict)
            start_time += step_time
        else:
            start_time = datetime.strptime(busy[index]['stop'], pattern)
            index += 1
    else:
        result_list.append(curr_dict)
        start_time += step_time

# выводим итоговый результат, разделяя элементы списка переносом на новую строку
print(*result_list, sep='\n')

# PS в моих репозиториях можно посмотреть другие тестовые задания и задачи с leetcode, которые я решал)
