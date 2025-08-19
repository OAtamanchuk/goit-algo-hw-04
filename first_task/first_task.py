def total_salary(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            total = 0
            count = 0
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        salary = int(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        continue
            if count == 0:  
                return (0, 0)
            average_salary = total / count
            return (total, average_salary)
    except FileNotFoundError:
        print("Файл не знайдено")
        return (0, 0)

total, average = total_salary("first_task/salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")





