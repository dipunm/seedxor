# Secret splitting with Seed XOR

and how it can improve security, redundancy, and inheritance.

---

## What is a bitcoin wallet?

- Software that facilitates the creation and broadcasting of transactions for its users. 
<!-- .element class="fragment" -->
- Connects to a Bitcoin node to retrieve details of your incoming and outgoing transactions and the final balance.
<!-- .element class="fragment" -->
- May interact with signing devices or act as its own signing device.
<!-- .element class="fragment" -->

---

## What is a private key?

- A randomly picked large number (256 bits long)
<!-- .element class="fragment" -->

<br />
<iframe 
src="https://youtube.com/embed/S9JGmA5_unY?autoplay=0&controls=0&showinfo=0&autohide=1&start=38" allowfullscreen>
</iframe>
<!-- .element class="fragment" -->
<br />

- XPRIV: Extended private key
<!-- .element class="fragment" -->

---

## Different ways to represent a number

- Decimal: (base10) \
    1,223,061
- Binary: (base2) \
    100101010100110010101 
- Hexadecimal: (base16) \
    12A,995

---

## Seed words

- https://observablehq.com/@jimbojw/grokking-bip39

![bip39](/assets/seed_words.png)

---

![bip39](/assets/seed_words.png)

---

## Number Wheel

```
|  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
```
<!-- .element style="text-align:center" -->

---

## Secret splitting

- NOT the same as multisig
- Allows for a more robust backup solution
- Better IMO for inheritance

---

## Multisig

- Requires two or more signing devices*
- Requires signing twice
- Future wallet software is hard to describe

---

## XOR

- 2+ sets of 24 words that reveal a secret number
<!-- .element class="fragment" -->
- Order is unimportant
<!-- .element class="fragment" -->
- Without every key, you are no closer to the final number
<!-- .element class="fragment" -->
- Can create distinct sets for the same key
<!-- .element class="fragment" -->
- Every part and every combination creates a valid XPRIV
<!-- .element class="fragment" -->
- Partial combinations can contain bitcoin as decoys
<!-- .element class="fragment" -->

---

## Workshop

- But first:
  - Most significant digit converter
  - Dice maps (a/symmetry)
  - 6 sided die introduces a small bias
    - Max entropy: ~254 bits
    - Other biases
  - XOR Map

---
<section>
  <img src="/assets/IMG_20220501_211152.jpg" />
</section>
<section>
  <img src="/assets/IMG_20220501_212340.jpg" />
</section>
<section>
  <img src="/assets/IMG_20220501_213251.jpg" />
</section>
<section>
  <img src="/assets/IMG_20220501_214258.jpg" />
</section>
<section>
  <img src="/assets/IMG_20220501_215235.jpg" />
</section>
<section>
  <img src="/assets/SHORT.png" />
</section>
---

## Workshop

- Roll
    - 2 rolls = 1 hex, 
    - 3 hex = 1 word,
    - 6 words = 36 rolls
    - (we'll treat them as a set of 2x 3 word seeds)
- Convert to Hexadecimal
- XOR them

---

## What do do with the parts

### A recipe
- Keep one *online* with high security
- Have one in a safe place at home
- Have duplicates of the physical key
- Create more keys and use them as decoys?

---

## The last word
- ColdCard
<!-- .element class="fragment" -->
- SeedSigner
<!-- .element class="fragment" -->
- Pi Pico + python script
<!-- .element class="fragment" -->
- Fake it
<!-- .element class="fragment" -->

---

## The last word

- Use the last box to write the first and last word with the given prefix.
- The last 2 characters of a hex word is the checksum (3**AF**)
- Seed XOR can be done on 12 words.
- The last 1 character will be your checksum (3A**F**)
- You will have a smaller range of last words that match your key, but a signing device will offer more words to select from.
- There should still only be one valid checksum.