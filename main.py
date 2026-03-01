from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from typing import List

app = FastAPI(title="RC Circuit Simulator API")

class SimulationParams(BaseModel):
    resistance: float  # Ohms
    capacitance: float # Farads
    voltage: float     # Volts
    duration: float = 0.5 # Seconds (reduced for better responsiveness)
    steps: int = 200

class SimulationResult(BaseModel):
    time: List[float]
    charge: List[float]
    current: List[float]
    voltage_c: List[float]
    time_constant: float

@app.post("/simulate", response_model=SimulationResult)
async def simulate_rc(params: SimulationParams):
    if params.resistance <= 0 or params.capacitance <= 0:
        raise HTTPException(status_code=400, detail="Resistance and Capacitance must be positive.")

    tau = params.resistance * params.capacitance
    # Use duration proportional to tau for better visualization, but capped.
    duration = min(params.duration, 5 * tau) 
    t = np.linspace(0, duration, params.steps)
    
    # Q(t) = C * V * (1 - e^(-t/RC))
    charge = params.capacitance * params.voltage * (1 - np.exp(-t / tau))
    
    # I(t) = (V/R) * e^(-t/RC)
    current = (params.voltage / params.resistance) * np.exp(-t / tau)
    
    # Vc(t) = V * (1 - e^(-t/RC))
    voltage_c = params.voltage * (1 - np.exp(-t / tau))

    return SimulationResult(
        time=t.tolist(),
        charge=charge.tolist(),
        current=current.tolist(),
        voltage_c=voltage_c.tolist(),
        time_constant=tau
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
