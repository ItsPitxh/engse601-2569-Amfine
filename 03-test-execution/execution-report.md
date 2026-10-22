# ผลการรันจริง (B1)

| รายการ | ข้อมูล |
|---|---|
| ทีม · feature | Amfine · Payment slip workflow (FR-05 แนบหลักฐานการชำระเงิน + FR-11 แจ้งเตือนทีมงานผ่าน LINE + FR-17 ป้องกันหลักฐานซ้ำ) |
| รุ่นของระบบที่รัน | **ยังไม่มีระบบให้รัน** · ENGSE212 repo ยังไม่สร้าง (ดู `INPUTS/input-register.md` IN-04) · Sprint 1 เริ่ม พ.ย. 2569 ตาม Proposal §9.1 ตารางที่ 13 |
| ชุดอ้างอิงที่ใช้ | Acceptance Criteria ของ FR-05/FR-11/FR-15 ใน `WEEKS/week-03/work/critical-requirement-review.md` + ชุด TC จาก Proposal §3.7 ตารางที่ 9 (TC-05, TC-11, TC-15, TC-17) · ยังไม่ได้ปรับเป็นชุด v1 ของใบงานครั้งที่ 2 (ดู `02-test-design/README.md`) |
| เครื่องมือ | **ยังไม่ได้ติดตั้ง** · แผนตาม Proposal §5.2 ตารางที่ 10: Jest 29, Supertest, Playwright, k6, LINE Sandbox |
| วันที่รัน · ผู้รัน | — (ยังไม่ได้รัน) |

> ตามข้อกำหนด `EVIDENCE-RULES.md` และ `SUBMISSIONS.md`: "ผลทดสอบต้องมาจากการรันจริง" · เมื่อยังไม่ได้รัน ให้ใช้ **Not Executed** พร้อมเหตุผล · **ห้ามใส่ผลสมมติ** · ไฟล์นี้จึงบันทึกสถานะตามความจริง

## ขั้นที่ 1 เลือกระดับ (3 คะแนน)

เหตุผลต้องบอกว่าพฤติกรรมที่ตรวจอยู่ที่ไหน เช่น ในฟังก์ชันเดียว ระหว่างบริการกับฐานข้อมูล หรือทั้งระบบผ่านหน้าจอ

| TC | ระดับ | เหตุผล (พฤติกรรมอยู่ที่ไหน) |
|---|---|---|
| TC-05 (อัปโหลดหลักฐานชำระเงิน) | Integration | พฤติกรรมอยู่ระหว่าง controller (upload endpoint) · service · GridFS · `payments` collection · ต้องรันกับ MongoDB (ของจริงหรือ in-memory) จึงเห็น field ที่บันทึกจริง |
| TC-11 (แจ้งเตือน LINE + response time) | Integration + Performance | พฤติกรรมอยู่ระหว่าง event emitter กับ LINE Messaging API ภายนอก · ต้องวัดเวลาจริงจาก event trigger → LINE receive · อาจต้อง mock LINE API ในระดับ Integration แล้วเสริมด้วย live Sandbox |
| TC-15 (consent + encryption) | Security + Integration | consent flow อยู่ที่ controller + `customers` collection · encryption at rest ตรวจที่ชั้น database · right-to-access/delete ตรวจที่ endpoint |
| TC-17 (ปฏิเสธหลักฐานซ้ำ) | Integration | uniqueness check อยู่ระหว่าง service กับ index/constraint ของ `payments` collection · ต้องรันกับฐานข้อมูลจริง |
| TC-UAT (จองทัวร์จริง 10 scenarios) | UAT (System level ที่ผู้ใช้จริงทดสอบ) | พฤติกรรมคือ user journey ครบตั้งแต่ค้นหา → จอง → ชำระ → ยืนยัน · ต้องให้ตัวแทนลูกค้าของบริษัททดลองใช้ |

## ขั้นที่ 2 กรณีทดสอบอัตโนมัติ (6 คะแนน)

| รายการ | ข้อมูล |
|---|---|
| TC และระดับ | TC-05 · Integration (ตามแผน) |
| ไฟล์โค้ดทดสอบ | **ยังไม่มี** · จะวางที่ `tests/payments.test.js` เมื่อ Sprint 1 เริ่ม |
| คำสั่งที่ใช้รัน | `npx jest tests/payments.test.js` (แผน · ยังไม่ได้รัน) |
| หลักฐาน | — (ยังไม่มี) |
| สถานะ | **Not Executed** เพราะยังไม่มี implementation ของ FR-05 ให้ทดสอบ · Sprint 1 เริ่ม พ.ย. 2569 |

ผลเทอร์มินัล (คัดลอกจากการรันจริงทั้งก้อน)

```text
(ยังไม่ได้รัน — ไม่มีผลเทอร์มินัลให้วางตามข้อกำหนด EVIDENCE-RULES.md ข้อ 4 "ห้ามเติมผลของกรณีทดสอบที่ไม่ได้รัน")
```

## ขั้นที่ 3 System ทำมือ (4 คะแนน)

| รายการ | ข้อมูล |
|---|---|
| TC | TC-17 (ปฏิเสธหลักฐานซ้ำผ่าน UI) — ตามแผน |
| ขั้นตอน | 1. ล็อกอินด้วยบัญชีลูกค้า <br> 2. สร้าง booking ใหม่ · กรอกข้อมูลผู้เดินทาง · ยอมรับ consent <br> 3. อัปโหลดสลิปใบที่ 1 (reference_id = R-001) · ระบบรับและขึ้นสถานะ pending_review <br> 4. สร้าง booking ที่สอง · อัปโหลดสลิปใบเดิม (reference_id = R-001 ซ้ำ) · ระบบต้องปฏิเสธ |
| ผลที่คาดหวัง | ระบบขึ้น error ที่ชี้ว่า reference_id R-001 ถูกใช้แล้ว · ไม่สร้าง `payments` record · ไม่กระตุ้นการแจ้งเตือน FR-11 |
| ผลจริง | — (ยังไม่ได้ทดสอบ) |
| สถานะ | **Not Executed** · จะทดสอบหลัง FR-17 implement ใน Sprint 1 |

## ขั้นที่ 4 UAT (3 คะแนน)

ผู้ทดสอบ UAT คือผู้ใช้จริงหรือตัวแทนผู้ใช้ ไม่ใช่สมาชิกทีม

| รายการ | ข้อมูล |
|---|---|
| ชื่อสถานการณ์ · ผู้ทดสอบ | "ลูกค้าใหม่จองทัวร์ครั้งแรก" · ผู้ทดสอบ: ตัวแทนลูกค้าของบริษัท เอเอ็มที แอมไฟน์ จำกัด (ยังไม่ได้นัด) |
| ขั้นตอน (ลำดับงานของผู้ใช้) | 1. เข้าหน้าแรกของเว็บ ค้นหาโปรแกรมทัวร์ที่สนใจ <br> 2. กด "จอง" กรอกข้อมูลผู้เดินทางครบตามที่ระบบขอ · ยอมรับ consent <br> 3. ชำระเงินตามช่องทางที่ระบบแสดงและแนบสลิป <br> 4. ตรวจสอบว่าได้รับการยืนยันจากทีมงานผ่าน LINE/อีเมล |
| ถือว่าผ่านเมื่อ | ลูกค้าทำครบ 4 ขั้นโดยไม่ต้องถามพนักงาน และได้รับยืนยันการจองภายในเวลาที่บริษัทกำหนด (จะได้ตัวเลขจากบริษัทต้น Sprint 1) |
| สถานะ และแผน | **Not Executed** · จะทดสอบในช่วง UAT (ม.ค.-ก.พ. 2570 ตาม Proposal §9.1 ตารางที่ 13) · นัดสองช่วงตามแผนรับมือ QR-02 |

## ขั้นที่ 5 ตารางผลของทุกกรณีทดสอบ (3 คะแนน)

| TC | ระดับ | ผลที่คาดหวัง | ผลจริง | สถานะ | หลักฐาน |
|---|---|---|---|---|---|
| TC-05 | Integration | สร้าง `payments` record มี field ครบตาม FR-05-AC-01 | — | Not Executed · ยังไม่มี implementation | — |
| TC-11 | Integration + Performance | ทีมงานได้รับ LINE message ภายใน 3,000 ms (P95 30 รอบ) | — | Not Executed · ยังไม่มี implementation + ยังไม่ทำ PoC LINE Sandbox | — |
| TC-15 | Security | consent บันทึก + passport_no เข้ารหัส + RBAC endpoint | — | Not Executed · ยังไม่มี implementation + รอ wording consent จากอาจารย์ที่ปรึกษา (GA-03) | — |
| TC-17 | Integration | ปฏิเสธ slip ที่ reference ซ้ำกับ record ที่อนุมัติแล้ว | — | Not Executed · ยังไม่มี implementation | — |
| TC-UAT | UAT | 10 scenario ครบตามใบงานครั้งที่ 2 (ยังไม่ได้ออกแบบ) | — | Not Executed · ยังไม่ได้นัดบริษัท + ยังไม่มีระบบให้ทดสอบ | — |

สรุป: Pass 0 · Fail 0 · Blocked 0 · **Not Executed 5**

## เหตุผลสรุป

ระบบ Amfine อยู่ในขั้น Requirements/SRS (SE-01 Proposal เสนอหัวข้อแล้ว 9 ต.ค. 2569) · ตามตารางเวลา Proposal §9.1 ตารางที่ 13 Sprint 1 เริ่ม พ.ย. 2569 · ภายในเวลาส่ง ENGSE601 (23 ต.ค. 2569 23:59) ยังไม่มี implementation ให้รันการทดสอบจริงใด ๆ · ตามกติกาใน `EVIDENCE-RULES.md` ข้อ 4 "ห้ามเติมผลของกรณีทดสอบที่ไม่ได้รัน" ทีมจึงบันทึก **Not Executed พร้อมแผนและเหตุผล** · ตามหัวข้อ `03-test-execution/README.md` "รันไม่ได้ ให้บันทึก Not Executed พร้อมเหตุผล และวางโค้ดที่เขียนแล้วใน tests/ ได้คะแนนตามเกณฑ์"
