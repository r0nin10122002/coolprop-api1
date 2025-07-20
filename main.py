from fastapi import FastAPI
from pydantic import BaseModel
from CoolProp.CoolProp import PropsSI

app = FastAPI()

class InputData(BaseModel):
    T1: float  # độ C
    P1: float  # bar
    T2: float  # độ C

@app.post("/calculate")
def calculate_h2(data: InputData):
    try:
        T1_K = data.T1 + 273.15
        T2_K = data.T2 + 273.15
        P1_Pa = data.P1 * 1e5

        s1 = PropsSI("S", "T", T1_K, "P", P1_Pa, "R134a")  # Entropy
        H2 = PropsSI("H", "T", T2_K, "S", s1, "R134a")     # Enthalpy
        H2_kJkg = round(H2 / 1000, 2)  # Chuyển J/kg → kJ/kg

        return {"H2_kJkg": H2_kJkg}

    except Exception as e:
        return {"error": str(e)}
