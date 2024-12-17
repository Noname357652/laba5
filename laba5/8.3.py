def create_set(prompt):
    while True:
        user_input = input(prompt)
        try:

            return set(map(int, user_input.split()))
        except ValueError:
            print("Введены некорректные символы. Пожалуйста, введите только числа, разделенные пробелами.")


set_1 = create_set("Введите первое множество (числа, разделенные пробелами):\n")
set_2 = create_set("Введите второе множество (числа, разделенные пробелами):\n")


intersection = set_1.intersection(set_2)


if intersection:
    result = ' '.join(map(str, intersection))
    print(f"Пересечение множеств: {result}")
else:
    print("Пересечения нет")
