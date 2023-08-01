##### **flashloan-forta-py**

**📝Description:**
This repository contains a bot that monitors flash loans interacting with a specified list of protocols on supported chains, including Ethereum and other EVM compatible chains.

**Supported Chains:**
- --> Ethereum
- --> Any other EVM compatible chain

**⚠️ Alerts:**
The bot can fire alerts of different types. One specific alert is FORTA-5, which occurs when a transaction involves an Aave3 flash loan.

**Test Data:**
The agent's behavior can be verified using the following transaction:
`0x4c74cfaf9b38c1f4ab4e06819bc60d44171db664ce111190e79cb511e9dfa0d0`
It can also be tested using the command:
`npm run tx 0x4c74cfaf9b38c1f4ab4e06819bc60d44171db664ce111190e79cb511e9dfa0d0`

### Getting Started as a Developer
**Developers:**
To get started with this project, follow these steps:
1. Clone the repository and install the required dependencies:
```
git clone https://github.com/PatrickAlphaC/flashloan-forta-py
cd flashloan-forta-py
pip3 install -r requirements_dev.txt
npm install
```
2. Run tests to ensure everything is set up correctly:
```
pytest
```
3. Start the agent:
```
npm run start
```

Feel free to explore and contribute to this project by making pull requests, using actions, managing projects, updating the wiki, ensuring security, and checking insights in the settings.
