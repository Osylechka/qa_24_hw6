# import random, calendar
# from calendar import weekheader
# from datetime import datetime, timedelta

# x = random.randint(0, 100)
#
# print(x)
#
# if x >=90:
#     print('A')
#
# elif x >=75:
#     print('B')
#
# elif x >=60:
#     print('C')
#
# else:
#     print('D')

# name = input("Name: ").strip()
# if name:
#     if name != '-':
#         print("Name cannot be blank")
#     else:
#         print("Error")

# age = 20
# had_id = False
#
# if age >= 18 and had_id == True:
#     print('OK')
#
# else:
#     print('Error')

# a, b, c, d = 1000, 20, True, 10
# if a >= b >= c <= d:
#     print('Ok')

# def square(number):
#     return number * number
#
#
# for i in range(1, 11):
#     print(square(i))


# def repeat(text, times):
# #     return text * times
# #
# # print(repeat('Hello', 10))

# def format_test(text, upper=True):
#     if upper:
#         text = text.upper()
#     return text

# def show_work_schedule(days=7, work_time="9:00-18:00"):
#     today = datetime.today()
#
#     for day in range(days):
#         day = today + timedelta(days=day)
#         weekday = day.weekday()
#         day_name = calendar.day_name[weekday]
        # print(day_name, day)


# from datetime import datetime, timedelta
# import calendar
#
#
# def show_work_schedule(days=7, work_time="9:00-18:00"):
#     today = datetime.today()
#
#     for i in range(days):
#         current_day = today + timedelta(days=i)
#         weekday = current_day.weekday()
#         day_name = calendar.day_name[weekday]
#
#         # Проверяем, рабочий ли это день (0-4 - понедельник-пятница)
#         if weekday < 5:  # 0-4 это понедельник-пятница
#             print(f"{day_name}, {current_day.strftime('%d.%m.%Y')}: {work_time}")
#         else:
#             print(f"{day_name}, {current_day.strftime('%d.%m.%Y')}: Выходной")
#
#
# # Вызываем функцию
# show_work_schedule()
#
# from datetime import datetime
#
# def log(event, /, *args, level='INFO', **meta):
#     print(f'{level}: ', event, args, meta)
#
# # Правильные вызовы:
# log('start')
# log('download', 'file.txt', level='CRITICAL', user='admin', time=datetime.now().date())
# log('download', 'file.txt', user='admin', time=datetime.now().date())

def fib(n):
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)
print(fib(6))
print(fib(7))
print(fib(8))