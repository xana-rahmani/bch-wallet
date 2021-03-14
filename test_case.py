from wallet import PublicKey
from bch.network import TestNet

public_keys_to_address = [
    {
        "public_key": "03544d5db5398d37196fe11bae89fa590db2b2d2087a949ffa9c0300c85e9be9af",
        "cash_address": "qzuxja723cpp8kuva4cvxer2dsd69wgyvqa7vf5v44",
        "cash_address_with_prefix": "bitcoincash:qzuxja723cpp8kuva4cvxer2dsd69wgyvqa7vf5v44",
        "legacy_address": "1Hp5gLZrxa6ZYvg2SC1KQ7g2a7Mh2JGqVJ",
    },
    {
        "public_key": "03066694c0b5ee49f319588d6b38cbbe9983879fb0638ad96119a07f0e17cedab3",
        "cash_address": "qqdr2z09rva6tcjwun3ftpcgf2kxs66435adqm7whs",
        "cash_address_with_prefix": "bitcoincash:qqdr2z09rva6tcjwun3ftpcgf2kxs66435adqm7whs",
        "legacy_address": "13Pa7BJwadY82cemb7nhWETmd6d6GW6jMb"
    }
]

# Testnet
t_public_keys_to_address = [
    {
        "public_key": "03f9c03eab73979482a7d521ea9358e808bf476a7fe8c5434a5fbdd74767742c76",
        "cash_address": "qrkzgjcgnwafngfdcrgaxk4gs0anx56peuk080zfrv",
        "cash_address_with_prefix": "bchtest:qrkzgjcgnwafngfdcrgaxk4gs0anx56peuk080zfrv",
        "legacy_address": "n33ZF1p3yQPXnJxsK7Mta5YxcwFPSssywx",
    },
    {
        "public_key": "0372445db5c0950bb44d92c72d60d0cb70bdd96a3e82f676af54098bb7fdad35cd",
        "cash_address": "qzzsac8up9srue7ylfklk0w6ekneqns6ucaw43f9ya",
        "cash_address_with_prefix": "bchtest:qzzsac8up9srue7ylfklk0w6ekneqns6ucaw43f9ya",
        "legacy_address": "mseVzNHWsAcGJ1zwJKxKmj9734aKpb1w6m"
    }
]

for p in public_keys_to_address:
    publicKey = PublicKey(p.get("public_key"))
    assert (publicKey.public_key_is_valid())
    assert (publicKey.public_key_is_compressed() == False)
    assert (p.get("cash_address") == publicKey.public_key_to_cash_address())
    assert (p.get("cash_address_with_prefix") == publicKey.public_key_to_cash_address(with_prefix=True))
    assert (p.get("legacy_address") == publicKey.public_key_to_legacy_address())


for p in t_public_keys_to_address:
    publicKey = PublicKey(p.get("public_key"), network=TestNet)
    assert (publicKey.public_key_is_valid())
    assert (publicKey.public_key_is_compressed() == False)
    assert (p.get("cash_address") == publicKey.public_key_to_cash_address())
    assert (p.get("cash_address_with_prefix") == publicKey.public_key_to_cash_address(with_prefix=True))
    assert (p.get("legacy_address") == publicKey.public_key_to_legacy_address())
