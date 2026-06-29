# 🔐 Crypto Talks

> A repository exploring the world of cryptocurrency, blockchain fundamentals, and decentralized finance — including a hackathon project built on Algorand.

---

## 📂 What's in this Repo?

| Part | Description |
|------|-------------|
| 📖 Crypto Research | In-depth notes on blockchain, wallets, consensus, security |
| 🏆 ScholarStream | Hackathon project built at MLSC Algorand Hackspiration |

---

## 📖 Crypto Research & Fundamentals

### Topics Covered

1. **The Core Concept: Decentralization** — How blockchain replaces banks as a trustless middleman
2. **Technological Pillars** — Cryptography, blockchain structure, and consensus mechanisms
3. **Asset Classifications** — Bitcoin (Store of Value), Ethereum/Solana (Smart Contract Platforms), Stablecoins
4. **Proof of Work vs. Proof of Stake** — Energy tradeoffs and how each secures the network
5. **Wallet Infrastructure & Custody** — Custodial vs. self-custody wallets, seed phrases
6. **Hardware Wallets (Cold Storage)** — Trezor, Ledger, Tangem, Coldcard — best practices
7. **Gas Fees & Layer 2 Scaling** — Why fees fluctuate, L1 vs L2 (Arbitrum, Optimism, Base)
8. **Threat Landscape & Scam Prevention** — Quishing, AI deepfakes, approval scams, burner wallets
9. **Emergency Protocols: Revoking Permissions** — Using Revoke.cash and Etherscan Token Approval Checker

---

## 🏆 ScholarStream — MLSC Algorand Hackspiration

> Real-time student allowance streaming + AI financial mentor built on Algorand.

**Team Nexus** — Built at the MLSC Algorand Hackspiration Hackathon

| Team Member | GitHub |
|---|---|
| Shivaji Jamadar | @SHIVAJIJAMADAR |
| Vedant Divate | @TheSleeper25 |
| Nandan Kabra | @n-a-n-d-a-n |
| Prajwal Gidde | @Prajwal-Gidde |

---

### 🚀 Problem Statement

Students are financially unstable not because they lack money — but because the system is poorly designed.
Allowances arrive as lump sums on Day 1. But expenses are continuous.
Due to behavioral bias (hyperbolic discounting), students overspend early and face financial stress by month-end.

**This feast and famine cycle is not a failure of discipline. It is a failure of financial architecture.**

---

### 💡 Solution

ScholarStream is a decentralized financial streaming platform where:
- Funds are released gradually over time based on a smart contract vesting schedule
- Students can only withdraw what has already unlocked — overspending is impossible by design
- An AI financial mentor analyzes on-chain transaction history and provides spending insights

---

### 🏗️ Architecture

Frontend (React + Vite + TypeScript)
↓ Wallet (Pera Connect)
↓ Algorand Smart Contract (ARC4 — Box Storage)
↓ AI Backend (FastAPI + Gemini 2.5 Flash)

---

### ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Blockchain | Algorand, ARC4 Smart Contracts, AlgoKit, TEAL |
| Storage | Box Storage (on-chain) |
| Frontend | React, TypeScript, Vite, Pera Wallet Connect, Algorand SDK |
| AI Backend | Python, FastAPI, Google Gemini 2.5 Flash |
| Indexer | Algorand Testnet Indexer (Algonode) |

---

### 🔐 Smart Contract Features

**Create Stream** — Parent sets beneficiary address, total allowance, and duration

**Real-Time Vesting Logic** — Funds unlock gradually using Global.latest_timestamp; vested = (total x elapsed) / duration

**Withdraw** — Student withdraws only the vested portion; contract tracks withdrawn amount in packed Box storage

**Delegated Withdraw** — Supports authorized third-party withdrawal on behalf of student

---

### 🤖 AI Financial Mentor

- Fetches the student's last 10 on-chain transactions via Algorand Testnet Indexer
- Sends spending data to Gemini 2.5 Flash for analysis
- Returns personalized, conversational budgeting advice
- Lightly roasts overspending behavior to drive engagement

---

### 📊 Project Status

| Component | Status |
|---|---|
| Smart Contract | ✅ 100% Functional |
| Wallet Integration | ✅ Working |
| Frontend UI | ✅ Basic MVP |
| AI Backend | ⚙️ Prototype |
| Full Integration | 🔄 In Progress |

---

### ⚙️ Setup & Run

#### 1. Clone the repo
git clone https://github.com/n-a-n-d-a-n/crypto-talks.git
cd crypto-talks/Hackspiration-main

#### 2. Start Algorand LocalNet
algokit localnet start

#### 3. Deploy the Smart Contract
cd projects/scholar-stream
algokit project run build
algokit project deploy localnet

#### 4. Run the Frontend
cd ../../scholar-frontend
npm install
npm run dev
Visit: http://localhost:5173

#### 5. Run the AI Backend
cd ../scholar-ai-backend
pip install fastapi uvicorn algosdk google-genai
cp .env.example .env
uvicorn app:app --reload

---

### 🔮 Future Enhancements

- Yield While Streaming (DeFi Integration)
- Emergency Buffer Unlock (Controlled Flexibility)
- Mobile wallet deep-link support
- Full frontend to contract integration
- Dashboard with spending graphs

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Nandan Kabra (n-a-n-d-a-n)**
AI & Data Science Student — VIT Pune
🚀 Open Source Enthusiast
