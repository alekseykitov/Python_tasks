import csv
import random


def create_csv_file_with_random_numbers(file_path: str) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        for _ in range(random.randint(100, 1000)):
            writer.writerow([random.randint(-10, 10) for _ in range(3)])


if __name__ == "__main__":
    create_csv_file_with_random_numbers("Random_Numbers.csv")
