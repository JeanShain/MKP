import sys
from typing import List, Tuple


def read_population_data(file_path: str) -> List[Tuple[str, float, int]]:
    """Зчитує файл і повертає список кортежів (країна, площа, населення)."""
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(', ')
                if len(parts) != 3:
                    continue
                country, area, population = parts[0], float(parts[1]), int(parts[2])
                data.append((country, area, population))
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    except ValueError:
        print("Помилка у форматі даних.")
    return data


def sort_by_area(data: List[Tuple[str, float, int]]) -> List[Tuple[str, float, int]]:
    """Сортує список за площею."""
    return sorted(data, key=lambda x: x[1], reverse=True)


def sort_by_population(data: List[Tuple[str, float, int]]) -> List[Tuple[str, float, int]]:
    """Сортує список за населенням."""
    return sorted(data, key=lambda x: x[2], reverse=True)


def main():
    if len(sys.argv) < 2:
        print("Використання: python script.py файл.txt")
        return

    file_path = sys.argv[1]
    data = read_population_data(file_path)

    if not data:
        print("Дані не знайдено або мають невірний формат.")
        return

    print("Сортування за площею:")
    for country, area, population in sort_by_area(data):
        print(f"{country}: {area} км², {population} осіб")

    print("\nСортування за населенням:")
    for country, area, population in sort_by_population(data):
        print(f"{country}: {area} км², {population} осіб")


if __name__ == "__main__":
    main()
