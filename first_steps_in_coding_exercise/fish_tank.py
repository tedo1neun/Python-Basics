length = int(input())
width = int(input())
height = int(input())
percent_occupied = float(input())

Volume = length * width * height
Volume_L = Volume / 1000
occupied_float = percent_occupied / 100

Volume_Needed_IN_L = Volume_L * (1-occupied_float)

print(Volume_Needed_IN_L)