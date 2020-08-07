# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open("ciphertext.txt") as f:
    words = f.read()

word_list = words.split()

#letters in order of frequency
letters = ('E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z')


count = {}

for word in word_list:
    for char in word:
        if char.isalpha():
            if char not in count:
                count[char] = 1

            else:
                count[char] += 1

        else: continue

letter_count = list(count.items())

letter_count.sort(key=lambda x: x[1], reverse=True)
print(letter_count)


decoded = {}

for num in range(len(letter_count)):
    decoded[letter_count[num][0]] = letters[num]

#print(decoded)

def crack_caeser(s):
    #string for translated text
    translated_cipher = ''

    for char in s:
        if char.isalpha():
            #if the character in the string is an alphabet letter - add the decoded character num to the translated_cipher
            translated_cipher += decoded[char]
        else:
            #if not a letter add the character
            translated_cipher += char

    return translated_cipher

#map the decoded number to the word_list words
final_decode = map(crack_caeser, word_list)

#print it all out, joined back together       
print(" ".join(final_decode))


