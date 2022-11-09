month = 9

spring_months = {
    3: "Март",
    4: "Апрель",
    5: "Май",
}
summer_months = [6, 7, 8]
autumn_months = (9, 10, 11)
winter_months = {12, 1, 2}

if month in spring_months:
    print("Весна")
elif month in summer_months:
    print("Лето")
elif month in autumn_months:
    print("Осень")
elif month in winter_months:
    print("Зима")
