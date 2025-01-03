def вычислить_полином_жегалкина(таблица_истинности):
    
    n = len(таблица_истинности)  # Длина таблицы истинности
    коэффициенты = таблица_истинности[:]  # Копируем таблицу истинности для вычислений
    
    # Метод конечных разностей
    for i in range(1, n):  # Итерация по строкам таблицы
        for j in range(n - i):  # Пересчет коэффициентов
            коэффициенты[j] ^= коэффициенты[j + 1]  # Операция XOR для обновления коэффициентов
    
    # Определение переменных
    количество_переменных = len(bin(n - 1)) - 2  # Количество переменных (2^k = n)
    переменные = [f'x{i + 1}' for i in range(количество_переменных)]
    полином = []
    
    # Построение полинома на основе коэффициентов
    for i, c in enumerate(коэффициенты):
        if c == 1:  # Если коэффициент равен 1, добавляем член в полином
            член = []
            for j in range(количество_переменных):
                if i & (1 << j):  # Проверяем, входит ли переменная в член
                    член.append(переменные[j])
            полином.append(' & '.join(член) if член else '1')  # "1" для константного члена
    
    return ' ^ '.join(полином) if полином else '0'  # XOR представлен как ^

# Пример использования
if __name__ == "__main__":
    # Таблица истинности для функции x1 XOR x2
    таблица_истинности = [0, 1, 1, 0]
    print("Таблица истинности:", таблица_истинности)
    print("Полином Жегалкина:", вычислить_полином_жегалкина(таблица_истинности))
