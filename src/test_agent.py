from typing import List
from unittest.mock import Mock

from forta_agent import (
    FindingSeverity,
    FindingType,
    create_transaction_event,
    transaction_event,
)
from forta_agent.transaction_event import TransactionEvent

from agent import AAVE_V3_ADDRESS, FLASH_LOAN_TOPIC, PROTOCOL, handle_transaction

# This should be a pytest fixture in conftest...
mock_tx_event: TransactionEvent = create_transaction_event(
    {"transaction": {"hash": "0x1234"}, "addresses": {"0x1234": True}}
)
mock_tx_event.filter_log = Mock()


class TestFlashLoanDetector:
    def test_returns_empty_if_not_aave_contract(self):
        findings: List[transaction_event.TransactionEvent] = handle_transaction(
            mock_tx_event
        )
        assert len(findings) == 0

    def test_returns_empty_if_no_flash_loan_events(self):
        mock_tx_event.filter_log.reset_mock()
        mock_tx_event.addresses = {AAVE_V3_ADDRESS: True}
        findings: List[transaction_event.TransactionEvent] = handle_transaction(
            mock_tx_event
        )
        assert len(findings) == 0

    def test_returns_finding_if_it_sees_a_flash_loan(self):
        mock_tx_event.filter_log.reset_mock()
        mock_tx_event.addresses = {AAVE_V3_ADDRESS: True, PROTOCOL: True}
        mock_tx_event.logs = [
            {"topics": [FLASH_LOAN_TOPIC], "address": AAVE_V3_ADDRESS}
        ]
        findings: List[transaction_event.TransactionEvent] = handle_transaction(
            mock_tx_event
        )
        assert len(findings) == 1
