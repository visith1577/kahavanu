from scripts.helpful_scripts import get_account
from brownie import KahavanuToken
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")  # 1000
token_name = "Kahavanu"
token_symbol = "KHV"


def main():
    account = get_account()
    KahavanuToken.deploy(initial_supply, {"from": account})


