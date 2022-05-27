## Motivation

When you set up a self-custodial wallet, you are usually asked to create a backup of your private key.

Unfortunately, not much advice is given as to how we should write down and store our backups.

If we make only a single backup, we have a chance of losing or accidentally destroying the backup; this means we could lose access to the bitcoin that we saved.

If we make multiple backups, we increase the odds of leaking our backup, or having a copy stolen; this means we someone could take the bitcoin that we saved.

A single 24 word seed phrase is like a hot potato, and most _**naive**_ attempts to split a backup into multiple parts will compromise our security ([Why is seed splitting a bad idea? - youtube video](https://www.youtube.com/watch?v=p5nSibpfHYE)), but what if we could split our secret into multiple parts without compromising on security?

> Note: Shamir's secret sharing scheme (aka SSSS) is a good way to split a secret without compromising on security as explained by Andreas Aantonopolous in the video linked above, but this method is simpler and can be mostly done with a dice, pen and paper.

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

## An ephemeral private key

An ephemeral private key, is one that exists temporarily, but is then forgotten or destroyed.

When considering a backup strategy for your bitcoin wallet, any written or stored record of your wallet's private key is a single point of failure; if it were to get leaked or fall into the hands of a criminal, they would have full access to steal your bitcoin!

By keeping your wallet's private key ephemeral, you remove this single point of failure, and any chance of stealing your funds, now relies on an attacker being able to find one of each of your backups across your isolated domains.

## Seed splitting vs Multisig

TODO: Explain multi-sig is better, but more complicated

## Hardware wallets

TODO: Explain harware wallets for convenience, only if necessary, XPUB for extra security

## Backing up an existing seed vs creating a new seed

TODO: Describe benefit of dice roll and how to use your own seed in wallets.