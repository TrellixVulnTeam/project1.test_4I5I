from logic.logic1 import *
from logic.logic2 import *
from main_body_logic_db import *


def thermal_calculation_template_1(x1, x2, x3):
    print(x1)

    z1 = x2
    z2 = x3

    m1 = Therm1_Logic(z1, z2)  # создание объекта для расчёта термического оперения шаров стены

    flag = int(input("Добавить расчётный слой?\n1 - ДА;\n2 - НЕТ;\n-"))  # запуск цикла с сбором информации
    while flag == 1:  # создание цикла
        x = float(input("Толщина: "))  # сбор данных: толщина и теплопроводимость
        y = float(input("Теплопроводимость: "))

        m1.therm_calc(x, y)  # метод для расчёта термического оперения шаров стены

        if x1 == "Теплотехнічний розрахунок зовнішніх стін":
            data_dase_1_1(x, y)
        elif x1 == "Теплотехнічний розрахунок зовнішньої стіни нижче відмітки 0.00":
            data_base_2_1(x, y)
        elif x1 == "Теплотехнічний розрахунок горищного покриття":
            data_base_6_1(x, y)
        elif x1 == "Теплотехнічний розрахунок над підвалом та техпідпіллям":
            data_base_4_1(x, y)
        else:
            print("Помилка")
            return

        flag = int(input("Добавить расчётный слой?\n-"))  # зацикливание процесса

    print("Ответ", m1.full_formul_calc())
    ans = m1.full_formul_calc()

    if x1 == "Теплотехнічний розрахунок зовнішніх стін":
        data_base_1_2(ans)
    elif x1 == "Теплотехнічний розрахунок зовнішньої стіни нижче відмітки 0.00":
        data_base_2_2(ans)
    elif x1 == "Теплотехнічний розрахунок горищного покриття":
        data_base_6_2(ans)
    elif x1 == "Теплотехнічний розрахунок над підвалом та техпідпіллям":
        data_base_4_2(ans)
    else:
        print("Помилка")
        return


def thermal_calculation_template_2(x1):
    print(x1)
    if x1 == "Теплотехнічний розрахунок стін підвалу нижче поверхні землі для I зони":
        z_zero = 2.1

    if x1 == "Теплотехнічний розрахунок стін підвалу нижче поверхні землі для II зони":
        z_zero = 4.3

    if x1 == "Теплотехнічний розрахунок стін підвалу нижче поверхні землі для III зони":
        z_zero = 8.6

    if x1 == "Теплотехнічний розрахунок стін підвалу нижче поверхні землі для IV зони":
        z_zero = 14.2

    if x1 == "Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для I зони" :
        z_zero = 2.1

    if x1 == "Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для II зони":
        z_zero = 4.3

    if x1 == "Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для III зони":
        z_zero = 8.6

    if x1 == "Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для IV зони":
        z_zero = 14.2

    m3 = Therm2_Logic(z_zero)

    flag = int(input("Добавить расчётный слой?\n1 - ДА;\n2 - НЕТ;\n-"))  # запуск цикла с сбором информации
    while flag == 1:  # создание цикла
        x = float(input("Толщина: "))  # сбор данных: толщина и теплопроводимость
        y = float(input("Теплопроводимость: "))

        m3.therm2_calc(x, y)

        if x1 == "Теплотехнічний розрахунок стін підвалу нижче поверхні землі для I зони":
            data_base_3_1_1(x, y)
        elif x1 == "Теплотехнічний розрахунок стін підвалу нижче поверхні землі для II зони":
            data_base_3_1_2(x, y)
        elif x1 == "Теплотехнічний розрахунок стін підвалу нижче поверхні землі для III зони":
            data_base_3_1_3(x, y)
        elif x1 == "Теплотехнічний розрахунок стін підвалу нижче поверхні землі для IV зони":
            data_base_3_1_4(x, y)
        elif x1 == "Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для I зони":
            data_base_5_1_1(x, y)
        elif x1 == "Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для II зони":
            data_base_5_1_2(x, y)
        elif x1 == "Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для III зони":
            data_base_5_1_3(x, y)
        elif x1 == "Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для IV зони":
            data_base_5_1_4(x, y)
        else:
            print("Помилка")
            return

        flag = int(input("Добавить расчётный слой?\n-"))  # зацикливание процесса

    print("Ответ", m3.full_therm2_calc())
    ans = m3.full_therm2_calc()

    if x1 == "Теплотехнічний розрахунок стін підвалу нижче поверхні землі для I зони":
        data_base_3_2_1(ans)
    elif x1 == "Теплотехнічний розрахунок стін підвалу нижче поверхні землі для II зони":
        data_base_3_2_2(ans)
    elif x1 == "Теплотехнічний розрахунок стін підвалу нижче поверхні землі для III зони":
        data_base_3_2_3(ans)
    elif x1 == "Теплотехнічний розрахунок стін підвалу нижче поверхні землі для IV зони":
        data_base_3_2_4(ans)
    elif x1 == "Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для I зони":
        data_base_5_2_1(ans)
    elif x1 == "Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для II зони":
        data_base_5_2_2(ans)
    elif x1 == "Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для III зони":
        data_base_5_2_3(ans)
    elif x1 == "Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для IV зони":
        data_base_5_2_4(ans)
    else:
        print("Помилка")
        return
