# RC Circuit Lab 3D - Backend

Backend service for the **RC Circuit 3D Physics Laboratory Simulator**.  
This API is responsible for handling physics calculations, experiment logic, and communication with the Kotlin Multiplatform frontend.

The backend is implemented using **FastAPI** and provides endpoints to simulate the behavior of RC circuits such as capacitor charging, discharging, and time constant calculations.

---

## 🚀 Features

- RC circuit simulation endpoints
- Capacitor charge and discharge calculations
- Time constant computation (τ = RC)
- Experiment data processing
- RESTful API for frontend communication
- Modular and scalable FastAPI architecture

---
![WhatsApp Image 2026-03-01 at 1 45 39 PM](https://github.com/user-attachments/assets/8fc518cb-0aa7-4748-98b2-eeb63ce49975)


## 🧪 Physics Model

The simulator models the behavior of a **Resistor-Capacitor (RC) circuit**, where the voltage across the capacitor changes exponentially over time.

Charging equation:
