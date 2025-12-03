numbers = [45,22,14,65,97,72]
for i in range(len(numbers)):
    if numbers[i]%3==0 and numbers[i]%5==0:
        numbers[i]='fizzbuzz'
    elif numbers[i]%3==0:
        numbers[i]='fizz'
    elif numbers[i]%5==0:
        numbers[i]='buzz'
print(numbers)

numbers = [45,22,14,65,97,72]
for i,num in enumerate(numbers)            :
    if num%3==0 and num%5==0:
        numbers[i]='fizzbuzz'
    elif num%3==0:
        numbers[i]='fizz'
    elif num%5==0:
        numbers[i]='buzz'
print(numbers)

numbers = [45,22,14,65,97,72]
for i,num in enumerate(numbers, start=1):
    print(i, num)
    
#map
def square(n):
    return n*n

print(list(map(square,numbers)))
print([square(n) for n in numbers])
# filter
def is_odd(n):
    return n%3==0

print(is_odd(2))
print(list(filter(is_odd,numbers)))
print([n for n in numbers if is_odd(n)])

print(f"Sorted numbers: {sorted(numbers)}")
print(f"Reverse sorting numbers: {sorted(numbers,reverse=True)}")
animals = [
  {'type':'elephant', 'name':'devon', 'age':3},
  {'type':'puma', 'name':'Moe', 'age': 5},
  {'type':'penguin', 'name':'Stephanie', 'age':8}
]
#sorted with calling function that decide the sort order
print(sorted(animals, key=lambda animal: animal['age'], reverse=True))
