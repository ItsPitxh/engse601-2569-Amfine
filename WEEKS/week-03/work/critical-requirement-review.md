# W03 Work — Critical Requirement Review

## Review scope

- Project/team: Amfine · Online Tour Reservation Website for A.M.T. Amfine Co., Ltd.
- SRS/Requirement artifact + version/commit: Proposal SE-01 v1 (9 ต.ค. 2569) · `INPUTS/proposal/SE-01_Amfine_Proposal_v1_2569-10-09.md` §3.2 (ตารางที่ 4), §3.3 (ตารางที่ 5), §3.4 (ตารางที่ 6), §3.6 (ตารางที่ 8)
- Critical slice / linked W01 risk / W02 route: Payment slip workflow (FR-05, FR-11, FR-17) + PDPA (FR-15); เชื่อมกับ QR-01, QR-04, QR-05 และ critical slice ของ W02
- Authors: Peachu
- Decision owner(s): Peachu + อาจารย์ที่ปรึกษา (นริศ กำแพงแก้ว) · ยังไม่มี stakeholder sign-off จากบริษัท (ยังไม่เริ่ม Sprint)

> ทบทวน 3 ข้อ (FR-05, FR-11, FR-15) ตามแนะนำ W03 README (เริ่ม 3 ก่อน)

## Requirement Record — REQ-01 (FR-05 แนบหลักฐานการชำระเงิน)

### A. Source and risk

| Field | Record |
|---|---|
| Original Requirement ID | FR-05 |
| Original text | ระบบต้องให้ลูกค้าอัปโหลดหลักฐานการชำระเงิน (`slip_image_url`) เข้าสู่คอลเล็กชัน `payments` โดยตรง แทนการส่งผ่านช่องทางสนทนาส่วนตัว · ที่มา: UC-06 · ความสำคัญ: สูง |
| Source/version/location | Proposal v1 §3.2 ตารางที่ 4 แถว FR-05 · เชื่อมใน §3.4 ตารางที่ 6 UC-06 · §3.6 ตารางที่ 8 (BR-05→FR-05) · §3.7 ตารางที่ 9 TC-05 |
| Linked risk/stakeholder | QR-01 (slip reuse/forgery) · stakeholder ลูกค้า + ทีมงาน (Proposal ตารางที่ 1) |

### B. Lightweight review

| Check / issue type | Pass / Finding | Evidence, question or counterexample |
|---|---|---|
| Clear / unambiguous | **Finding (minor)** | คำว่า "อัปโหลด" ครอบคลุมประเภทไฟล์ใดบ้าง (JPG/PNG/PDF) · ขนาดสูงสุดเท่าไร · Proposal ไม่ได้กำหนด |
| Complete | **Finding** | ไม่มีการระบุว่าเมื่อผู้ใช้อัปโหลด ระบบตั้งสถานะอะไรเริ่มต้น (เช่น `pending_review`) · field ที่ต้องเก็บเพิ่ม (เช่น `uploaded_at`, `amount`, `reference_id`) ยังไม่ได้ระบุใน FR-05 ตรง ๆ (ปรากฏบางส่วนใน FR-17) |
| Consistent | Pass | สอดคล้องกับ UC-06 และ `payments` collection ใน §5.1.1 |
| Feasible | Pass | GridFS รองรับการเก็บไฟล์ (Proposal §5.2 ตารางที่ 10) |
| Testable / observable | **Finding** | TC-05 ระบุเพียง "อัปโหลดเข้า payments" ยังไม่ชี้ expected status หรือการ emit event แจ้งเตือน FR-11 |

### C. Revision and open decision

- Revised wording: **ระบบต้องให้ลูกค้าอัปโหลดหลักฐานการชำระเงิน (ไฟล์ภาพ JPG/PNG หรือ PDF ขนาดไม่เกิน 5 MB) เข้าสู่คอลเล็กชัน `payments` พร้อมเขตข้อมูล `slip_image_url`, `amount`, `paid_at`, `reference_id` และ `status = pending_review` และต้องกระตุ้นการแจ้งเตือนตาม FR-11 ภายใน 3 วินาที · ขอบเขตการแทนที่: ลูกค้าไม่ต้องส่งหลักฐานผ่านช่องทางสนทนาส่วนตัวสำหรับการจองที่สร้างในระบบ**
- Assumption ที่ยังไม่ใช่ decision: ขนาด 5 MB อิงจาก HOW-TO-GITHUB upload limit โดยทั่วไป · บริษัทยังไม่ยืนยันเพดาน
- Open question: ขนาดไฟล์สูงสุดที่บริษัทรับได้คือเท่าใด · อนุญาต PDF หรือเฉพาะภาพ · เขตข้อมูล `reference_id` ให้ลูกค้ากรอกเองหรือ OCR จากสลิป
- Decision owner + due/decision point: Peachu + บริษัท · ก่อนเริ่ม design `payments` schema ใน Sprint 1
- Status: **Conditional** (ไปต่อได้ด้วย assumption โดยบันทึก open question)

### D. Acceptance Criteria

| AC ID | Context/Input/State | Event/Rule | Observable expected result | Type/risk covered |
|---|---|---|---|---|
| FR-05-AC-01 | ลูกค้าล็อกอินแล้วและมี booking id ที่สถานะ awaiting payment | อัปโหลดไฟล์ JPG ขนาด 2 MB พร้อมจำนวนเงินและ reference id | ระบบบันทึก `payments` ด้วย `slip_image_url`, `amount`, `paid_at`, `reference_id`, `status=pending_review` และสามารถเรียกดูภาพได้จาก backend | Normal |
| FR-05-AC-02 | เหมือน AC-01 | อัปโหลดไฟล์ขนาด > 5 MB | ระบบปฏิเสธและแสดงข้อความความผิดพลาด ไม่สร้าง record ใน `payments` | Negative/Boundary (file size) |
| FR-05-AC-03 | เหมือน AC-01 | อัปโหลดไฟล์นามสกุล .exe | ระบบปฏิเสธ (ยอมเฉพาะ JPG/PNG/PDF) ไม่สร้าง record | Negative (file type) |
| FR-05-AC-04 | อัปโหลดสำเร็จครั้งแรก | ระบบต้องกระตุ้น FR-11 (แจ้งเตือนทีมงานผ่าน LINE) ภายใน 3 วินาที | ตรวจเวลา publish ของเหตุการณ์ ≤ 3,000 ms (วัดใน TC-11) | Normal (integration) |

### E. Planned evidence

- Planned test level: Unit (validation ของ size/type) + Integration (เขียน `payments` + emit event FR-11) + E2E (ลูกค้าอัปโหลดจบจนเห็นสถานะในแดชบอร์ดทีมงาน)
- Planned evidence: TC-05 + TC-11 (Proposal §3.7 ตารางที่ 9) + หลักฐาน log การ emit event ใน `03-test-execution/evidence/`
- Current status: `Planned` · ยังไม่ได้รันเพราะยังไม่มี implementation
- Owner/next action: Peachu · implement FR-05 ใน Sprint 1 ก่อนจึงรัน TC-05/TC-11

---

## Requirement Record — REQ-02 (FR-11 แจ้งเตือนทีมงานผ่าน LINE)

### A. Source and risk

| Field | Record |
|---|---|
| Original Requirement ID | FR-11 |
| Original text | ระบบต้องส่งการแจ้งเตือนไปยังบัญชี LINE ของทีมงานแบบเรียลไทม์ ผ่าน LINE Messaging API + Webhook ทันทีที่มีการจองใหม่หรือมีการอัปโหลดหลักฐานการชำระเงิน โดยเวลาตอบสนองเฉลี่ยไม่เกิน 3 วินาที (อ้างอิง อรรถวิทย์ ชังคมานนท์และคณะ 2568) · ที่มา: UC-15 · ความสำคัญ: สูง |
| Source/version/location | Proposal v1 §3.2 ตารางที่ 4 แถว FR-11 · §3.4 ตารางที่ 6 UC-15 · §3.6 ตารางที่ 8 (BR-02→FR-11, BR-05→FR-11, BR-06→FR-11) · §3.7 ตารางที่ 9 TC-11 · §5.2 ตารางที่ 10 แถว Realtime Notification · §7 ตารางที่ 11 แถว LINE Notification Test |
| Linked risk/stakeholder | QR-05 (LINE API ตอบช้า/quota) · stakeholder ทีมงาน (ตารางที่ 1) |

### B. Lightweight review

| Check / issue type | Pass / Finding | Evidence, question or counterexample |
|---|---|---|
| Clear / unambiguous | Pass | เงื่อนไข trigger (จองใหม่/อัปโหลดสลิป) และเกณฑ์เวลา 3 วินาที ชัดเจน |
| Complete | **Finding** | ไม่ได้ระบุพฤติกรรมเมื่อ LINE API fail (retry กี่ครั้ง · fallback เป็น in-app notification ตามแผน §8 แถว 9 ควรเขียนเป็น requirement) |
| Consistent | Pass | สอดคล้องกับ FR-16 (ฝั่งลูกค้า) และ FR-05 (trigger) |
| Feasible | Pass | งาน [4] ของ อรรถวิทย์ (2568) วัด response time 2.35 วินาที · เลือก 3 วินาทีเป็น safety margin |
| Testable / observable | **Finding (minor)** | TC-11 ระบุระดับ Integration แต่ไม่ได้ให้วิธีคำนวณ "เวลาตอบสนองเฉลี่ย" (จำนวนรอบ · percentile) |

### C. Revision and open decision

- Revised wording: **ระบบต้องส่งการแจ้งเตือนไปยังบัญชี LINE ของทีมงานผ่าน LINE Messaging API + Webhook ภายใน 3,000 ms (P95) นับจากเวลาที่ (ก) `bookings` ถูกสร้างใหม่ หรือ (ข) `payments` ถูกสร้างใหม่ · วัดจากการรันทดสอบอย่างน้อย 30 รอบในสภาพแวดล้อม test · หาก LINE API ล้มเหลว ระบบต้อง retry 2 ครั้งห่างกัน 1 วินาที และหากล้มเหลวต่อ ต้องบันทึก fallback event ไปที่ in-app notification พร้อม log**
- Assumption: 30 รอบ และ P95 เลือกตามแนวทาง k6/Lighthouse ใน NFR-01
- Open question: ทีมงานยอม "เฉลี่ย" หรือ "P95" · จำนวน retry และ interval ตามที่บริษัทรับได้
- Decision owner + due/decision point: Peachu + บริษัท · ก่อนเริ่ม Sprint ที่พัฒนา FR-11
- Status: **Conditional**

### D. Acceptance Criteria

| AC ID | Context/Input/State | Event/Rule | Observable expected result | Type/risk covered |
|---|---|---|---|---|
| FR-11-AC-01 | LINE Messaging API ปกติ · ทีมงาน 1 บัญชีผูกไว้ | ลูกค้าสร้าง booking ใหม่ | ทีมงานได้รับข้อความใน LINE ภายใน 3,000 ms (P95 จาก 30 รอบ) และข้อความระบุ booking id + tour name | Normal (performance) |
| FR-11-AC-02 | เหมือน AC-01 | ลูกค้าอัปโหลด payment slip | ทีมงานได้รับข้อความใหม่ภายใน 3,000 ms (P95) และข้อความระบุ booking id + amount | Normal |
| FR-11-AC-03 | LINE API ส่ง response 500 ครั้งแรก | ระบบต้อง retry 2 ครั้ง | ครั้งใดครั้งหนึ่ง success → ทีมงานได้ข้อความเดียว · ทุกครั้ง fail → fallback เป็น in-app notification + บันทึก log พร้อม error reason | Negative (reliability + fallback) |
| FR-11-AC-04 | push message quota ของ LINE Free tier หมด | ลูกค้าอัปโหลด payment slip | ระบบไม่ล่ม · บันทึก log ว่า quota หมด และใช้ fallback | Negative (quota) |

### E. Planned evidence

- Planned test level: Integration + Performance (วัด response time) + Negative (mock LINE API fail)
- Planned evidence: TC-11 + บันทึกการวัดเวลา 30 รอบ (เก็บ raw timings) + log fallback
- Current status: `Planned` · PoC ยังไม่ทำ
- Owner/next action: Peachu · PoC บน LINE Sandbox ต้น Sprint ที่พัฒนา FR-11 (ตามแผนรับมือ §8 แถว 7)

---

## Requirement Record — REQ-03 (FR-15 PDPA Consent + Encryption at Rest)

### A. Source and risk

| Field | Record |
|---|---|
| Original Requirement ID | FR-15 |
| Original text | ระบบต้องขอความยินยอม (PDPA Consent) ก่อนจัดเก็บข้อมูลส่วนบุคคล และเข้ารหัสข้อมูล ณ ที่จัดเก็บ · ที่มา: รองรับ UC-04 · ความสำคัญ: สูง |
| Source/version/location | Proposal v1 §3.2 ตารางที่ 4 แถว FR-15 · §3.6 ตารางที่ 8 (BR-01→FR-15) · §3.7 ตารางที่ 9 TC-15 · §4.1 In-scope PDPA · §4.3 ข้อจำกัด (พ.ร.บ. 2562) · §7 ตารางที่ 11 แถว PDPA Compliance Checklist |
| Linked risk/stakeholder | QR-04 (PDPA mismatch) · stakeholder ลูกค้า + เจ้าของบริษัท (ตารางที่ 1) |

### B. Lightweight review

| Check / issue type | Pass / Finding | Evidence, question or counterexample |
|---|---|---|
| Clear / unambiguous | **Finding** | "ข้อมูลส่วนบุคคล" ครอบคลุมเขตใดบ้างระบุไม่ชัด (ชื่อ, พาสปอร์ต, อีเมล, เบอร์โทร, ภาพสลิป?) |
| Complete | **Finding** | ไม่ได้พูดถึงสิทธิของเจ้าของข้อมูลตาม PDPA (right to access/delete/correct) ที่ควรมี endpoint รองรับ · ไม่ได้พูดถึง Retention Policy ที่ §4.1 เขียนไว้แต่ FR ยังไม่ถูกเขียนรายละเอียด |
| Consistent | Pass | สอดคล้องกับ NFR-03 Security |
| Feasible | Pass | MongoDB Atlas รองรับ Encryption at Rest + App layer encryption สำหรับ sensitive fields |
| Testable / observable | **Finding** | TC-15 ระบุ Security level แต่ไม่ได้ให้ list ของสิ่งที่ต้องตรวจ (consent record · encrypted field) |

### C. Revision and open decision

- Revised wording: **ระบบต้องขอ PDPA Consent ก่อนบันทึก (ก) ข้อมูลผู้เดินทาง (ชื่อ-สกุล TH/EN, วันเกิด, เลขที่หนังสือเดินทาง, วันหมดอายุหนังสือเดินทาง, สัญชาติ, อีเมล, เบอร์โทร) และ (ข) ภาพหลักฐานการชำระเงิน · บันทึก consent ใน `customers` พร้อม timestamp และเวอร์ชันของ consent text · เขตข้อมูลที่กำหนดในข้อ (ก) และ (ข) ต้องถูกเข้ารหัส ณ ที่จัดเก็บ (database encryption at rest + application-layer encryption สำหรับเลขที่หนังสือเดินทาง) · ระบบต้องมี endpoint ให้เจ้าของข้อมูลขอดู, แก้ไข, หรือลบข้อมูลของตนตามสิทธิใน พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562**
- Assumption: endpoint right-to-access/delete อยู่ใน MVP เพื่อให้ส่งมอบระบบจริงกับบริษัทได้
- Open question: ข้อความ consent (wording) ต้องให้ที่ปรึกษาด้านกฎหมายของบริษัทหรืออาจารย์ที่ปรึกษาทบทวนก่อน · Retention period เท่าใด (ปัจจุบัน §4.1 บอก "มี" แต่ไม่ให้ตัวเลข)
- Decision owner + due/decision point: Peachu + อาจารย์ที่ปรึกษา (นริศ กำแพงแก้ว) · ก่อนเริ่ม Sprint ที่พัฒนา consent flow
- Status: **Conditional** · มี open question ที่ block การ release

### D. Acceptance Criteria

| AC ID | Context/Input/State | Event/Rule | Observable expected result | Type/risk covered |
|---|---|---|---|---|
| FR-15-AC-01 | ลูกค้าเข้าหน้าจอง และยังไม่เคยให้ consent | ลูกค้ากดปุ่ม "จอง" แต่ไม่ติ๊ก consent | ระบบไม่บันทึกข้อมูลผู้เดินทาง และแสดง error ที่อ้าง PDPA | Negative |
| FR-15-AC-02 | ลูกค้าติ๊ก consent (เวอร์ชัน v1) แล้วกรอกข้อมูลผู้เดินทาง | ระบบสร้าง `customers` record | `customers` มี field `consent_version=v1`, `consent_at=timestamp`, และ `passport_no` ถูกเข้ารหัสในฐานข้อมูล (อ่านผ่าน Atlas shell โดยไม่ decrypt ไม่สามารถเห็นเลขปกติได้) | Normal (security) |
| FR-15-AC-03 | ลูกค้าล็อกอิน และต้องการขอดูข้อมูลของตัวเอง | เรียก endpoint `GET /me/pii` | ระบบคืนข้อมูลที่ decrypt แล้วเฉพาะของตัวเอง ไม่คืนของผู้อื่น | Normal (right to access) |
| FR-15-AC-04 | ลูกค้าร้องขอให้ลบข้อมูล | เรียก endpoint `DELETE /me` | ระบบทำ anonymization/removal ตาม policy · booking ที่เดินทางแล้วเก็บเฉพาะยอดสำหรับงบ ไม่เก็บ PII | Normal (right to delete) |
| FR-15-AC-05 | ผู้ไม่มี role admin เรียก `GET /customers/*` | — | ระบบปฏิเสธด้วย 403 | Negative (RBAC) |

### E. Planned evidence

- Planned test level: Security review + Integration (consent flow) + Unit (encryption helpers)
- Planned evidence: TC-15 + PDPA Compliance Checklist (Proposal §7 ตารางที่ 11) + log การเรียก endpoint right-to-access/delete
- Current status: `Planned` · ยังไม่มี design ของ consent dialog
- Owner/next action: Peachu + อาจารย์ที่ปรึกษา · ปรึกษาเรื่อง wording ของ consent และ retention period ก่อนเริ่ม Sprint ที่พัฒนา consent flow

---

## Handoff summary for Week 04

| Requirement ID | Revision status | Acceptance basis ready? | Open decision/blocker | Owner/due | Candidate test level |
|---|---|---|---|---|---|
| FR-05 | Revised (ขยายเขตข้อมูล + file validation + trigger FR-11) | Conditional · AC 4 ข้อ ครอบคลุม normal + negative (size, type, integration) | ขนาดไฟล์สูงสุดจริง · อนุญาต PDF หรือไม่ · reference_id แหล่งที่มา | Peachu + บริษัท · ต้น Sprint 1 | Unit + Integration + E2E |
| FR-11 | Revised (เพิ่ม retry/fallback · ระบุ P95 และจำนวนรอบวัด) | Conditional · AC 4 ข้อ ครอบคลุม normal + negative (API fail, quota) | เลือก P95 vs เฉลี่ย · จำนวน retry/interval · fallback policy ของทีมงาน | Peachu + บริษัท · ก่อน PoC | Integration + Performance |
| FR-15 | Revised (ขยาย scope ข้อมูล · เพิ่ม right-to-access/delete · ระบุเขตข้อมูลที่ต้องเข้ารหัส) | Conditional · AC 5 ข้อ ครอบคลุม consent + encryption + RBAC + right-to-access/delete | wording ของ consent · retention period · ที่ปรึกษาทางกฎหมาย | Peachu + อาจารย์ที่ปรึกษา · ก่อน Sprint consent | Security + Integration |
