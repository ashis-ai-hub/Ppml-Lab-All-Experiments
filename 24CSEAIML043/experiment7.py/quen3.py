
para = input("Enter a paragraph: ")
words = para.split()
print("Total number of words:", len(words))
pal_count = 0
for w in words:
    if w.lower() == w.lower()[::-1] and len(w) > 1:
        pal_count += 1
print("Number of palindrome words:", pal_count)
print("Words in reverse order:")
for w in words:
    print(w[::-1])
