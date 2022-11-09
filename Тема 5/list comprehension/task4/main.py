students_list = [
    {
        "name": "Саша",
        "age": 27,
    },
    {
        "name": "Кирилл",
        "age": 52,
    },
    {
        "name": "Маша",
        "age": 14,
    },
    {
        "name": "Петя",
        "age": 36,
    },
    {
        "name": "Оля",
        "age": 43,
    },
]

ages_list = [student["age"] for student in students_list]
mean_age = sum(ages_list) / len(ages_list)

print([student for student in students_list if student["age"] < mean_age])
