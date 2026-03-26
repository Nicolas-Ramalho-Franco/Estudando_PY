CP1 = float(input("Digite a primeira nota da CP1: "))
CP2 = float(input("Digite a segunda nota da CP2: "))
CP3 = float(input("Digite a segunda nota da CP2: "))

if CP1 <= CP2 and CP1<=CP3:
    CP1 = CP3
elif CP2 <= CP1 and CP2 <= CP3:
    CP2=CP3
print(f"As duas maiores São {CP1} e {CP2}")