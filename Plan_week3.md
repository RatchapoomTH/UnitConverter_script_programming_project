# Plan for Week3
**หน้าที่**
1. 📝 **ข้าวปั้น (Planner**)

    *   กำหนดว่าจะเพิ่ม Volume Converter(L ↔ mL, L ↔ Tbsp, L ↔ Tsp, mL ↔ Tbsp, mL ↔ Tsp, Tbsp ↔ Tsp) และปรับปรุง error handling
    *   เขียน README การใช้งานโปรแกรมใน Github


2. 🐞 **โบ๊ท (Debugger)**

    * ทดลอง run โปรแกรมกับ input ที่ผิดตรวจสอบว่า error handling ทำงานถูกต้อง
    * แก้ไข error handling ให้มีความสมเหตุสมผลมากยิ่งขึ้น ค่าของน้ำหนัก เวลา ความยาว และปริมาตรไม่สามารถติดลบได้
    * แก้ไข error handling ในการป้องกันการรับค่า input ที่ผิด เช่น abc, !@#


3. 💻 **ต้า (Coder)**
    * เพิ่ม Volume Converter (L ↔ mL, L ↔ Tbsp, L ↔ Tsp, mL ↔ Tbsp, mL ↔ Tsp, Tbsp ↔ Tsp)
    *  ทำงานร่วมกับโบ๊ท: เมื่อโค้ดเสร็จ → ส่งให้โบ๊ททดสอบ → แก้ไขตาม feedback
    * บันทึกประวัติการแปลงหน่วยใน Google sheet

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
15. L → mL
16. mL → L
17. L → Tbsp
18. Tbsp → L
19. L → Tsp
20. Tsp → L
21. mL → Tbsp
22. Tbsp → mL
23. mL → Tsp
24. Tsp → mL
25. Tbsp → Tsp
26. Tsp → Tbsp

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

**การทำงานของโปรแกรม**
 1. Run โดยใช้ colab
 2. ผู้ใช้เลือกตัวเลือกที่ต้องการ
 3. ผู้ใช้ป้อนค่าที่ต้องการจะแปลง
 4. Enter -> ได้ค่าที่แปลงเรียบร้อยแล้ว

 **Link Colab**: https://colab.research.google.com/drive/1Wst1sjSuaHp7KRVqdOke9cYKc0mUhDx2?usp=sharing
