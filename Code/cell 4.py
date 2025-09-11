import datetime

def save_conversion_to_sheet(record_id, category, from_unit, to_unit, input_val, output_val, message=""):
    ts = datetime.datetime.utcnow().isoformat()
    row = [
        record_id,
        ts,
        category,
        from_unit,
        to_unit,
        input_val,
        output_val,
        message
    ]
    ws.append_row(row)
    print("✅ Saved to Google Sheet.")
