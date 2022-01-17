import numpy as np


def random_predict(number: int = 1) -> int:

    count = 0
    min_border = 1  # нижняя граница интервала поиска
    max_border = 101  # верхняя граница интервала поиска

    while True:
        count += 1
        # задаём среднее значение
        predict_number = (min_border + max_border) // 2
        if predict_number < number:  # если число меньше загаданного
            min_border = predict_number  # увеличиваем нижнюю границу 
        elif predict_number > number:  # если число больше загаданного 
            max_border = predict_number  # уменьшаем верхнюю границу
        else:
            break  # выходим из цикла, если угадали
    
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []  # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для вопроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

# RUN
if __name__ == '__main__':
    # запуск функции
    score_game(random_predict)