#### Check flash loans on an interesting protocol

#### Description
This bot listens for flashloans that interact with a list of protocols. 

##### Supported Chains

- Ethereum
- Any other EVM compatible chain

## Alerts

Describe each of the type of alerts fired by this agent

- FORTA-5
  - Fired when a transaction has an Aave3 flash loan in it

## Test Data

The agent behaviour can be verified with the following transactions:

- 0x4c74cfaf9b38c1f4ab4e06819bc60d44171db664ce111190e79cb511e9dfa0d0

And can be tested with: 

```bash
npm run tx 0x4c74cfaf9b38c1f4ab4e06819bc60d44171db664ce111190e79cb511e9dfa0d0
```

# Developers

## Getting started

### Clone the repo and install dependencies

```
git clone https://github.com/PatrickAlphaC/flashloan-forta-py
cd flashloan-forta-py
pip3 install -r requirements_dev.txt
npm install
```

### Run tests

```
pytest
```

### Run the agent

```
npm run start
```
