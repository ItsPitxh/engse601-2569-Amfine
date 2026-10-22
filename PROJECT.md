# Project Profile — ENGSE212 × ENGSE601

> อัปเดตล่าสุด 22 ต.ค. 2569 · อ้างอิง Proposal SE-01 v1 (9 ต.ค. 2569)

## ข้อมูลโครงงาน

| รายการ | ข้อมูลของทีม |
|---|---|
| ชื่อโครงงานภาษาไทย | การพัฒนาระบบเว็บไซต์จองโปรแกรมทัวร์สำหรับบริษัทนำเที่ยว เอเอ็มทีแอมไฟน์ จำกัด |
| ชื่อโครงงานภาษาอังกฤษ | Online Tour Reservation Website for A.M.T. Amfine Co., Ltd. |
| ชื่อทีมสำหรับใช้ในชื่อไฟล์ (`TeamName`) | Amfine |
| ปัญหาที่โครงงานต้องการแก้ | บริษัท เอเอ็มที แอมไฟน์ จำกัด ใช้เครื่องมือหลายชนิดโดยไม่มีระบบกลางเชื่อมโยง (Google Forms + Sheets + LINE) ทำให้การทำงานถูกขัดจังหวะ สลับอุปกรณ์ไปมา เกิดขั้นตอนซ้ำซ้อน ไม่สามารถติดตามสถานะการชำระเงินได้ทันที และไม่รองรับ PDPA อย่างเป็นระบบ |
| ผู้ใช้/ผู้มีส่วนได้ส่วนเสียหลัก | ลูกค้า/นักท่องเที่ยว · ทีมงานของบริษัท · ผู้ดูแลระบบ · เจ้าของบริษัท · อาจารย์ที่ปรึกษา (รายละเอียดใน Proposal ตารางที่ 1) |
| ขอบเขตสำคัญของรุ่นที่กำลังพัฒนา | เว็บแอปพลิเคชันครอบคลุม 3 กระบวนการหลัก (ประกาศ/จอง/ติดตามหลังการจอง) · 18 Use Cases · 3 บทบาท (ลูกค้า/ทีมงาน/Admin) · MongoDB 6 collections (`staffs`, `tour_programs`, `customers`, `bookings`, `payments`, `feedbacks`) · PDPA (Consent, Encryption at Rest, Retention, RBAC) · การแนบหลักฐานชำระเงินให้ทีมงานตรวจ |
| สิ่งที่อยู่นอกขอบเขต | Payment Gateway อัตโนมัติ · Native mobile app · การจองโรงแรม/ตั๋วเครื่องบินอัตโนมัติ · GenAI วางแผนทัวร์อัตโนมัติ · ระบบบัญชี/ภาษี |
| Milestone/Sprint ปัจจุบัน | SE-01 Proposal เสนอหัวข้อแล้ว (9 ต.ค. 2569) · กำลังเตรียมเข้า Sprint 1 (พ.ย. 2569) |
| สถานะ SDLC ปัจจุบัน | Requirements/SRS (อยู่ใน Proposal ส่วนที่ 3) |
| อาจารย์ที่ปรึกษา/ผู้ให้ข้อมูล | อาจารย์ นริศ กำแพงแก้ว (อาจารย์ที่ปรึกษา) · บริษัท เอเอ็มที แอมไฟน์ จำกัด (ผู้ใช้จริง/แหล่งกระบวนการ) |

## Repository และระบบที่เกี่ยวข้อง

| รายการ | URL / Reference | หมายเหตุ |
|---|---|---|
| ENGSE212 project repository | ยังไม่สร้าง | จะสร้างก่อน Sprint 1; default branch จะใช้ `main` |
| Issue/Project board | GitHub Project ของ repo นี้ | ใช้ติดตาม backlog FR-01 ถึง FR-18 |
| Prototype/Demo | — | จะมีเมื่อจบ Sprint 1 |
| Course materials / LMS | ตามที่อาจารย์แจ้ง | ไม่ใส่ credential |
| Repository นี้ | กรอกหลังสร้าง Release | Team V&V Evidence Repo (ENGSE601) |

## Critical context เริ่มต้น

| ID | Requirement / Feature / Risk | เหตุผลที่สำคัญ | Source + version | Owner |
|---|---|---|---|---|
| C-01 | FR-05 + FR-17 — การแนบหลักฐานการชำระเงินและป้องกันสลิปซ้ำ | เป็นปัญหาแกนของกระบวนการเดิม (ทักแชตส่วนตัว + ไม่มีการตรวจซ้ำ) และเป็น risk ที่มี impact สูงใน Proposal ตารางที่ 12 | Proposal v1 §3.2 (FR-05, FR-17), §8 | Peachu |
| C-02 | FR-11 + FR-16 — การแจ้งเตือนผ่าน LINE Messaging API (เรียลไทม์) ทั้งทีมงานและลูกค้า | NFR Performance (ตอบใน 3 วินาที) อ้างงานของ อรรถวิทย์ (2568) และเป็น technology risk ที่ผู้พัฒนายังไม่คุ้นเคย | Proposal v1 §3.2 (FR-11, FR-16), §5.2, §8 | Peachu |
| C-03 | FR-15 — PDPA Consent + Encryption at Rest | ผูกกับ พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 ซึ่งเป็นข้อจำกัดบังคับของระบบ | Proposal v1 §3.2 (FR-15), §4.3 | Peachu |

## Constraints และข้อมูลที่ต้องปกป้อง

- ข้อจำกัดด้านเวลา/ทรัพยากร: ผู้ดำเนินโครงงานคนเดียว · ภาคเรียน 1/2569 (Proposal) และ 2/2569 (พัฒนา) · Hosting แบบ Free Tier (MongoDB Atlas M0, Vercel Hobby, Render)
- ระบบหรือบริการภายนอกที่พึ่งพา: LINE Messaging API + Webhook · MongoDB Atlas · Vercel · Render · GitHub Actions
- ข้อมูลส่วนบุคคล/ข้อมูลลับที่เกี่ยวข้อง: ข้อมูลผู้เดินทาง (ชื่อ-สกุล TH/EN, วัน-เดือน-ปีเกิด, เลขที่หนังสือเดินทาง, วันหมดอายุ, สัญชาติ) และหลักฐานการชำระเงิน — ห้ามคัดลอกข้อมูลจริงเข้ามาใน repo
- สิ่งที่ห้ามส่งให้เครื่องมือ AI หรือเผยแพร่สาธารณะ: ข้อมูลลูกค้าจริงของบริษัท · credential (`.env`, token, LINE channel secret)
- ข้อตกลงอื่น: repo นี้เป็น Public ตามข้อกำหนด ENGSE601 → ห้ามใส่รหัสนักศึกษาและข้อมูลส่วนบุคคล

## Current truth

- Requirement/SRS version ที่ใช้อยู่: Proposal v1 (9 ต.ค. 2569) — ยังเป็น source of truth ของทั้ง BR/FR/NFR/UC จนกว่าจะแยกเล่ม SRS ใน ENGSE212
- Design version ที่ใช้อยู่: `Not Ready` — มีเพียง Architecture Overview ใน Proposal §5 (รูปที่ 6, 7)
- Latest build/commit ที่อ้างอิง: `Not Ready` — ยังไม่เริ่ม Sprint 1
- อัปเดตล่าสุดโดย/วันที่: Peachu / 22 ต.ค. 2569
