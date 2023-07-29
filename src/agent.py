from typing import List

from forta_agent import (
    Finding,
    FindingSeverity,
    FindingType,
    get_transaction_receipt,
    receipt,
    transaction_event,
)

AAVE_V3_ADDRESS: str = "0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2".lower()
# function flashLoan( address receiverAddress, address[] calldata assets, uint256[] calldata amounts, uint256[] interestRateModes, address onBehalfOf, bytes calldata params, uint16 referralCode)
# cast keccak "FlashLoan(address,address,address,uint256,uint8,uint256,uint16)"
FLASH_LOAN_TOPIC: str = (
    "0xefefaba5e921573100900a3ad9cf29f222d995fb3b6045797eaea7521bd8d6f0".lower()
)

PROTOCOL = "0xdAC17F958D2ee523a2206206994597C13D831ec7".lower()
INTERESTING_PROTOCOLS: List[str] = [PROTOCOL]
HIGH_GAS_THRESHOLD: int = 7000000
BALANCE_DIFF_THRESHOLD: int = 200_000_000_000_000_000_000  # 200 ETH


def handle_transaction(
    transaction_event: transaction_event,
) -> List[transaction_event.TransactionEvent]:
    findings: List[transaction_event.TransactionEvent] = []

    addresses_lowered = [key.lower() for key in transaction_event.addresses.keys()]

    if AAVE_V3_ADDRESS not in addresses_lowered:
        return findings

    flash_loan_events = []
    # We check for a flash loan topic from Aave in the list of events
    for log in transaction_event.logs:
        for topic in log["topics"]:
            if topic.lower() == FLASH_LOAN_TOPIC:
                if log["address"].lower() == AAVE_V3_ADDRESS:
                    flash_loan_events.append(log)

    if len(flash_loan_events) == 0:
        return findings

    for address in INTERESTING_PROTOCOLS:
        if address in transaction_event.addresses:
            findings.append(
                Finding(
                    {
                        "name": "Potential flash loan on our contract",
                        "description": f"Flash Loan detechted one of the interesting protocols on hash: {transaction_event.hash}",
                        "alert_id": "FORTA-5",
                        "protocol": "aave",
                        "type": FindingType.Suspicious,
                        "severity": FindingSeverity.Low,
                        "metadata": {
                            "protocolAddress": transaction_event.addresses,
                        },
                    }
                )
            )
            return findings
    return findings


# def initialize():
#     # do some initialization on startup e.g. fetch data

# def handle_block(block_event):
#     findings = []
#     # detect some block condition
#     return findings

# def handle_alert(alert_event):
#     findings = []
#     # detect some alert condition
#     return findings
