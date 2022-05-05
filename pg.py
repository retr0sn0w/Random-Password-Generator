import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbol = "!@#$%^&*()_+[]{}:;.,<>/?"

ans = lower_case + upper_case + symbol + num

length = 20

password = "".join(random.sample(ans,length))

print("La contrasena generada es: ",password)