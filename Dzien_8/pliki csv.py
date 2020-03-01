import csv

dane =[["A","B","C"],
       [1,2,3],
       [4,6,6]]

# with open("test.csv", 'w', newline="") as f:
#     writer = csv.writer(f,delimiter = ";")
#     for row in dane:
#         writer.writerow(row)



with open("test.csv") as f:
    reader = csv.reader(f,delimiter = ";")
    for row in reader:
        print(row)