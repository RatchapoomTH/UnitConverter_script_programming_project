#volume.py
%%writefile converter2/volume.py
ML_PER_L = 1000
ML_PER_TBSP = 15
ML_PER_TSP = 5

def liter_to_milliliter(l: float):
    if l < 0:
        return None, "❌ Volume cannot be negative."
    ml = l * ML_PER_L
    return ml, f"{l:.4f} L = {ml:.4f} mL"

def milliliter_to_liter(ml: float):
    if ml < 0:
        return None, "❌ Volume cannot be negative."
    l = ml / ML_PER_L
    return l, f"{ml:.4f} mL = {l:.4f} L"

def liter_to_tbsp(l: float):
    if l < 0:
        return None, "❌ Volume cannot be negative."
    tbsp = (l * ML_PER_L) / ML_PER_TBSP
    return tbsp, f"{l:.4f} L = {tbsp:.4f} Tbsp"

def tbsp_to_liter(tbsp: float):
    if tbsp < 0:
        return None, "❌ Volume cannot be negative."
    l = (tbsp * ML_PER_TBSP) / ML_PER_L
    return l, f"{tbsp:.4f} Tbsp = {l:.4f} L"

def liter_to_tsp(l: float):
    if l < 0:
        return None, "❌ Volume cannot be negative."
    tsp = (l * ML_PER_L) / ML_PER_TSP
    return tsp, f"{l:.4f} L = {tsp:.4f} Tsp"

def tsp_to_liter(tsp: float):
    if tsp < 0:
        return None, "❌ Volume cannot be negative."
    l = (tsp * ML_PER_TSP) / ML_PER_L
    return l, f"{tsp:.4f} Tsp = {l:.4f} L"

def milliliter_to_tbsp(ml: float):
    if ml < 0:
        return None, "❌ Volume cannot be negative."
    tbsp = ml / ML_PER_TBSP
    return tbsp, f"{ml:.4f} mL = {tbsp:.4f} Tbsp"

def tbsp_to_milliliter(tbsp: float):
    if tbsp < 0:
        return None, "❌ Volume cannot be negative."
    ml = tbsp * ML_PER_TBSP
    return ml, f"{tbsp:.4f} Tbsp = {ml:.4f} mL"

def milliliter_to_tsp(ml: float):
    if ml < 0:
        return None, "❌ Volume cannot be negative."
    tsp = ml / ML_PER_TSP
    return tsp, f"{ml:.4f} mL = {tsp:.4f} Tsp"

def tsp_to_milliliter(tsp: float):
    if tsp < 0:
        return None, "❌ Volume cannot be negative."
    ml = tsp * ML_PER_TSP
    return ml, f"{tsp:.4f} Tsp = {ml:.4f} mL"

def tbsp_to_tsp(tbsp: float):
    if tbsp < 0:
        return None, "❌ Volume cannot be negative."
    tsp = (tbsp * ML_PER_TBSP) / ML_PER_TSP
    return tsp, f"{tbsp:.4f} Tbsp = {tsp:.4f} Tsp"

def tsp_to_tbsp(tsp: float):
    if tsp < 0:
        return None, "❌ Volume cannot be negative."
    tbsp = (tsp * ML_PER_TSP) / ML_PER_TBSP
    return tbsp, f"{tsp:.4f} Tsp = {tbsp:.4f} Tbsp"
