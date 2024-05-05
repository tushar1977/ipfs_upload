import requests
from dotenv import load_dotenv
import os
import random
from web3 import Web3
import json

load_dotenv()

private_key = os.getenv("PRIVATE_KEY")
chain_id = 0x14A34

account_address = "0xfB54504aaFa7D6C90ae8c115f44203d8Bf8A573a"

contract_address = "0x42Aa8b7905a603F42332f634daB323Cf2f5F7437"
url = "https://base-sepolia.g.alchemy.com/v2/ry0RpisMZsHyMTeS9y2SyEGqV-pMuxwO"

jsonfile = "abi.json"

with open(jsonfile, "r") as f:
    abi = json.load(f)


web3 = Web3(Web3.HTTPProvider(url))
contract = web3.eth.contract(address=contract_address, abi=abi)


def upload_to_pinata(filepath, jwt_token):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {"Authorization": f"Bearer {jwt_token}"}
    metadata_path = "./metadata.json"
    with open(metadata_path, "r") as f:
        metadata = json.load(f)

    with open(filepath, "rb") as file:
        response = requests.post(
            url,
            headers=headers,
            files={"file": file},
            json=metadata,
        )

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}


def get_pinata(jwt_token):
    url = "https://api.pinata.cloud/data/pinList"
    headers = {"Authorization": f"Bearer {jwt_token}"}

    response = requests.get(url, headers=headers)

    return response.json()


def upload_to_contract(id, url, address, key):
    tx = contract.functions.addImage(id, url).build_transaction(
        {
            "chainId": chain_id,
            "gas": 3000000,
            "gasPrice": web3.to_wei("1", "gwei"),
            "nonce": web3.eth.get_transaction_count(address),
        }
    )

    signed_tx = web3.eth.account.sign_transaction(tx, private_key=key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt


def return_img(address):
    tx = contract.functions.getUserImages(address).call()
    return tx


jwt = os.getenv("TOKEN")
file_path = "./ipfs/5.jpeg"

generated_img = "https://ipfs.io/ipfs/" + upload_to_pinata(file_path, jwt)["IpfsHash"]
# print(upload_to_contract(1, generated_img, account_address, private_key))
data = return_img(account_address)

for i in range(len(data[0])):
    print([data[0][i], data[1][i]])
