from fastapi import FastAPI
from CoolProp.CoolProp import PropsSI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "CoolProp API is running!"}

@app.get("/get_h2")
def get_h2(T1: float, P1: float, T2: float):
    try:
        P1_Pa = P1 * 1e5  # bar to Pa
        s1 = PropsSI("S", "T", T1 + 273.15, "P", P1_Pa, "R134a")
        h2 = PropsSI("H", "T", T2 + 273.15, "S", s1, "R134a")
        return {"H2_kJ_per_kg": round(h2 / 1000, 2)}
    except Exception as e:
        return {"error": str(e)}
