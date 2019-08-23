import random
import typing

# powitanie
print("Masz do zestrzelenia dwa jednomasztowce. Powodzenia!")
clear = "\n" * 100

# tworzenie planszy

row_title: typing.List[str] = ["A", "B", "C", "D", "E"]
row_A: typing.List[str] = ["1 "]
row_B: typing.List[str] = ["2 "]
row_C: typing.List[str] = ["3 "]
row_D: typing.List[str] = ["4 "]
row_E: typing.List[str] = ["5 "]

for i in range(5):
    row_A.append("0")
    row_B.append("0")
    row_C.append("0")
    row_D.append("0")
    row_E.append("0")


def board_print():
    print("   " + " ".join(row_title))
    print(" ".join(row_A))
    print(" ".join(row_B))
    print(" ".join(row_C))
    print(" ".join(row_D))
    print(" ".join(row_E))


# losowanie umiejscowienia statkow
ship_A = []
ship_B = []

for i in range(2):
    ship_A.append(random.randrange(1, 5, 1))
    ship_B.append(random.randrange(1, 5, 1))

while ship_A == ship_B:
    ship_B[1] = random.randrange(1, 5, 1)

dic_col = dict(A=1, B=2, C=3, D=4, E=5)

# wprowadzanie strzalu

while ship_A != [0, 0] or ship_B != [0, 0]:
    board_print()
    print(ship_A, ship_B)
    print("Oddaj strzal")
    shoot_col: str = input("Wprowadz litere kolumny: ")
    shoot_col = shoot_col.upper()
    while shoot_col != "A" and shoot_col != "B" and shoot_col != "C" and shoot_col != "D" and shoot_col != "E":
        shoot_col: str = input("Wprowadz litere kolumny: ")
    shoot_row: str = input("Wprowadz cyfre wiersza: ")
    while shoot_row != "1" and shoot_row != "2" and shoot_row != "3" and shoot_row != "4" and shoot_row != "5":
        shoot_row: str = input("Wprowadz cyfre wiersza: ")

    shoot_check: typing.List[int] = [int(dic_col[shoot_col]), int(shoot_row)]


    def shoot_mark(hit_mark):
        if shoot_check[1] == 1:
            row_A[shoot_check[0]] = hit_mark
        elif shoot_check[1] == 2:
            row_B[shoot_check[0]] = hit_mark
        elif shoot_check[1] == 3:
            row_C[shoot_check[0]] = hit_mark
        elif shoot_check[1] == 4:
            row_D[shoot_check[0]] = hit_mark
        elif shoot_check[1] == 5:
            row_E[shoot_check[0]] = hit_mark


    hit = "!"
    miss = "X"

    if ship_A == shoot_check:
        shoot_mark(hit)
        ship_A = [0, 0]
    elif ship_B == shoot_check:
        shoot_mark(hit)
        ship_B = [0, 0]
    else:
        shoot_mark(miss)
    print(clear)

print("Brawo! Oba statki zatopione!")
board_print()
