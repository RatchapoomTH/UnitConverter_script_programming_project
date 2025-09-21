#volume.py
%%writefile converter3/volume.py
def l_to_ml(l: float):
    ml = l * 1000
    return ml, f"{l:.2f} L = {ml:.2f} mL"

def ml_to_l(ml: float):
    l = ml / 1000
    return l, f"{ml:.2f} mL = {l:.2f} L"

def tbsp_to_tsp(tbsp: float):
    tsp = tbsp * 3
    return tsp, f"{tbsp:.2f} Tbsp = {tsp:.2f} Tsp"

def tsp_to_tbsp(tsp: float):
    tbsp = tsp / 3
    return tbsp, f"{tsp:.2f} Tsp = {tbsp:.2f} Tbsp"
