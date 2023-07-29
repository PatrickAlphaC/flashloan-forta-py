# A way for me to find a sample flash loan on aave v3
# You can ignore this code
from alchemy_sdk_py import Alchemy

AAVE_V3_ADDRESS: str = "0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2"
FLASH_LOAN_TOPIC: str = (
    "0xefefaba5e921573100900a3ad9cf29f222d995fb3b6045797eaea7521bd8d6f0"
)

alchemy = Alchemy()

events = alchemy.get_events(AAVE_V3_ADDRESS, [FLASH_LOAN_TOPIC], 0, 17795072)
print(events)
