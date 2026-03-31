from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ScholarStream Risk Auditor API")

class WithdrawalData(BaseModel):
    total_stream_amount: int
    withdrawn_amount: int
    elapsed_time_seconds: int
    duration_seconds: int
    requested_withdrawal: int

@app.post("/analyze-risk")
def analyze_risk(data: WithdrawalData):
    # Calculate vesting logic mirroring the Algorand contract
    clamped_elapsed = min(data.elapsed_time_seconds, data.duration_seconds)
    vested = (data.total_stream_amount * clamped_elapsed) // data.duration_seconds
    
    # Analyze the withdrawal behavior
    withdrawal_percentage = (data.requested_withdrawal / data.total_stream_amount) * 100
    
    if withdrawal_percentage >= 50:
        return {
            "status": "CRITICAL",
            "score": 30,
            "advice": "Avoid draining your stream all at once; budget for the entire semester.",
            "reasoning": "Requested withdrawal constitutes a massive lump-sum event, creating high financial instability risk."
        }
    elif withdrawal_percentage >= 20:
        return {
            "status": "WARNING",
            "score": 75,
            "advice": "Keep an eye on your burn rate; you are withdrawing large portions at a time.",
            "reasoning": "Moderate lump-sum behavior detected, straying from the recommended daily fractional withdrawals."
        }
    else:
        return {
            "status": "HEALTHY",
            "score": 95,
            "advice": "Great job pacing your funds.",
            "reasoning": "Small, regular withdrawals align perfectly with the linear vesting design of the smart contract."
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
