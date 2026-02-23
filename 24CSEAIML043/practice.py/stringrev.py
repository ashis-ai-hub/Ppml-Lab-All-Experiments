s = input("Enter a string: ")
reverse_str = s[::-1]
print("Reversed string:", reverse_str)
vowels = 0
consonants = 0
for ch in s:
    if ch.isalpha():  
        if ch in 'aeiouAEIOU':
            vowels += 1
        else:
            consonants += 1
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
