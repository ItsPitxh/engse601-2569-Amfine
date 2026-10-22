# หน้าส่งงานกลุ่ม ENGSE601 (หน้าเดียว)

> **กำหนดส่ง: ศุกร์ 23 ต.ค. 2569 เวลา 23:59**
> ผู้สอนตรวจจากหน้านี้ และจาก Release ชื่อ `engse601-submit` ที่สร้างก่อนกำหนดส่ง
> งานที่ไม่มีในตารางนี้ หรือไม่อยู่ใน Release ถือว่าไม่ได้ส่ง
> ดูตัวอย่างงานที่ทำครบจาก Case X ได้ที่ลิงก์ในหัวข้อ "ตัวอย่าง" ด้านล่าง

## กติกาเพราะ repo นี้เป็น Public

1. **ห้ามใส่รหัสนักศึกษา** ในไฟล์ ชื่อไฟล์ หรือหน้านี้ ใช้ชื่อและ GitHub username ใน [TEAM.md](TEAM.md) ผู้สอนจับคู่กับรหัสเอง
2. **ห้ามวางงานเดี่ยวส่วน A** ของใบงานใดในนี้ ส่วน A ส่งทาง Google Form ของแต่ละคนเท่านั้น
3. **ผลทดสอบต้องมาจากการรันจริง** ไม่ได้รันให้เขียน Not Executed พร้อมเหตุผล ดู [EVIDENCE-RULES.md](EVIDENCE-RULES.md)
4. ไม่ใส่รหัสผ่าน token หรือข้อมูลส่วนบุคคลของผู้ใช้จริง

## ข้อมูลทีม

| รายการ | กรอก |
|---|---|
| ชื่อทีม (`<TeamName>` ภาษาอังกฤษ ไม่มีช่องว่าง ใช้ชื่อเดียวกันทุกไฟล์) | Amfine |
| โครงงาน ENGSE212 | Online Tour Reservation Website for A.M.T. Amfine Co., Ltd. |
| feature ที่ใช้ทดสอบ (เลือกในใบงานครั้งที่ 1) | การแนบและตรวจสอบหลักฐานการชำระเงิน (FR-05 + FR-11 + FR-17) · critical slice ของทั้งโครงงาน |
| ผู้ส่งหลัก | พิชญ์ สินธรสวัสดิ์ (Peachu) |
| ลิงก์ repo นี้ | [กรอกหลังสร้าง Release เช่น https://github.com/<your-github>/engse601-2569-Amfine] |

## งานที่ต้องส่ง

| # | งาน | ไฟล์และตำแหน่ง | นับเข้า | สถานะ | หมายเหตุ |
|---|---|---|---|---|---|
| G1 | W01 Quality Risk Cards | `WEEKS/week-01/submission/W01_Amfine_Quality-Risk-Cards_v1.pdf` | จิตพิสัย | [ ] ส่งบางส่วน | ร่างใน `work/` แล้ว ยังต้อง export PDF |
| G2 | W02 Project Quality Route Map | `WEEKS/week-02/submission/W02_Amfine_Project-Quality-Route-Map_v1.pdf` | จิตพิสัย | [ ] ส่งบางส่วน | ร่างใน `work/` แล้ว ยังต้อง export PDF |
| G3 | W03 Revised Critical Requirements | `WEEKS/week-03/submission/W03_Amfine_Revised-Critical-Requirements_v1.pdf` | Gate A | [ ] ส่งบางส่วน | ร่างใน `work/` แล้ว ยังต้อง export PDF |
| G4 | W04 SRS Review, RTM Lite และ Gate A | `WEEKS/week-04/submission/W04_Amfine_SRS-Review-and-RTM_v1.pdf` | Gate A | [ ] ส่งบางส่วน | ร่างใน `work/` ครบ 01–05 ยังต้อง export PDF |
| G5 | W05 Requirement-to-Design Trace | `WEEKS/week-05/submission/W05_Amfine_Requirement-to-Design-Trace_v1.pdf` | Gate B | [ ] ไม่ได้ทำ | ต้องใช้ Case X SRS v1.0 และ CaseX HLD v0.9 จากอาจารย์ — ยังไม่มีในมือ (ดู `WEEKS/week-05/submission/README.md`) |
| G6 | ใบงานครั้งที่ 1 ส่วน B วางแผนก่อนทดสอบ | `01-plan/S1-B_Amfine.pdf` **เฉพาะส่วน B** | Evidence Pack | [ ] ไม่ได้ทำ | ยังไม่มีเนื้อหาใบงานในมือ (ดู `01-plan/README.md`) |
| G7 | ใบงานครั้งที่ 2 ส่วน B ออกแบบกรณีทดสอบ | `02-test-design/S2-B_Amfine.pdf` | Evidence Pack | [ ] ไม่ได้ทำ | ยังไม่มีเนื้อหาใบงานในมือ (ดู `02-test-design/README.md`) |
| G8 | ใบงานรวม 3–4 ส่วน B1 รันชุดอ้างอิงของทีม | `03-test-execution/execution-report.md` · `tests/` · `evidence/` | Evidence Pack | [ ] ไม่ได้ทำ | ระบบ MERN ยังไม่เริ่มพัฒนา (Sprint 1 เริ่ม พ.ย. 2569) ยังไม่มีอะไรให้รัน — ใช้ Not Executed พร้อมแผน |
| G9 | ใบงานรวม 3–4 ส่วน B3 หน้าที่และการใช้ AI | [TEAM.md](TEAM.md) · [AI-LOG.md](AI-LOG.md) | Evidence Pack | [x] ส่งแล้ว | TEAM.md และ AI-LOG.md กรอกครบ |

**สถานะที่ใช้:** `ส่งแล้ว` · `ส่งบางส่วน` (เขียนในหมายเหตุว่าขาดอะไร) · `ไม่ได้ทำ` (เขียนเหตุผล) · `แก้หลังส่ง` (บอกว่าแก้อะไร)

## ไม่ต้องทำ

- **ใบงานรวม 3–4 ส่วน B2** (ข้อบกพร่อง ความรุนแรง ทดสอบซ้ำ คำตัดสินส่งมอบ) เพราะไม่ได้สอนครั้งที่ 4 · ไม่นับคะแนน
- **ใบงานรวม 3–4 ส่วน A ข้อ 3–5** (งานเดี่ยว) ไม่นับคะแนน ทำเฉพาะข้อ 1–2
- **สัปดาห์ที่ 6–17** ในโฟลเดอร์ `WEEKS/` ไม่ได้ใช้ในภาคนี้

## ทีมที่ยังไม่มีข้อมูลโครงงานพอ

ทำเท่าที่มีจริง แล้วเขียนช่องว่างให้ชัด เช่น "ยังไม่มีเอกสารออกแบบ · ผู้รับผิดชอบ … · จะได้เมื่อ …" งานที่บอกช่องว่างตามจริงได้คะแนนตามเกณฑ์ **ห้ามสร้างเอกสาร ผลการรัน หรือหลักฐานย้อนหลังเพื่อให้มีของส่ง**

## วิธีส่ง

1. วางไฟล์ตามตารางด้านบน แล้ว commit และ push · ตั้งชื่อไฟล์ตามตารางทุกตัวอักษร
2. กรอกตาราง "งานที่ต้องส่ง" ในหน้านี้ให้ครบ
3. ผู้ส่งหลักสร้าง Release: หน้า repo → **Releases** → **Draft a new release** → Choose a tag พิมพ์ `engse601-submit` → **Create new tag** → ตั้งชื่อ `engse601-submit` → **Publish release**
4. ผู้ส่งหลักกรอกลิงก์ repo ในฟอร์มลงทะเบียนทีมที่ผู้สอนแจก

แก้หลังสร้าง Release ได้ก่อนกำหนดส่ง โดยสร้าง Release ใหม่ชื่อ `engse601-submit-v2` · ผู้สอนตรวจ Release ล่าสุดที่สร้างก่อนกำหนดส่ง

## ตัวอย่าง

ตัวอย่างงานที่ทำครบจาก Case X ของผู้สอน (ทีมสมมติ Team00): https://github.com/se-rmutl/ENGSE601-Team00-CaseX-Example · เปิด `SUBMISSIONS.md` ของตัวอย่างเทียบกับหน้านี้ได้ทีละแถว · ใช้ดูรูปแบบและระดับความละเอียด **ห้ามคัดลอกข้อความหรือหลักฐาน** เพราะงานของทีมต้องมาจากโครงงานของทีมเอง

## ตรวจก่อนส่ง

- [x] ชื่อไฟล์ใช้ `Amfine` เดียวกันทุกไฟล์ และตรงกับตาราง
- [x] ไม่มีรหัสนักศึกษาและไม่มีส่วน A ใน repo
- [ ] `03-test-execution/` มีโค้ดทดสอบใน `tests/` และผลการรันจริงใน `evidence/` (หรือ Not Executed พร้อมเหตุผล) — ใช้ Not Executed พร้อมเหตุผลและแผน
- [x] TEAM.md บอกว่าใครทำส่วนไหน · AI-LOG.md กรอกแล้ว
- [ ] สร้าง Release `engse601-submit` แล้ว — ยังไม่ได้ทำ (ให้ Peachu ทำผ่านหน้าเว็บ GitHub หลัง push)
