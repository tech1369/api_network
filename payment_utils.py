import requests
import json
from decimal import Decimal

# USDT Contract Address on Ethereum
USDT_CONTRACT = "0xdAC17F958D2ee523a2206206994597C13D831ec7"

# Your Trust Wallet Address
YOUR_WALLET_ADDRESS = "0xA3C369cA91e1F851b7224268F2555aE9711e4815"

def check_usdt_payment(required_amount, transaction_hash=None):
    """
    Check if USDT payment has been received
    Args:
        required_amount: Amount in USDT (e.g., 0.15 for $0.15)
        transaction_hash: Optional transaction hash to verify specific payment
    Returns:
        dict: Payment status and details
    """
    try:
        # Using Etherscan API to check USDT transactions
        api_key = "YourEtherscanAPIKey"  # Get free API key from etherscan.io
        
        if transaction_hash:
            # Check specific transaction
            url = f"https://api.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash={transaction_hash}&apikey={api_key}"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('result'):
                    # Verify transaction details
                    tx = data['result']
                    if tx['to'].lower() == USDT_CONTRACT.lower():
                        # This is a USDT transaction, decode the amount
                        return verify_usdt_transaction(tx, required_amount)
        
        # Check recent transactions to wallet
        url = f"https://api.etherscan.io/api?module=account&action=tokentx&contractaddress={USDT_CONTRACT}&address={YOUR_WALLET_ADDRESS}&page=1&offset=10&sort=desc&apikey={api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('result'):
                for tx in data['result']:
                    # Check if payment matches required amount
                    amount = Decimal(tx['value']) / Decimal(10**6)  # USDT has 6 decimals
                    if amount >= Decimal(str(required_amount)):
                        return {
                            "status": "paid",
                            "amount": float(amount),
                            "transaction_hash": tx['hash'],
                            "timestamp": tx['timeStamp']
                        }
        
        return {"status": "pending", "required_amount": required_amount}
        
    except Exception as e:
        return {"status": "error", "message": str(e)}

def verify_usdt_transaction(tx, required_amount):
    """Verify USDT transaction details"""
    try:
        # Decode USDT transfer data
        input_data = tx['input']
        if len(input_data) >= 138:  # Standard USDT transfer
            # Extract amount from transaction data
            amount_hex = input_data[-64:]
            amount = int(amount_hex, 16) / (10**6)  # USDT has 6 decimals
            
            if amount >= required_amount:
                return {
                    "status": "paid",
                    "amount": amount,
                    "transaction_hash": tx['hash']
                }
        
        return {"status": "invalid", "message": "Payment amount insufficient"}
        
    except Exception as e:
        return {"status": "error", "message": str(e)}

def generate_payment_request(amount, api_endpoint):
    """Generate payment request details"""
    return {
        "payment_address": YOUR_WALLET_ADDRESS,
        "amount_usdt": amount,
        "network": "Ethereum",
        "contract_address": USDT_CONTRACT,
        "api_endpoint": api_endpoint,
        "instructions": f"Send {amount} USDT to the address above, then call the API with your transaction hash"
    }
