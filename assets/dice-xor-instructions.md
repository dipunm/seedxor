# Dice XOR Instructions

This is a guide on how to use the dice-xor worksheet.

To understand the motivation behind this tool,and how you could use it to secure your bitcoin, please check out [background.md](background.md).

## Instructions

Using one of the provided worksheets, you will produce two BIP-39 seed phrases which combine to produce a third BIP-39 seed phrase. The third seed phrase will be used by your Bitcoin wallet, while the first two will be used as part of your backup solution.

If you already have a seed phrase provided by your wallet, you may choose to use the worksheet to split it into two new seed phrases for your backup solution.

> Be sure to destroy any physical paper trails of the seed phrase used by your Bitcoin wallet to ensure the security of your wallet.

### You need:
- One or more dice
- A printed version of the [dice-xor-12words-a4.pdf](dice-xor-12words-a4.pdf) or the [dice-xor-24words-a4.pdf](dice-xor-24words-a4.pdf) file
- A pen or pencil

This guide focuses on the 24 word version of the worksheet for brevity, but will explain certain important differences between this and the 12 word variant.

> NOTE: ALWAYS DOUBLE CHECK YOUR WORK. After completing, redo the lookup processes again to verify that you get the same answers as before.

> NOTE: BE SURE TO DESTROY THE WORKSHEET AND ANY EVIDENCE OF YOUR FINAL SEED PHRASE.

### The word list

The first 4 pages provide the full range of official words that can be used to create a bitcoin seed word backup.

Paired with each word is a 3 digit code. This list is sorted alphabetically.

### The worksheet

On the final page, is a worksheet. It is designed to allow us to generate two sets of 24 seed words, and then combine them to make our third set of seed words.

The first two tables that span the page are there to be filled in by pen or pencil. Think of it as one long table that we cut into two because a single table with 24 columns would not fit on a single page.

Notice that the table has 3 rows grouped by letter `A` and another 3 rows grouped by letter `B`. `A` and `B` represent our first two set of seed words, and the first two rows within them are used to help us formulate those words from a set of dice rolls.

In this guide, we will refer to words as `A1` or `B3` etc. Use the numbers above the table and match with the letter on the left of the table to identify what area of the table we are referring to.

The rows labelled `A⊕B` will store a hex code representing the combined key of `A` and `B` and the final row will contain the matching words, revealing our third set of seed words.

The other tables below are lookup tables that will help us as we continue through this guide.

### Rolling dice

The first thing we need to do, is to roll a die 132 times (roll 70 times for the 12 word variant). An 8 sided die is technically fairer, but a 6 sided die will do fine too.

If we have multiple dice, we can speed up the process by rolling them together.

As we roll the dice, write the results in the `Rolls` row in the `A` section of the table. Put exactly 6 outcomes in each column.

For example, if I roll 6 times, and get the following results: `3, 3, 5, 1, 6, 2`, then I should write `3,3,5,1,6,2` in the `Rolls` row for word `A1`. Be sure to give yourself space to fit in all the numbers.

The final 24th column will have only 2 outcomes. This is fine, the 24th word is special, and we'll get to that at the end.

If you are using the 12 word variant, then you should have a total of 4 outcomes for the 12th word.

### Generating hex codes

On the worksheet, there are two lookup tables, one for 6 sided dice, and one for 8 sided dice. Use the approriate lookup table.

Take your rolls in pairs and use the lookup table to find the appropriate number or letter and write it into the first column in the `HexCode` row.

For example, assuming I am using a 6 sided die, based on the above rolls: `3,3,5,1,6,2`, I should get the following code for word `A1`: 
```
3x3 = A
5x1 = 4
6x2 = 2
---
A42
```

Continue this process until we have a set of codes for seed words `A`. Again, the 24th word will have a single digit code for now.

If you are using the 12 word variant, you will have a 2 digit code for the 12th word.

### The most significant digit

Before we can look up our word using our hex code, we need to make a small adjustment. Our seed words map to hex codes ranging from `000` to `7FF`.

If the first digit of our code is larger than `7`, or if it is a letter, then we need to convert it using the `Most significant digit converter` lookup table.

For example, our code for word `A1` would change from `A42` to `242`.

We only need to change the FIRST digit of each 3 digit code, the other two should remain the same.

If we had a word with the following code: `FFF`, we would convert it to `7FF`.

### Looking up the words

Now we can use the big seed word table to find the appropriate seed words to fill in the `Words` column for seed words `A`.

Leave the last word empty for now.

### Repeat for B

Roll another 132 times and follow the steps above, this time filling in the sheet for seed words `B`.

If you are looking to split an existing seed phrase into two parts, you can skip the dice rolling steps and work backwards:

- Write the seed words down
- Use the lookup table to find the appropriate hexcodes for each word and fill that in too.

### XOR time

To fill in the `A⊕B` row, we will use the lookup table labeled `XOR Map`. Simply take each digit of hex code `A` and `B` and use the lookup table to find the appropriate digit for our third seed.

For example, if word `A1` had the code `242` and word `B1` had the code `73A`, then we would get the following result:
```
2x7 = 5
4x3 = 7
2xA = 8
---
578
```

Continue this until all 24 hex codes have been converted. The last word will end up with a single digit hex code. This is fine.

If using the 12 word variant, the last word will end up with a 2 digit hex code.

### The final set of seed words

Finally, we can look up each code and write the appropriate word into the final row of the table. The last word will be left blank for now.

### The last word

Since we only have the first digit of the code for the last word, we can only know a range of words that the last word might be. For example, if our last word begins with `5`, then our last word will be somewhere between `parade` and `say`.

Depending on what devices you have, there are a few ways that we can work out our last word:

#### Hardware wallet
If we have a hardware wallet, we can enter the first 23 words of each of our seed phrases into the device, and it will offer 16 possible words to finish with. Find the one that fits within the range of our last word (eg. the one between `parade` and `say` alphabetically). This is your final word, there will always only be one matching word.

#### TailsOS
If you are technically able to run TailsOS, consider using a python script such as [generate-seed.min.py](generate-seed.min.py) made by myself, or use the pre-installed Electrum wallet to help discover the appropriate last word.

#### Make it up

A last ditch idea, is to pick any word within the range of possible words given our first hexcode digit.

There are some important tradeoffs to consider here:

- This option is OKAY to use on seed words that are part of your backup, but your final ephemeral private key will need a properly calculated final word.
- The downside to using this method, is that if an attacker finds one of our seed words and enters it into a wallet, they will be able to tell immediately that the last word is wrong and that you may be using it as a seed XOR setup.
- Another downside, is that the final word cannot act as a checksum for your other 23 words. If you mistype or misrecord your seed words, the final word gives your bitcoin wallet enough information to warn you that the backup is mistyped or has been compromised. Without knowing the correct final word, you will rely on the wallet to provide the last word and will not know if you made any mistakes which could lead you to losing access to your bitcoin.

