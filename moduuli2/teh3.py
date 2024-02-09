import math
print("suorakulmion area")

num1 = int(input("mitä on suorakolmion kannan pituus?"))
num2 = int(input("mitä on suorakulmion korkeuden pituus?"))

area = num1 * num2

print(f"suorakulmion pinta-alan on {area:.1f}")

piiri = 2*num1 + 2*num2
print(f"suorakulmion piiri on {piiri: .1f}")