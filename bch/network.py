class MainNet():
    TESTNET = False
    WIF_PREFIX = 0x80
    ADDRTYPE_P2PKH = 0
    ADDRTYPE_P2PKH_BITPAY = 28
    ADDRTYPE_P2SH = 5
    ADDRTYPE_P2SH_BITPAY = 40
    CASHADDR_PREFIX = "bitcoincash"

    # Bitcoin Cash fork block specification
    BITCOIN_CASH_FORK_BLOCK_HEIGHT = 478559
    BITCOIN_CASH_FORK_BLOCK_HASH = "000000000000000000651ef99cb9fcbe0dadde1d424bd9f15ff20136191a5eec"

    # Nov 13. 2017 HF to CW144 DAA height (height of last block mined on old DAA)
    CW144_HEIGHT = 504031

    # Note: this is not the Merkle root of the verification block itself , but a Merkle root of
    # all blockchain headers up until and including this block. To get this value you need to
    # connect to an ElectrumX server you trust and issue it a protocol command. This can be
    # done in the console as follows:
    #
    #    network.synchronous_get(("blockchain.block.header", [height, height]))
    #
    # Consult the ElectrumX documentation for more details.
    VERIFICATION_BLOCK_MERKLE_ROOT = "68077352cf309072547164625deb11e92bd379e759e87f3f9ac6e61d1532c536"
    VERIFICATION_BLOCK_HEIGHT = 661942
    # Note: We *must* specify the anchor if the checkpoint is after the anchor, due to the way
    # blockchain.py skips headers after the checkpoint.  So all instances that have a checkpoint
    # after the anchor must specify the anchor as well.

    # Version numbers for BIP32 extended keys
    # standard: xprv, xpub
    XPRV_HEADERS = {
        'standard': 0x0488ade4,
    }

    XPUB_HEADERS = {
        'standard': 0x0488b21e,
    }


class TestNet():
    TESTNET = True
    WIF_PREFIX = 0xef
    ADDRTYPE_P2PKH = 111
    ADDRTYPE_P2PKH_BITPAY = 111  # Unsure
    ADDRTYPE_P2SH = 196
    ADDRTYPE_P2SH_BITPAY = 196  # Unsure
    CASHADDR_PREFIX = "bchtest"
    DEFAULT_UNIT = "tBCH"

    # Nov 13. 2017 HF to CW144 DAA height (height of last block mined on old DAA)
    CW144_HEIGHT = 1155875

    # Bitcoin Cash fork block specification
    BITCOIN_CASH_FORK_BLOCK_HEIGHT = 1155876
    BITCOIN_CASH_FORK_BLOCK_HASH = "00000000000e38fef93ed9582a7df43815d5c2ba9fd37ef70c9a0ea4a285b8f5"

    VERIFICATION_BLOCK_MERKLE_ROOT = "d97d670815829fddcf728fa2d29665de53e83609fd471b0716a49cde383fb888"
    VERIFICATION_BLOCK_HEIGHT = 1421482

    # Version numbers for BIP32 extended keys
    # standard: tprv, tpub
    XPRV_HEADERS = {
        'standard': 0x04358394,
    }

    XPUB_HEADERS = {
        'standard': 0x043587cf,
    }


class TestNet4(TestNet):
    GENESIS = "000000001dd410c49a788668ce26751718cc797474d3152a5fc073dd44fd9f7b"
    TITLE = 'Electron Cash Testnet4'

    BITCOIN_CASH_FORK_BLOCK_HEIGHT = 6
    BITCOIN_CASH_FORK_BLOCK_HASH = "00000000d71b9b1f7e13b0c9b218a12df6526c1bcd1b667764b8693ae9a413cb"

    # Nov 13. 2017 HF to CW144 DAA height (height of last block mined on old DAA)
    CW144_HEIGHT = 3000

    VERIFICATION_BLOCK_MERKLE_ROOT = "9ca8933d4aa7b85093e3ec317e40bdfeda3e2b793fcd7907b38580fa193d9c77"
    VERIFICATION_BLOCK_HEIGHT = 16845


class ScaleNet(TestNet):
    GENESIS = "00000000e6453dc2dfe1ffa19023f86002eb11dbb8e87d0291a4599f0430be52"
    TITLE = 'Electron Cash Scalenet'
    BASE_UNITS = {'sBCH': 8, 'msBCH': 5, 'sbits': 2}
    DEFAULT_UNIT = "tBCH"

    BITCOIN_CASH_FORK_BLOCK_HEIGHT = 6
    BITCOIN_CASH_FORK_BLOCK_HASH = "000000000e16730d293050fc5fe5b0978b858f5d9d91192a5ca2793902493597"

    # Nov 13. 2017 HF to CW144 DAA height (height of last block mined on old DAA)
    CW144_HEIGHT = 3000

    VERIFICATION_BLOCK_MERKLE_ROOT = "41eb32849a353fcb408c8b25e84578c714dbdc5ee774d0fbe25e85755250df6a"
    VERIFICATION_BLOCK_HEIGHT = 2016


class TaxCoinNet():
    """ This is for supporting ABC tax coin. Use CLI arg --taxcoin to see this network.
    Users using this network cannot see BCH and vice-versa, due to the checkpoint block.
    If one wants to see both chains one can run 2 clients since they will use different data
    directories. """
    TESTNET = False
    WIF_PREFIX = 0x80
    ADDRTYPE_P2PKH = 0
    ADDRTYPE_P2PKH_BITPAY = 28
    ADDRTYPE_P2SH = 5
    ADDRTYPE_P2SH_BITPAY = 40
    CASHADDR_PREFIX = "bitcoincash"
    GENESIS = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
    TITLE = "Electron Tax - 'Ard Moné Edition"
    BASE_UNITS = {'TAX': 8, 'mTAX': 5, 'sechets': 2}
    DEFAULT_UNIT = "TAX"

    # Bitcoin Cash fork block specification
    BITCOIN_CASH_FORK_BLOCK_HEIGHT = 478559
    BITCOIN_CASH_FORK_BLOCK_HASH = "000000000000000000651ef99cb9fcbe0dadde1d424bd9f15ff20136191a5eec"

    # Nov 13. 2017 HF to CW144 DAA height (height of last block mined on old DAA)
    CW144_HEIGHT = 504031

    # Note: this is not the Merkle root of the verification block itself , but a Merkle root of
    # all blockchain headers up until and including this block. To get this value you need to
    # connect to an ElectrumX server you trust and issue it a protocol command. This can be
    # done in the console as follows:
    #
    #    network.synchronous_get(("blockchain.block.header", [height, height]))
    #
    # Consult the ElectrumX documentation for more details.
    VERIFICATION_BLOCK_MERKLE_ROOT = "d0d925862df595918416020caf5467b7ae67ae8f807daf60626c36755b62f9a2"
    VERIFICATION_BLOCK_HEIGHT = 661648  # ABC fork block

    # Version numbers for BIP32 extended keys
    # standard: xprv, xpub
    XPRV_HEADERS = {
        'standard': 0x0488ade4,
    }

    XPUB_HEADERS = {
        'standard': 0x0488b21e,
    }