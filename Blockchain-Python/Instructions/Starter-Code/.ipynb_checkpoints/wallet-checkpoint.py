import os
import subprocess
import json
from constant import *
from bit import wif_to_key
import bit 
import web3
from web3 import Web3
from eth_account import Account
from web3.middleware import geth_poa_middleware

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

def derive_wallets(coin, numderive):
    mnemonic = os.getenv('MNEMONIC', "river uphold key roof estate silver word person vapor decrease ribbon angle")
    command = f'./derive -g --mnemonic="{mnemonic}" --coin={coin} --numderive={numderive} --cols=path,address,privkey,pubkey --format=json'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()

    return json.loads(output.decode('utf-8'))


def priv_key_to_account(coin, priv_key):

    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)

    if coin == BTCTEST:
        return bit.PrivateKeyTestnet(priv_key)

def create_tx(coin, account, to, amount):
    
    if coin == ETH:
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)    
        gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": to, "value": amount}
        )
        return {
            "from": account.address,
            "to": to,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address)
        }

    if coin == BTCTEST:
        return bit.PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])


def send_tx(coin, account, to, amount):

    tx = create_tx(coin, account, to, amount)
    signed_tx = account.sign_transaction(tx)
    if coin == ETH:
        return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    if coin == BTCTEST:
        return bit.network.NetworkAPI.broadcast_tx_testnet(signed_tx)



if __name__ == "__main__":
    coin = BTCTEST
    numderive = 3
    btc_test_key = {'btc-test': derive_wallets(coin, numderive)}
    print(json.dumps(btc_test_key, indent=4, sort_keys=True))

    coin = ETH
    eth_key = {'eth': derive_wallets(coin, numderive)}
    print(json.dumps(eth_key, indent=4, sort_keys=True))

