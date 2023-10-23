line1 = ["⬜", "⬜", "⬜"]
line2 = ["⬜", "⬜", "⬜"]
line3 = ["⬜", "⬜", "⬜"]
Map = [line1, line2, line3]
print("   A     B    C")
print(f"1{line1}\n2{line2}\n3{line3}")
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
col = position[0].lower()
abc = ["a", "b", "c"]

col_index = abc.index(col)
row_index = int(position[1]) - 1

Map[row_index][col_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
