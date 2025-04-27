import time
import sys
from web3 import Web3
from colorama import init, Fore, Style

# Init colorama nya ges
init(autoreset=True)

# Header info dude
def display_header():
    print(Fore.CYAN + Style.BRIGHT + "===============================")
    print(Fore.YELLOW + Style.BRIGHT + "Auto Daily Claim $RWT Humanity Protocol")
    print(Fore.CYAN + Style.BRIGHT + "Bot created by: WIN")
    print(Fore.YELLOW + Style.BRIGHT + "Join Our Channel at: " + Fore.GREEN + "https://t.me/airdropseeker_official")
    print(Fore.CYAN + Style.BRIGHT + "===============================\n")

# RPC dan koneksi Web3
rpc_url = 'https://rpc.testnet.humanity.org'
web3 = Web3(Web3.HTTPProvider(rpc_url))

if not web3.is_connected():
    print(Fore.RED + "❌ Gagal konek ke Humanity Protocol.")
    sys.exit(1)
else:
    print(Fore.GREEN + "✅ Terkoneksi ke Humanity Protocol.\n")

# Alamat dan ABI kontrak
contract_address = '0xa18f6FCB2Fd4884436d10610E69DB7BFa1bFe8C7'
contract_abi = contract_abi = [{"inputs":[],"name":"AccessControlBadConfirmation","type":"error"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"bytes32","name":"neededRole","type":"bytes32"}],"name":"AccessControlUnauthorizedAccount","type":"error"},{"inputs":[],"name":"InvalidInitialization","type":"error"},{"inputs":[],"name":"NotInitializing","type":"error"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint64","name":"version","type":"uint64"}],"name":"Initialized","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":False,"internalType":"bool","name":"bufferSafe","type":"bool"}],"name":"ReferralRewardBuffered","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"user","type":"address"},{"indexed":True,"internalType":"enum IRewards.RewardType","name":"rewardType","type":"uint8"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"RewardClaimed","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":True,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":True,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":True,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":True,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimBuffer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"claimReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"currentEpoch","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"cycleStartTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"vcContract","type":"address"},{"internalType":"address","name":"tkn","type":"address"}],"name":"init","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"callerConfirmation","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"startTimestamp","type":"uint256"}],"name":"start","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"stop","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"userBuffer","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"epochID","type":"uint256"}],"name":"userClaimStatus","outputs":[{"components":[{"internalType":"uint256","name":"buffer","type":"uint256"},{"internalType":"bool","name":"claimStatus","type":"bool"}],"internalType":"struct IRewards.UserClaim","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"userGenesisClaimStatus","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]
 # <--- paste ABI kamu di sini, sama seperti versi awal kamu jon

# Load kontrak
contract = web3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=contract_abi)

# Fungsi untuk load private keys dari file
def load_private_keys(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

# Fungsi klaim reward
def claim_rewards(private_key):
    try:
        account = web3.eth.account.from_key(private_key)
        sender = account.address

        genesis_claimed = contract.functions.userGenesisClaimStatus(sender).call()
        current_epoch = contract.functions.currentEpoch().call()
        buffer_amount, claimed = contract.functions.userClaimStatus(sender, current_epoch).call()

        if not claimed:
            print(Fore.GREEN + f"🔁 Klaim reward untuk {sender} (Genesis claimed: {genesis_claimed})")
            proceed_to_claim(sender, private_key)
        else:
            print(Fore.YELLOW + f"✅ Reward sudah diklaim untuk {sender} (epoch {current_epoch})")
    except Exception as e:
        if "user not registered" in str(e):
            print(Fore.RED + f"❌ User belum terdaftar: {sender}")
        else:
            print(Fore.RED + f"⚠️ Error saat klaim untuk {sender}: {e}")
# claim
def proceed_to_claim(sender_address, private_key):
    try:
        gas_price = web3.to_wei(5, 'gwei')
        nonce = web3.eth.get_transaction_count(sender_address)
        gas_limit = contract.functions.claimReward().estimate_gas({'from': sender_address})

        transaction = contract.functions.claimReward().build_transaction({
            'chainId': web3.eth.chain_id,
            'from': sender_address,
            'gas': gas_limit,
            'gasPrice': gas_price,
            'nonce': nonce
        })

        signed_tx = web3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx['rawTransaction'])

        print(Fore.CYAN + f"⏳ Menunggu konfirmasi untuk transaksi: {web3.to_hex(tx_hash)}")
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=180)
        print(Fore.GREEN + f"✅ Transaksi sukses untuk {sender_address}, hash: {web3.to_hex(tx_hash)}")

    except Exception as e:
        print(Fore.RED + f"⚠️ Gagal memproses klaim untuk {sender_address}: {str(e)}")


# Main
if __name__ == "__main__":
    display_header()
    try:
        while True:
            keys = load_private_keys('private_keys.txt')
            for pk in keys:
                claim_rewards(pk)

            print(Fore.CYAN + "\n⏳ Menunggu 6 jam sebelum klaim berikutnya... Jangan Lupa Join Channel Kita untuk informasi Airdrop https://t.me/airdropseeker_official\n")
            time.sleep(6 * 60 * 60)

    except KeyboardInterrupt:
        print(Fore.RED + "\n⛔ Dihentikan manual. Sampai jumpa!")
