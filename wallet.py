from bch.network import MainNet
from bch.crypto import hash_160, sha256, base_58_encode
from bch.cash_address import _pack_addr_data, _create_checksum, _CHARSET

class PublicKey:
    def __init__(self, public_key, network=None):
        self.public_key = public_key
        if network is None:
            self.network = MainNet
        else:
            self.network = network

    def public_key_is_compressed(self):
        """ Returns True if the pubkey is compressed. """
        return len(self.public_key) == 33

    def public_key_is_valid(self, pubkey=None):
        if pubkey is None:
            pubkey = self.public_key
        pubkey = bytes.fromhex(pubkey)
        if len(pubkey) == 33 and pubkey[0] in (2, 3):
            return True  # Compressed
        if len(pubkey) == 65 and pubkey[0] == 4:
            return True  # Uncompressed
        return False

    def public_key_to_cash_address(self, with_prefix=False):
        hash160 = hash_160(bytes.fromhex(self.public_key))
        kind = 0  # PUBKEY_TYPE = 0, SCRIPT_TYPE = 1
        prefix = self.network.CASHADDR_PREFIX

        payload = _pack_addr_data(kind, hash160)
        checksum = _create_checksum(prefix, payload)
        cash_address = ''.join([_CHARSET[d] for d in (payload + checksum)])
        if with_prefix:
            return '{}:{}'.format(self.network.CASHADDR_PREFIX, cash_address)
        return cash_address

    def public_key_to_legacy_address(self):
        hash160 = hash_160(bytes.fromhex(self.public_key))
        verbyte = self.network.ADDRTYPE_P2PKH

        payload = bytes([verbyte]) + hash160
        checksum = sha256(sha256(payload))[0:4]

        legacy_address = base_58_encode(payload + checksum)
        return legacy_address
