"""
This script is used to prime your brownie console environment with all the
objects needed to interact with the $GOLD ecosystem. E.g.:
```
$ brownie console
>>> from scripts.primer import *
>>> gold.name()
'GoldenBoys'
>>> inflation.owner()
'0x941dcEA21101A385b979286CC6D6A9Bf435EB1C2'
>>> msig
<GnosisSafeProxy Contract '0x941dcEA21101A385b979286CC6D6A9Bf435EB1C2'>
```
"""

from brownie import Contract, accounts


# tokens
gold = Contract("0xbeFD5C25A59ef2C1316c5A4944931171F30Cd3E4")

# accounts
humpy = accounts.at("0x36cc7B13029B5DEe4034745FB4F24034f3F2ffc6", force=True)
deployer = accounts.at("0x5612dE655956236284963d7D99653354a09cfd39", force=True)
msig = Contract("0x941dcEA21101A385b979286CC6D6A9Bf435EB1C2")

# contracts
inflation = Contract("0x2b55CEd05e9Ff838bcf3581D998468c603648466")
vesting = Contract("0x45AC5B411BcC919D869826DA904Be9Fbab527D22")
injector = Contract("0x79D0F97D4D8c1Dd30b1Ea09746dB8847036AD92d")


def main():
    pass
