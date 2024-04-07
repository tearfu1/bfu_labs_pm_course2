def rabinKarp(s, w):
    answer = []
    n = len(s)
    m = len(w)

    # Вычисление начальных хешей для s и w
    hashS = hash(s[:m])
    hashW = hash(w)

    # Проход по строке s и сравнение хешей
    for i in range(n - m + 1):
        if hashS == hashW and s[i:i + m] == w:  # Дополнительно проверяем подстроку
            # Если хеши совпали и подстроки совпадают, добавляем индекс i в ответ
            answer.append(i)
        if i < n - m:
            # Пересчет хеша для следующего окна
            hashS = hash(s[i + 1:i + m + 1])

    return answer

# Пример использования
s = "GCATCGCAGAGAGTATACAGTACG"
w = "GCAGAGAG"
print(rabinKarp(s, w))
