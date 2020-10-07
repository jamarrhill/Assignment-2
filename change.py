# Name: Jamar Hill
# Date: 10/07/20
# Description: Change Conversion

print("Please enter an amount in cents less than a dollar.")
C = float(input())
Q = 25 % C
D = 10 % C
N = 5 % C
P = 1 % C
print("Your change will be:")
print("Q =", C // 25) # Remainder 10
R_Q = C % 25
print("D =", R_Q // 10) # Remainder 4
R_D = R_Q % 10
print("N =", R_D // 5)
R_N = R_D % 5
print("P =", R_N // 1)