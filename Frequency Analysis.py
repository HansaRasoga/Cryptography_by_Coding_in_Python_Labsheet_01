alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = input("Enter the ciphertext: ").upper()

freq={}
#Initialize a dictionary freq to 0 for all letters in the alphabet
for c in alphabet:
    freq[c]=0

letter_count=0
for c in cipher:
    if c in freq:
        freq[c]+=1
        letter_count+=1
print("Letter Count: ",letter_count)

if letter_count:
    for c in freq:
        freq[c]=round(freq[c]/letter_count,4)

new_line_count=0
for c in freq:
    print(c," : ",freq[c],end=" ")
    if new_line_count%3==2:
        print()
    new_line_count+=1

