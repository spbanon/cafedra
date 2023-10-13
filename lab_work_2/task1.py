money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 1.05  # Ежемесячный рост цен

monthes = 0
while money_capital > spend:
    money_capital += salary
    money_capital -= spend

    if monthes != 0:

        spend = spend * increase
    monthes+=1

print("Количество месяцев, которое можно протянуть без долгов:", monthes)
