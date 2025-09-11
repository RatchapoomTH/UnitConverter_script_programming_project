import gspread
import google.auth

# ใช้ credentials จาก Colab (interactive auth)
creds, _ = google.auth.default()
gc = gspread.authorize(creds)

SPREADSHEET_NAME = "UnitConverterHistory"

# ถ้าไม่มี sheet จะสร้างใหม่
try:
    sh = gc.open(SPREADSHEET_NAME)
except gspread.SpreadsheetNotFound:
    sh = gc.create(SPREADSHEET_NAME)
    print(f"Created new spreadsheet: {SPREADSHEET_NAME}")
    # แชร์ให้ email ของตัวเอง (optional)
    # sh.share("your-email@gmail.com", perm_type="user", role="writer")

ws = sh.sheet1

# ถ้า worksheet ยังว่าง → เพิ่ม header
if not ws.get_all_values():
    header = ["id","timestamp","category","from_unit","to_unit","input","output","message"]
    ws.append_row(header)
    print("✅ Header created.")
