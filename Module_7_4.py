

team1 = "Мастера кода"
team2 = "Волшебники данных"

def members(team1_num, team2_num):
    print('В команде %s количество участников: %s.' % (team1, 5))
    print('Итого сегодня участников: %s и %s' % (team1_num, team2_num))


def competition(score_1, score_2, team1_time, team2_time):
    tasks_total = score_1 + score_2
    time_avg = round((team1_time + team2_time) / (tasks_total),3)
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = f'Победа команды {team1}!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = f'Победа команды {team2}!'
    else:
        result = 'Ничья!'
    print('Команда {} решила задач: {}!'.format(team2,score_2))
    print('{} решили задачи за {} с!'.format(team2,team2_time))
    print(f'Команды решили {score_1} и {score_2} задач.')
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
    print(result)

members(5, 6)
competition(40,42,1552.512,2153.31451)