# ScholarStream

ScholarStream is an Algorand-based dApp designed to stream educational funds to students securely. The project includes an ARC4 smart contract for linear vesting and a Risk Auditor API to monitor and advise students on their financial health.

## Components
* **Smart Contract (`contracts/`)**: Written in Algopy. Manages the initialization of the stream and enforces linear vesting based on network timestamps.
* **Backend Auditor (`backend/`)**: A FastAPI service that analyzes withdrawal requests and assigns a Health Score (0-100) to ensure students pace their funds responsibly.
* **Frontend (`frontend/`)**: A React interface allowing students to check their risk score and interact with the Algorand blockchain to withdraw their vested ALGO.

## Quick Start
1. **Contract**: Compile and deploy `contract.py` using AlgoKit.
2. **Backend**: Run `pip install -r requirements.txt` followed by `python main.py`.
3. **Frontend**: Run `npm install` and `npm start` to boot the student dashboard.
