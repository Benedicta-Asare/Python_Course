#4-3. Counting to Twenty
print("Numbers from 1 to 20:")
for num in range(1,21):
    print(num)

#4-5. Summing a Million
numbers = list(range(1,1000001))
print("\n", min(numbers))
print(max(numbers))
print(sum(numbers))

#4-6. Odd Numbers
print("\nOdd numbers from 1 to 20:") 
odd_numbers = list(range(1,21,2))
for number in odd_numbers:
    print(number)

#4-7. Multiples of three
print("\nMultiples of 3 from 3 to 30:")
multiples = list(range(3,31,3))
for num in multiples:
    print(num)