# converter3/main.py
import gradio as gr
import datetime, json

# import conversion modules
from converter3.temperature import fahrenheit_to_celsius, celsius_to_fahrenheit, celsius_to_kelvin, kelvin_to_celsius
from converter3.weight import kg_to_lb, lb_to_kg
from converter3.time_converter import hr_to_min, min_to_hr, min_to_sec, sec_to_min
from converter3.length import m_to_km, km_to_m, m_to_cm, cm_to_m
from converter3.volume import l_to_ml, ml_to_l, tbsp_to_tsp, tsp_to_tbsp
from converter3.parser import parse_input

# import parser
from converter3.parser import parse_input

# Google Sheet setup
import gspread, google.auth
from google.colab import auth

# authenticate Google
auth.authenticate_user()
creds, _ = google.auth.default()
gc = gspread.authorize(creds)

SPREADSHEET_NAME = "UnitConverterHistory_webGUI"
try:
    sh = gc.open(SPREADSHEET_NAME)
except gspread.SpreadsheetNotFound:
    sh = gc.create(SPREADSHEET_NAME)

ws = sh.sheet1

# create header if empty
if not ws.get_all_values():
    header = ["id","timestamp","category","from_unit","to_unit","input","outputs_json","message"]
    ws.append_row(header)

# auto-increment record_id
def get_next_id():
    all_rows = ws.get_all_values()
    if len(all_rows) <= 1:
        return 1
    else:
        last_id = int(all_rows[-1][0])
        return last_id + 1

def save_conversion(record_id, category, from_unit, to_unit, input_val, outputs, message=""):
    ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
    row = [record_id, ts, category, from_unit, to_unit, input_val, json.dumps(outputs, ensure_ascii=False), message]
    ws.append_row(row)
    print(f"✅ Saved row {record_id} to Google Sheet at {ts} UTC.")

# main conversion function
def convert(input_text):
    category, unit, value, msg = parse_input(input_text)
    if msg:
        return msg

    outputs = {}
    result_msg = ""

    try:
        if category == "temperature":
            if unit.lower() in ["c", "°c"]:
                f, _ = celsius_to_fahrenheit(value)
                k, _ = celsius_to_kelvin(value)
                outputs = {"fahrenheit": f, "kelvin": k}
                result_msg = f"{value} °C → {f:.2f} °F, {k:.2f} K"
            elif unit.lower() in ["f", "°f"]:
                c, _ = fahrenheit_to_celsius(value)
                k, _ = celsius_to_kelvin(c)
                outputs = {"celsius": c, "kelvin": k}
                result_msg = f"{value} °F → {c:.2f} °C, {k:.2f} K"
            elif unit.lower() in ["k"]:
                c, _ = kelvin_to_celsius(value)
                f, _ = celsius_to_fahrenheit(c)
                outputs = {"celsius": c, "fahrenheit": f}
                result_msg = f"{value} K → {c:.2f} °C, {f:.2f} °F"

        elif category == "weight":
            if unit == "kg":
                lb, _ = kg_to_lb(value)
                outputs = {"lb": lb}
                result_msg = f"{value} kg → {lb:.2f} lb"
            else:
                kg, _ = lb_to_kg(value)
                outputs = {"kg": kg}
                result_msg = f"{value} lb → {kg:.2f} kg"

        elif category == "time":
            if unit in ["hr","h"]:
                m, _ = hr_to_min(value)
                outputs = {"min": m}
                result_msg = f"{value} hr → {m:.2f} min"
            elif unit=="min":
                hr, _ = min_to_hr(value)
                s, _ = min_to_sec(value)
                outputs = {"hr": hr, "sec": s}
                result_msg = f"{value} min → {hr:.2f} hr, {s:.2f} sec"
            else:
                m, _ = sec_to_min(value)
                outputs = {"min": m}
                result_msg = f"{value} sec → {m:.2f} min"

        elif category == "length":
            if unit=="m":
                km, _ = m_to_km(value)
                cm, _ = m_to_cm(value)
                outputs = {"km": km, "cm": cm}
                result_msg = f"{value} m → {km:.2f} km, {cm:.2f} cm"
            elif unit=="km":
                m_val, _ = km_to_m(value)
                outputs = {"m": m_val}
                result_msg = f"{value} km → {m_val:.2f} m"
            else:
                m_val, _ = cm_to_m(value)
                outputs = {"m": m_val}
                result_msg = f"{value} cm → {m_val:.2f} m"

        elif category == "volume":
            if unit=="l":
                ml, _ = l_to_ml(value)
                outputs = {"ml": ml}
                result_msg = f"{value} L → {ml:.2f} mL"
            elif unit=="ml":
                l_val, _ = ml_to_l(value)
                outputs = {"L": l_val}
                result_msg = f"{value} mL → {l_val:.2f} L"
            elif unit=="tbsp":
                tsp, _ = tbsp_to_tsp(value)
                outputs = {"Tsp": tsp}
                result_msg = f"{value} Tbsp → {tsp:.2f} Tsp"
            else:
                tbsp, _ = tsp_to_tbsp(value)
                outputs = {"Tbsp": tbsp}
                result_msg = f"{value} Tsp → {tbsp:.2f} Tbsp"

    except Exception as e:
        return f"❌ Error: {e}"

    record_id = get_next_id()
    save_conversion(record_id, category, unit, "/".join(outputs.keys()), value, outputs, result_msg)
    return result_msg

# Gradio Interface
iface = gr.Interface(
    fn=convert,
    inputs=gr.Textbox(label="Enter value with unit (e.g., 20C, 5kg, 10m)"),
    outputs="text",
    title="🗿 Unit Converter Web GUI 🗿",
    description=(
        "Supports [🌡️]Temperature: C, F, K | [⚖️]Weight: kg, lb | [⌚]Time: hr, min, sec | "
        "[📏]Length: m, km, cm | [🧪]Volume: L, mL, Tbsp, Tsp conversions.\n"
        "All conversions are logged to Google Sheet."
    )
)

iface.launch(share=True)  # public link
