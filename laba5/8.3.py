def create_many(a):
    while True:
        inputt = input(a)

        try:
            text = set(map(int, inputt.split()))
            return text
        except ValueError:
            print("Введены некорректные символы. Введите числа")
            exit(0)


text_1 = create_many("Введите первое множество\n")
text_2 = create_many("Введите второе множество\n")

intersec = text_1.intersection(text_2)

if intersec:
    r = ' '.join(map(str, intersec))
    print(f"Пересечение множеств: {r}")
else:
    print("Пересечения нет")
