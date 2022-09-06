import csv
import keyboard

f = open("./data/data.csv", "r", newline="")
csv_reader = csv.reader(f)
rows = list(csv_reader)

