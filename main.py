from colorama import Style, Fore

fizzCount = 0
buzzCount = 0
fizz_buzz_count = 0
another_numbers = 0

print(Style.BRIGHT)

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(Fore.GREEN + "FizzBuzz")
        fizz_buzz_count += 1
    elif i % 3 == 0:
        print(Fore.YELLOW + "Fizz")
        fizzCount += 1
    elif i % 5 == 0:
        print(Fore.BLUE + "Buzz")
        buzzCount += 1
    else:
        print(f'{Fore.WHITE} {i}')
        another_numbers += 1

print("")
print(f'{Fore.GREEN} FizzBuzz Count = {fizz_buzz_count}')
print(f'{Fore.YELLOW} Fizz Count = {fizzCount}')
print(f'{Fore.BLUE} Buzz Count = {buzzCount}')
print(f'{Fore.WHITE} Another Numbers Count = {another_numbers}')

print(Style.RESET_ALL)