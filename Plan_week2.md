# Plan for Week2
**หน้าที่**
1. 📝 **ต้า (Planner**)

    *   ขยาย Requirement เพิ่มประเภทหน่วยที่ต้องแปลง เช่น ความยาว: km, m, cm | น้ำหนัก: kg, lb | อุณหภูมิ: °C, °F, K
    *   จัดลำดับความสำคัญ (Priority) ว่าหน่วยใดต้องเสร็จก่อน
    *   กำหนด requirement เบื้องต้น เช่น ต้องการ Input Output ในรูปแบบไหน

2. 🐞 **ข้าวปั้น (Debugger)**

    * เขียน Test Case เพิ่มเติม สำหรับหน่วยใหม่ ๆ
    * ตรวจสอบว่าโค้ดที่โบ๊ทเขียนออกมาถูกต้องตาม requirement หรือไม่
    * ตรวจสอบหา bug ที่เกิดขึ้น

3. 💻 **โบ๊ท (Coder)**
    * พัฒนาฟังก์ชันแปลงหน่วยเพิ่มเติมตามที่ข้าวปั้นวางไว้
    *  จัดโครงสร้างโค้ดให้ง่ายต่อการเพิ่มฟังก์ชันใหม่
    *  รัน Test ของข้าวปั้น ถ้ามี bug ก็แก้ไข

**Requirement**
1. °F → °C
2. °C → °F
3. °C → K
4. K → °C
5. kg → lb
6. lb → kg
7. hr → min
8. min → hr
9. min → sec
10. sec → min
11. m → km
12. km → m
13. cm → m
14. m → cm

 **สูตรที่ใช้ในการคำนวณ**

1.   Fahrenheit → Celsius คือ °C=(°F−32)×5​/9
2.   Celsius → Fahrenheit คือ °F=(°C×9/5​)+32
3.   Celsius → Kelvin คือ K=°C+273.15
4.   Kelvin → Celsius คือ °C=K−273.15
5.   Kilogram → Pound คือ lb=kg×2.20462
6.   Pound → Kilogram คือ kg=lb×0.453592
7.   Hours → Minutes คือ min=hr×60
8.   Minutes → Hours คือ hr=min/60
9.   Minutes → Seconds คือ sec=min×60
10.   Seconds → Minutes คือ min=sec/60
11.   Meters → Kilometers คือ km=m/1000
12.   Kilometers → Meters คือ m = km*1000
13.   Centimeters → Meters คือ m = cm/100
14.   Meters → Centimeters คือ cm = m*100

**การทำงานของโปรแกรม**
 1. Run โดยใช้ colab
 2. ผู้ใช้เลือกตัวเลือกที่ต้องการ
 3. ผู้ใช้ป้อนค่าที่ต้องการจะแปลง
 4. Enter -> ได้ค่าที่แปลงเรียบร้อยแล้ว

 **Link Colab**: https://colab.research.google.com/drive/1JYg_WW6Ks9geAz1NPTV8qH_Si90EXYnt?usp=sharing
