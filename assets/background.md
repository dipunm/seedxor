## Motivation

When you set up a self-custodial wallet, you are usually asked to create a backup of your extended private key in the form of 12 or 24 words.

Unfortunately, not much advice is given as to _how_ and _where_ we should create and store our backups.

If we make only a single backup, we have a chance of losing or accidentally destroying the backup; this means we could lose access to the bitcoin that we saved.

If we make multiple backups, we increase the odds of leaking our backup, or having a copy stolen; this means someone could take the bitcoin that we saved.

A single 24 word seed phrase is like a hot potato, and most _**naive**_ attempts to split a backup into multiple parts will compromise our security ([Why is seed splitting a bad idea? - youtube video](https://www.youtube.com/watch?v=p5nSibpfHYE)), but what if we could split our secret into multiple parts without compromising on security?

> Note: Shamir's secret sharing scheme (aka SSSS) is a good way to split a secret without compromising on security as explained by Andreas Aantonopolous in the video linked above, but the XOR method is simpler and can be done mostly with a dice, pen and paper.

By splitting a secret **securely**, when combined with **isolated domains**, we gain the ability to create multiple backups with less concern for leakage or theft.

## Isolated Domains

A domain is simply a location, or a set of locations that can be considered related to each other with respect to a subject. That subject would be you and/or your bitcoin backups.

If you have a rigid daily routine, someone who knows of your bitcoin, who would like to find your backups, might visit and/or break into locations that you frequent in order to find your backups.

Creating domains is not easy, but if we can think of a different set of locations, maybe ones which you frequent much less often, that could become another set of locations that make up a new domain.

If we trust a friend or relative to keep a secret and apply good security, we can consider them to be another domain with whom we could store backups, that an attacker might not know about.

A bank secure deposit box could be considered a good isolated domain. Even if an attacker were to identify that it was a likely place for you to keep a backup, getting access to that backup is going to be very difficult and risky.

Finally, for many individuals, as long as your online security is decent, online storage services can act as another isolated domain. If your online security is not great, (if for example, you keep your passwords in a notebook) then there is good reason to believe that someone who can break into your home can also break into your online accounts.

When splitting your secrets, it is important to keep each part within separate domains. Each domain can have duplicate copies, for example, your trusted friend can make multiple copies of the seed words that they receive in order to avoid losing it forever.

You should also have a way to know if any of your backups in each domain has been compromised.

## Quick thought experiment
Imagine you have two keys:

1. Multiple copies of Key A are stored at home, in the garden, in your car and at work.
2. Copies of Key B are stored in safety deposit boxes in 3 different locations.

The following risks are mitigated:

1. An attacker breaks into your car. They found Key A, but even if they break into your home, they will never find Key B.
2. The government raids local banks and an officer steals Key B. They may know who you are, and may attempt to break into your home to find Key A. Be aware.

In either case, the discovery of either Key A or Key B does not present an immediate threat to your funds 👍

However, the chances of your being targeted for a possible Key B has now increased, and the consequence of someone discovering Key B is much more likely to present an immediate threat to your funds ⚠️

To summarise, this setup affords you TIME ⏱️. You should still stay aware of your backup locations and whether they might have been compromised. For example, if you kept a key at your workplace and there was recently a break-in, consider the key compromised.

If you suspect that your keys have been compromised, you should create a new wallet, move your funds as soon as possible and then recreate your seedxor setup. You should also be more concious of risks to the copies of your other key until you have done so.

Seedxor is not limited to just 2 fragments. You could split your key into 3 or 4 keys before distributing them to different locations. Although this increases security, it also increases the complexity of your setup and the need to identify more isolated domains.

## An ephemeral private key

An ephemeral private key, is one that exists temporarily, but is then forgotten or destroyed.

When considering a backup strategy for your bitcoin wallet, any written or stored record of your wallet's private key is a single point of failure; if it were to get leaked or fall into the hands of a criminal, they would have full access to steal your bitcoin!

By keeping your wallet's private key ephemeral, you remove this single point of failure, and any chance of stealing your funds, now **exclusively** relies on an attacker being able to compromise your keys across your isolated domains.

Note, that if your wallet is HOT, then your private key is not ephemeral as there still exists a record of your sensitive private key to steal. Furthermore, as a hot record, it exists or has existed on a device that can be remotely compromised by a hacker.

## XOR Seed splitting vs Multisig

Let's be clear, from a technical security point of view, Multisig is an objectively more secure solution. It is also becoming easier to implement (although not necessarily cheaper) over time.

That said, the fact that it requires two signing devices and two rounds of signing makes it feel convoluted and complicated for a single user. This has to be done every time you spend.

By contrast, seed splitting allows us to keep using a more convenient setup for personal use, and provides the extra security only for our backups, recovery plans, and inheritance plans.

When we set up our wallets, we have to write down our seed phrase. To many, it can feel like the backup is our most vulnerable point of failure, if it can be easily stolen, copied, lost or damaged, then XOR seed splitting will flip the table; the wallet is now our most vulnerable point of failure, so we can now focus on finding our sweet spot between security and convenience with our spending wallet.

## XPUBs and Hardware wallets

For a long term pot which will act as a retirement plan, we don't necessarily need a spending plan, we can create our recovery setup, ensure it is secure and leave it.

If we need to add to the pot over time, we can use a hardware wallet, or a carefully secured device (such as an old laptop that has been factory reset and has no internet or wireless connectivity enabled), to create ourselves an XPUB file.

An XPUB file provides us an extended public key. This key allows wallets to show our balance and our transaction history, to reveal fresh receive addresses, and to create unsigned transactions. We can import it into wallets such as BlueWallet or Sparrow Wallet.

Once we have our XPUB, we can use this to monitor our bitcoin, and to add to it without ever touching our backups.

If we DO want to spend from this wallet periodically, we can use a hardware wallet. A good hardware wallet is air-gapped, pin protected, and will allow you to see and verify your transactions before you sign them.

Again, using an XPUB file, we can do most of the things we want to do with our wallet without ever touching the hardware wallet, and we will only need to use the hardware wallet when we wish to withdraw from our wallet.

## Backing up an existing seed vs creating a new seed

When we create a new wallet, most applications will generate an extended private key for you using a _pseudo-random_ number generator (PRNG).

Unfortunately, it is difficult to tell if the extended private key has been generated maliciously due to compromised hardware, malicious software or viruses. For this reason, it is recommended to roll your own key where possible.

Many wallets that allow you to "restore a wallet" allow you to enter your own seed phrase in the form of 12 or 24 words. Using a dice is a much more reliable way to produce a random extended private key and it is recommended to provide your own seed phrase if your wallet supports it.

If your wallet does not support this, you can still use XOR seed splitting to create a robust backup.
