def get_cats_info(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            cats_info = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id = parts[0]
                    name = parts[1]
                    age = parts[2]
                    cats_info.append({"id": cat_id, "name": name, "age": age})
                else:
                    print(f"Неправильний формат рядка: {line}")
            return cats_info
    except FileNotFoundError:
        print("Файл не знайдено")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []
    
cats_info = get_cats_info("second_task/cats.txt")
print(cats_info)
        