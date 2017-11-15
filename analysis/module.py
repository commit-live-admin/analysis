from time import sleep
import csv


asdMy = 1

from macpath import abspath



# for i in range(10):
#     sleep(1)
#     i = i + 1

# print(i)

def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    print(reader)


if __name__ == "__main__":
    csv_path = "data/olympics.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)
