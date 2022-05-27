import sys
import hashlib
import re

# Validation of the arguments
# Check there are 24 arguments
argument_count = len(sys.argv) - 1
if argument_count != 24:
    print('Error: found %d arguments, there should be a total of 24!'%(argument_count))
    print("Exiting. Re-execute the program to try again.")
    exit(1)

# Check the first 23 are 3 digit hex values
for i in range(1, 24):
    if re.search(r"^[0-9A-Fa-f]{3}$", sys.argv[i]) is None:
        print('Error: argument %d is invalid: %s!'%(i, sys.argv[i]))
        print("Exiting. Re-execute the program to try again.")
        exit(1)

# Check the last argument is a single hex value
if re.search(r"^[0-9A-Fa-f]$", sys.argv[24]) is None:
    print('Error: argument 24 is invalid: %s!'%(sys.argv[24]))
    print("Exiting. Re-execute the program to try again.")
    exit(1)

outcomes = sys.argv[1:24]
tail = sys.argv[24]

print('Inputs validated! continuing with calculations\n')

# Start with an empty string for our 'binary' string
binary = ''

##
# Each word should be represented by 11 bits, but our
# hexadecimal outcomes represent 12 bit numbers.
# 
# We discard the leftmost bit from each outcome before
# appending it to our 'binary' string.
##

# loop over each word in 'outcomes' array
for word in outcomes:
    # convert hexadecimal (base 16) string into an actual number type
    word_numeric = int(word, 16)

    # reformat number as a 12 bit binary string
    word_binary = "{0:012b}".format(word_numeric)
    
    # take rightmost 11 characters and append to 'binary'
    binary += word_binary[-11:]

##
# Our tail must represent only 3 bits of the last 
# word to allow for 8 bits to be provided by the 
# checksum.
# 
# Again, we discard the leftmost bit from our tail 
# before appending it to our 'binary' string
##

# convert 'tail' (base 16) to an actual number type
tail_numeric = int(tail, 16)

# reformat number as 4 bit binary string
tail_binary = "{0:04b}".format(tail_numeric)

# take rightmost 3 characters only to add to 'binary'
tail_compact = tail_binary[-3:]

# append to binary
binary += tail_compact

# We now have 23*11+3 bits of information: 256 bits.
print('calculated binary value as: %s\n'%(binary))

# Convert binary (base 2) string back to a number type
# And then to 32 bytes in big endian byte order
bytes = int(binary, 2).to_bytes(32, 'big')

# Hash the bytes to derive our checksum
sha = hashlib.sha256(bytes).hexdigest()

print('calculated sha value as: %s'%(sha))

# The checksum is the first byte (8 bits = 2 hexadecimal characters)
checksum = sha[0:2].upper()

print('the checksum is 2 chars: %s\n'%(checksum))

# recalculate the numeric value of 'tail' compact
tail_compact_numeric = int(tail_compact, 2)

# reformat 'tail_compact_numeric' as a single hexadecimal character
tail_compact_hex = "{0:01X}".format(tail_compact_numeric)

print('tail compacts to: %s'%(tail_compact_hex))

# combine the 'tail' with the checksum to get the last word.
last_word = tail_compact_hex + checksum

print('so the last word is: %s\n'%(last_word))

# create an empty array for the XOR Worksheet adjusted words
words = []

# Loop 23 times in multiples of 11 for each word
for i in range(0, 23*11, 11):
    # take 11 character segment from 'binary' string
    word_binary = binary[i:i+11]

    # convert back to numeric value
    word_numeric = int(word_binary, 2)

    # re-format as hexadecimal
    word_hex = "{0:02X}".format(word_numeric)

    # add word to 'words' array
    words.append(word_hex)

print('your seed XOR words are:')
print('----------')
print("%s %s"%(" ".join(words), last_word))
print('----------')
