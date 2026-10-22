# W05 Gap Note — เหตุผลที่ยังไม่ได้ส่ง W05

> ตามหัวข้อ "ทีมที่ยังไม่มีเอกสารออกแบบของโครงงาน" ใน `WEEKS/week-05/README.md` และตามข้อกำหนด `SUBMISSIONS.md` ที่ว่า "ห้ามสร้างเอกสาร ผลการรัน หรือหลักฐานย้อนหลังเพื่อให้มีของส่ง"

## สภาพปัจจุบัน (22 ต.ค. 2569)

สัปดาห์ที่ 5 ใช้กรณีศึกษา **Case X — Multi-Resource Event Booking** ตามเอกสารประจำวิชา โดยต้องอ้างถึง:

- `ENGSE206_CaseX_SRS_v1.0_TH` (รุ่น 1.0)
- `ENGSE601_CaseX_HLD_v0_9_Draft_for_Review_TH` (รุ่น 0.9)

**ทั้งสองไฟล์ยังไม่มีในมือของทีม Amfine** ณ ตอนที่กรอกไฟล์นี้

## เอกสารที่ขาด

| ไฟล์ | ผู้รับผิดชอบส่งต่อ | เมื่อไรจึงจะได้ |
|---|---|---|
| `ENGSE206_CaseX_SRS_v1.0_TH` | อาจารย์ประจำวิชา ENGSE601 | รอให้อาจารย์แจกในชั้นเรียนหรือ LMS |
| `ENGSE601_CaseX_HLD_v0_9_Draft_for_Review_TH` | อาจารย์ประจำวิชา ENGSE601 | เช่นเดียวกัน |

## ผลกระทบต่อ Phase 2

- W05 Requirement-to-Design Trace: ตัดสินสถานะการรองรับของ design (`Supported/Partially Supported/Not Supported/Not Verifiable`) ไม่ได้ · DR-xx, HF-xx, DQ-xx ยังเติมไม่ได้
- RTM update ของ Case X ก็ยังทำไม่ได้ด้วยเหตุผลเดียวกัน

## สิ่งที่ทีมจะไม่ทำ

- **ไม่คัดลอก** เอกสารจากทีมอื่นหรือจาก Case X Example (Team00) · ตามข้อกำหนดใน `SUBMISSIONS.md` หัวข้อ "ตัวอย่าง"
- **ไม่สร้าง** design component, finding, risk, หรือ open question ของ Case X จาก memory ของ AI หรือเดา

## สิ่งที่ทีมจะทำ

1. ขอเอกสาร Case X จากอาจารย์ประจำวิชา
2. เมื่อได้เอกสารแล้ว กรอก CSV ใน `work/` ตามรูปแบบที่ให้มา (ตัวอย่างแถวใน `trace.csv` และ `design-register.csv` คงไว้เป็น reference)
3. Export เป็น `W05_Amfine_Requirement-to-Design-Trace_v1.pdf` วางใน `submission/` และสร้าง tag ใหม่

## การถ่ายโอนไปโครงงาน Amfine (optional, ตาม README หัวข้อ "ส่งต่อครั้งที่ 1")

ทีม Amfine ยังไม่มีเอกสารออกแบบของโครงงานตัวเอง (`INPUTS/design/` **Not Ready** ตาม `INPUTS/input-register.md` IN-03) · ส่วนที่ 5 ของ Proposal v1 ให้เพียง Architecture Overview (รูปที่ 6, 7)

แผนการสร้าง HLD โครงงาน Amfine:

| ส่วน | เมื่อไร | Owner |
|---|---|---|
| Sequence diagram ของ upload-notify-approve (critical slice ที่เลือกใน W02) | Sprint 0 (ปลาย ต.ค.-ต้น พ.ย. 2569) | Peachu |
| ER refinement จาก Proposal รูปที่ 7 → schema ของ 6 คอลเล็กชัน | Sprint 0 | Peachu |
| Context + Container diagram (C4-style) ของ MERN + LINE Messaging API | Sprint 0 | Peachu |

**ยังไม่สร้างเอกสารใด ๆ ตอนนี้** · ไฟล์นี้เป็นบันทึกช่องว่างที่ตามข้อกำหนด ENGSE601 "ได้คะแนนเต็มได้" เมื่อระบุผู้รับผิดชอบและกำหนดวันที่ชัด
