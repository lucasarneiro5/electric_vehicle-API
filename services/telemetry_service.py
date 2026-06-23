import random
from datetime import datetime


def gerar_telemetria():
    return {
        "veiculo_id": f"EV{random.randint(1, 10):03d}",
        "bateria": random.randint(20, 100),
        "velocidade": round(random.uniform(0, 120), 1),
        "gps": {
            "latitude": round(random.uniform(-23.0, -21.0), 6),
            "longitude": round(random.uniform(-44.0, -42.0), 6)
        },
        "data_hora": datetime.now().isoformat()
    }