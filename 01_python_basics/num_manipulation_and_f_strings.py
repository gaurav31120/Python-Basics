print(8 / 3) # 2.6666666666666665
print(int(8 / 3)) # 2
print(round(8 / 3)) # 3

print(round(8 / 3, 2)) # 2.67 ----- this will round off to 2 decimal places

print(8 / 3) # 2.6666666666666665 ---- if we will put / then result will come as type - float
print(8 // 3) # 2 ---- if we will put // then result will come as type - int

result = 4 / 2
result /=2
print(result) # 1.0

scored = 0

# user scores a point
scored += 1
print(scored) # 1

#########################  F strings #######################################

score = 0
height = 1.8
isWinning = True
#f-String
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}") # your score is 0, your height is 1.8, you are winning is True

