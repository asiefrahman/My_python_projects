from datetime import datetime

def print_time(task_name):
    print(task_name)
    print(datetime, datetime.now())
    print()

first_time='Susan'
print_time(first_time)

for x in range(1,10000000,2000000):
    print_time('printed for ')
