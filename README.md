# Unit Converter 
Unit Converter เป็นโปรแกรมรันบน Google Colab เพื่อใช้ในการเปลี่ยนหน่วยต่างๆที่ต้องการ โดยจะประกอบไปด้วย หน่วยของอุณหภูมิ หน่วยของน้ำหนัก หน่วยของเวลา หน่วยของความยาว และหน่วยของปริมาตร
Mini Project นี้เป็นงาน Mini Project ของรายวิชา CP352301 Script Programming ภาคเรียนที่ 1 ปีการศึกษา 2568

# ความคืบหน้าของแต่ละสัปดาห์
# Sprint 1 (week1)
**เป้าหมาย**
* วางแผนการแบ่งหน้าการทำงานของแต่ละคน
* ออกแบบและสร้างโปรแกรมเปลี่ยนหน่วย (Unit Converter) เบื้องต้น โดยประกอบไปด้วยฟังก์ชันในการแปลงหน่วย 5 อย่าง ได้แก่
1.   Fahrenheit → Celsius คือ °C=(°F−32)×5​/9
2.   Celsius → Fahrenheit คือ °F=(°C×9/5​)+32
3.   Celsius → Kelvin คือ K=°C+273.15
4.   Kilogram → Pound คือ lb=kg×2.20462
5.   Pound → Kilogram คือ kg=lb×0.453592

* ทดสอบการรันโปรแกรมว่าสามารถรันได้หรือไม่
* ตรวจสอบผลลัพธ์ที่ได้หากเกิดขอผิดพลาดให้ไปปรับปรุงแก้ไข

**Deliverables สิ้นสัปดาห์ที่ 1**
* ขอบเขตของโปรเจกต์ + Requirement (โดยโบ๊ท) ✅
* Test Cases เบื้องต้น (โดยต้า) ✅
* โครงสร้างโปรเจกต์ + ฟังก์ชันทดลองเล็ก ๆ (โดยข้าวปั้น) ✅
* Task Board แบ่งงานชัดเจน (ทั้งทีมเห็นร่วมกัน) ✅

# Sprint 2 (week2)
**เป้าหมาย**
* เพิ่มการแปลงความยาว (m ↔ km, cm ↔ m)
* เพิ่มการแปลงเวลา (hr ↔ min, min ↔ sec)
* จัดหมวดหมู่ให้โปรเจกต์ใหม่โดยสร้างเป็น module แยกแล้วมารันภายใน main โดย module แยกประกอบไปด้วย

🌡️ *temperature.py*
1.   Fahrenheit → Celsius คือ °C=(°F−32)×5​/9
2.   Celsius → Fahrenheit คือ °F=(°C×9/5​)+32
3.   Celsius → Kelvin คือ K=°C+273.15
4.   Kelvin → Celsius คือ °C=K−273.15

 ⚖️ *weight.py*
 
5.   Kilogram → Pound คือ lb=kg×2.20462
6.   Pound → Kilogram คือ kg=lb×0.453592
   
  ⌚ *time.py*

7.   Hours → Minutes คือ min=hr×60
8.   Minutes → Hours คือ hr=min/60
9.   Minutes → Seconds คือ sec=min×60
10.   Seconds → Minutes คือ min=sec/60

 📏 *length.py*
    
11.   Meters → Kilometers คือ km=m/1000
12.   Kilometers → Meters คือ m = km*1000
13.   Centimeters → Meters คือ m = cm/100
14.   Meters → Centimeters คือ cm = m*100

**Deliverables สิ้นสัปดาห์ที่ 2**
* โค้ดที่รองรับหลายหน่วยมากกว่า Sprint 1 ✅
* Test Cases ครอบคลุมมากขึ้น (เช่น ค่า 0, ค่าลบ, ค่าใหญ่ ๆ) ✅
* update github ✅

# Sprint 3 (week3)
**เป้าหมาย**
* แก้ไข error handling ให้มีความสมเหตุสมผลมากยิ่งขึ้น เช่น ค่าของน้ำหนักไม่สามารถติดลบได้
* แก้ไข error handling ในการป้องกันการรับค่า input ที่ผิด เช่น abc, !@#
* เพิ่มการบันทึกประวัติการแปลงหน่วยใน Google sheet
* เพิ่มการแปลงปริมาตร (L ↔ mL, L ↔ Tbsp, L ↔ Tsp, mL ↔ Tbsp, mL ↔ Tsp, Tbsp ↔ Tsp)

🌡️ *temperature.py*
1.   Fahrenheit → Celsius คือ °C=(°F−32)×5​/9
2.   Celsius → Fahrenheit คือ °F=(°C×9/5​)+32
3.   Celsius → Kelvin คือ K=°C+273.15
4.   Kelvin → Celsius คือ °C=K−273.15

 ⚖️ *weight.py*
 
5.   Kilogram → Pound คือ lb=kg×2.20462
6.   Pound → Kilogram คือ kg=lb×0.453592
   
  ⌚ *time.py*

7.   Hours → Minutes คือ min=hr×60
8.   Minutes → Hours คือ hr=min/60
9.   Minutes → Seconds คือ sec=min×60
10.   Seconds → Minutes คือ min=sec/60

 📏 *length.py*
    
11.   Meters → Kilometers คือ km=m/1000
12.   Kilometers → Meters คือ m = km*1000
13.   Centimeters → Meters คือ m = cm/100
14.   Meters → Centimeters คือ cm = m*100

 🧪 *volume.py*

15.   Liters → Milliliters คือ mL=L×1000
16.   Milliliters → Liters คือ L=mL/1000
17.   Liters → Tablespoons คือ Tbsp=L×67.628
18.   Tablespoons → Liters คือ L=Tbsp/67.628
19.   Liters → Teaspoons คือ Tsp=L×202.884
20.   Teaspoons → Liters คือ L=Tsp/202.884
21.   Milliliters → Tablespoons คือ Tbsp=mL/14.787
22.   Tablespoons → Milliliters คือ mL=Tbsp×14.787
23.   Milliliters → Teaspoons คือ Tsp=mL/4.929
24.   Teaspoons → Milliliters คือ mL=Tsp×4.929
25.   Tablespoons → Teaspoons คือ Tsp=Tbsp×3
26.   Teaspoons → Tablespoons คือ Tbsp=Tsp/3

# วิธีการใช้งาน
**หมายเหตุ: ใช้ colab ในการรันโค้ด**
