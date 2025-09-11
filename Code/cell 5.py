# ตัวอย่างการบันทึก (ทดสอบรัน)
save_conversion_to_sheet(
    record_id=1,
    category="weight",
    from_unit="kg",
    to_unit="lb",
    input_val=2.5,
    output_val=2.5 * 2.20462,
    message="Converted successfully"
)
