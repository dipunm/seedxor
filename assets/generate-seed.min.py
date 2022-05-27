import sys
import hashlib
import re

argument_count = len(sys.argv) - 1
if argument_count != 24:
    print('Error: found %d arguments, there should be a total of 24!'%(argument_count))
    print("Exiting. Re-execute the program to try again.")
    exit(1)

for i in range(1, 24):
    if re.search(r"^[0-9A-Fa-f]{3}$", sys.argv[i]) is None:
        print('Error: argument %d is invalid: %s!'%(i, sys.argv[i]))
        print("Exiting. Re-execute the program to try again.")
        exit(1)

if re.search(r"^[0-9A-Fa-f]$", sys.argv[24]) is None:
    print('Error: argument 24 is invalid: %s!'%(sys.argv[24]))
    print("Exiting. Re-execute the program to try again.")
    exit(1)

outcomes = sys.argv[1:24]
tail = sys.argv[24]

binary = ''
for word in outcomes:
    word_numeric = int(word, 16)
    word_binary = "{0:012b}".format(word_numeric)
    binary += word_binary[-11:]

tail_numeric = int(tail, 16)
tail_binary = "{0:04b}".format(tail_numeric)
tail_compact = tail_binary[-3:]
binary += tail_compact

bytes = int(binary, 2).to_bytes(32, 'big')
sha = hashlib.sha256(bytes).hexdigest()
checksum = sha[0:2].upper()

tail_compact_numeric = int(tail_compact, 2)
tail_compact_hex = "{0:01X}".format(tail_compact_numeric)
last_word = tail_compact_hex + checksum

words = []
for i in range(0, 23*11, 11):
    word_binary = binary[i:i+11]
    word_numeric = int(word_binary, 2)
    word_hex = "{0:02X}".format(word_numeric)
    words.append(word_hex)

print('your seed XOR words are:')
print('----------')
print("%s %s"%(" ".join(words), last_word))
print('----------')
