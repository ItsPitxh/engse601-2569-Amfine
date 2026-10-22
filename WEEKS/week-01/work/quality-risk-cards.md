# W01 Work — Quality Risk Cards

## Submission context

- Project/team: Amfine · Online Tour Reservation Website for A.M.T. Amfine Co., Ltd.
- Proposal/SRS source + version: `INPUTS/proposal/SE-01_Amfine_Proposal_v1_2569-10-09.md` (v1 · 9 ต.ค. 2569) · อ้างถึงส่วนที่ 1 (ปัญหา/stakeholder), 3 (BR/FR/NFR), 8 (ความเสี่ยง — ตารางที่ 12)
- Authors: Peachu
- Peer reviewer: Peachu (self-review) · โครงงานผู้ดำเนินงานคนเดียวตาม Proposal §9.2 · บันทึกตรงนี้ด้วยความโปร่งใสว่าไม่มี peer ภายในทีม
- Review date/commit: 2026-10-22 (ก่อน commit แรก)

> ทำ 5 cards ครอบคลุม critical slice ของกระบวนการชำระเงิน + risk กลุ่มกระบวนการ/เทคโนโลยี/กฎหมาย/ทรัพยากร

## Card QR-01 — การใช้หลักฐานการชำระเงินซ้ำหรือปลอม

| Field | Team record |
|---|---|
| Requirement/feature/stakeholder source | FR-05, FR-17 (Proposal §3.2) · ตารางที่ 12 แถว 1 (Proposal §8) · stakeholder ทีมงาน + เจ้าของบริษัท (ตารางที่ 1) |
| Situation/context | ลูกค้าแนบหลักฐานการชำระเงินผ่านเว็บเพื่อขอการอนุมัติการจอง · ทีมงานต้องตรวจก่อนเปลี่ยนสถานะเป็นสำเร็จ · ปัจจุบันทีมงานยังตรวจกับแอปธนาคารของเจ้าของบริษัท |
| Quality risk statement | เมื่อทีมงานเริ่มเชื่อหน้าจอระบบแทนการเปิดแอปธนาคารตรวจ สลิปใบเดียวอาจถูกใช้ยืนยันได้มากกว่าหนึ่งรายการจอง หรือถูกแก้ไข/ปลอม ทำให้บริษัทรับรู้ยอดชำระเงินผิดและขาดทุนในระดับยอดจอง |
| Quality concern | Functional suitability + Security + Integrity (ISO/IEC 25010) |
| Impact and rationale | รายได้ของบริษัทขึ้นกับการกระทบยอดจริง · Proposal §8 ประเมินโอกาสเกิดต่ำ แต่ผลกระทบสูง · กระบวนการเดิมไม่มีการตรวจซ้ำแบบมีระบบ |
| Verification question/action | FR-17 ระบุไว้ชัดว่าระบบต้องปฏิเสธหลักฐานซ้ำโดยอัตโนมัติหรือไม่ · มี field จัดเก็บ reference ของสลิปใน `payments` ที่ตรวจ uniqueness ได้หรือไม่ · มี unit test ครอบคลุม duplicate detection หรือไม่ |
| Validation question/action | เมื่อทีมงานใช้งานจริง สามารถตัดสินใจเรื่องการอนุมัติโดยไม่ต้องเปิดแอปธนาคารได้หรือไม่ · UAT scenario ที่จงใจส่งสลิปซ้ำควรให้ผลที่ทีมงานยอมรับได้ |
| Planned evidence | Unit test ของ duplicate check (TC-17 ใน Proposal §3.7) · Integration test ของ flow upload (TC-05) · UAT scenario "ส่งสลิปซ้ำ" + บันทึกการตรวจกับแอปธนาคารในระยะแรก |
| Evidence status | Planned (test cases อยู่ใน Proposal §3.7; ยังไม่มี implementation) · Not Ready สำหรับผลการรันจริง |
| Evidence path/owner/next action | Owner: Peachu · Next action: implement duplicate check endpoint ใน Sprint 1 แล้ว run TC-17 · อ้าง Proposal §8 แผนรับมือข้อแรก (คงการตรวจกับแอปธนาคารจนกว่า automated check จะพร้อม) |

## Card QR-02 — ผู้ใช้จริงของบริษัทไม่พร้อมให้ทดสอบตามกำหนด (SUS + UAT)

| Field | Team record |
|---|---|
| Requirement/feature/stakeholder source | NFR-02 (SUS ≥ 70 ใน Proposal §3.3) · วัตถุประสงค์ข้อ 3 (Proposal §1.4) · ตารางที่ 12 แถว 2 · stakeholder ทีมงาน + ลูกค้า (ตารางที่ 1) |
| Situation/context | ภาคเรียนมีช่วงทดสอบจำกัด (ม.ค.-ก.พ. 2570 ตามตารางที่ 13) · บริษัทมีงานประจำวันของตัวเอง · ลูกค้าตัวแทนอาจไม่ว่างในวันที่ทีมจอง |
| Quality risk statement | เมื่อถึงช่วง UAT ทีมงานหรือตัวแทนลูกค้าไม่ว่างตามแผน จะไม่สามารถวัด SUS จากผู้ใช้จริงอย่างน้อย 5 คนตาม NFR-02 ได้ทันในภาคเรียน และ KPI คะแนน SUS ≥ 70 (ตารางที่ 14) ไม่สามารถตัดสินได้ |
| Quality concern | Usability + Validation (ความสามารถทวนสอบคุณภาพด้านประสบการณ์ผู้ใช้) |
| Impact and rationale | KPI ตัวหลักของโครงงานผูกอยู่กับ SUS · วัดไม่ได้ = ไม่สามารถประกาศความสำเร็จของวัตถุประสงค์ข้อ 3 ได้ · กระทบคะแนนประเมิน |
| Verification question/action | แบบสอบถาม SUS ฉบับไทย ครบ 10 ข้อแล้วหรือไม่ · การ์ด UAT scenario 10 รายการ (ตารางที่ 11 แถว UAT) พร้อมหรือไม่ · กำหนดการทดสอบมี option สองช่วงหรือไม่ |
| Validation question/action | ผู้ตอบ SUS เป็นผู้ใช้จริงที่ตรงกับ stakeholder ตารางที่ 1 หรือไม่ · คะแนนที่ได้สะท้อนประสบการณ์กระบวนการจองจริงหรือไม่ |
| Planned evidence | ตารางนัดหมาย UAT 2 ช่วง · แบบ SUS 10 ข้อ · บันทึก baseline SUS ของกระบวนการเดิม (จากตารางที่ 14 KPI SUS ก่อนใช้ระบบ) · log การรัน UAT scenario |
| Evidence status | Planned · ยังไม่ประสานงานกับบริษัท (ต้องเริ่มต้น Sprint 1) |
| Evidence path/owner/next action | Owner: Peachu · Next action: ส่งอีเมล/ติดต่อบริษัทต้น Sprint 1 เพื่อจองช่วง UAT ล่วงหน้า และสำรองสองช่วง (ตามแผนรับมือ Proposal §8 แถว 2) |

## Card QR-03 — Scope creep เพราะทำโครงงานคนเดียว

| Field | Team record |
|---|---|
| Requirement/feature/stakeholder source | Proposal §9.2 (ผู้ดำเนินงานคนเดียว) · ตารางที่ 12 แถว 3 · วัตถุประสงค์ข้อ 1 (18 UC ภายในภาคการศึกษา) |
| Situation/context | FR 18 ข้อ + NFR 7 ข้อ ต้องเสร็จภายใน 5 sprints ของพ.ย.-ธ.ค. 2569 · ตารางเวลาชนกับวิชาอื่น (ตารางที่ 12 แถว 8) |
| Quality risk statement | เมื่อ scope ขยายขึ้นหรือพบ bug ลึกใน sprint สุดท้าย งานอาจล้นจนไม่สามารถส่งทุก UC + ทดสอบครบตาม Definition of Done ได้ภายในภาคเรียน |
| Quality concern | Functional completeness + Delivery predictability + Risk management |
| Impact and rationale | ส่งงาน ENGSE212 ล่าช้า ส่งผลต่อการประเมิน · ตัวชี้วัดจำนวน UC ที่ใช้ได้จริง (ตารางที่ 14) ไม่ครบ |
| Verification question/action | Product Backlog จัดลำดับ MVP vs. Nice-to-have ตามความสำคัญ (ตารางที่ 4 คอลัมน์ "ความสำคัญ") แล้วหรือไม่ · มี Sprint Review ท้าย sprint ตาม Proposal §6 ที่ตัดสินใจเลื่อน feature ได้หรือไม่ |
| Validation question/action | ถ้าเลื่อน feature ระดับ Medium (เช่น FR-07, FR-12, FR-13, FR-18) ไป Phase 2 ผู้ใช้ยังรับได้หรือไม่ · วัตถุประสงค์ข้อ 2 (ลดขั้นตอน 40%) ยังทำได้ด้วย MVP หรือไม่ |
| Planned evidence | Product Backlog ที่จัดลำดับแล้ว · Sprint Retrospective note · บันทึก feature ที่ถูกย้ายไป Phase 2 พร้อมเหตุผล |
| Evidence status | Planned · จะมีหลัง Sprint 1 Review |
| Evidence path/owner/next action | Owner: Peachu · Next action: สร้าง GitHub Project backlog ที่กำกับ FR-ID ก่อนเริ่ม Sprint 1 · ยึดแผนรับมือ Proposal §8 แถว 3 |

## Card QR-04 — การออกแบบไม่สอดคล้องกับ PDPA

| Field | Team record |
|---|---|
| Requirement/feature/stakeholder source | FR-15 (Proposal §3.2) · NFR-03 (Security §3.3) · ส่วนที่ 4.1 (In-scope — PDPA Consent/Encryption/Retention/RBAC) · ตารางที่ 12 แถว 4 · พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 [1] |
| Situation/context | ระบบเก็บข้อมูลผู้เดินทางที่เป็นข้อมูลส่วนบุคคล (ชื่อ-สกุล, วันเกิด, เลขที่หนังสือเดินทาง, สัญชาติ) · เป็นข้อมูลที่ PDPA ควบคุม |
| Quality risk statement | เมื่อการออกแบบ consent flow หรือ encryption at rest ไม่ครบ ระบบจะไม่สามารถออกใช้งานจริงกับบริษัทได้ แม้ฟังก์ชันหลักเสร็จ และบริษัทอาจมีความเสี่ยงทางกฎหมาย |
| Quality concern | Security · Compliance (PDPA) · Validation |
| Impact and rationale | PDPA เป็นเงื่อนไขบังคับของขอบเขต (Proposal §4.3) · ไม่ผ่าน = ไม่สามารถส่งมอบระบบจริง |
| Verification question/action | consent dialog ก่อนบันทึกข้อมูลผู้เดินทางครอบคลุมหมวดข้อมูลที่เก็บจริงหรือไม่ · encryption at rest ถูกเปิดใช้ที่ MongoDB Atlas และฝั่งไฟล์ GridFS หรือไม่ · RBAC endpoint ทุกตัวตรวจ role หรือไม่ · retention policy เขียนไว้ที่ไหน |
| Validation question/action | ลูกค้าเข้าใจ consent ที่แสดงหรือไม่ · ทีมงานสามารถตอบคำถามเรื่องการเก็บ-ลบข้อมูลตามสิทธิ์ของลูกค้าตาม PDPA ได้หรือไม่ |
| Planned evidence | PDPA Compliance Checklist (Proposal §7 ตารางที่ 11 แถว 8) · Security review log · TC-15 (Proposal §3.7) |
| Evidence status | Planned |
| Evidence path/owner/next action | Owner: Peachu + อาจารย์ที่ปรึกษา · Next action: ปรึกษาอาจารย์เรื่อง PDPA checklist ก่อนเริ่ม Sprint ที่พัฒนา consent flow · ยึดแผนรับมือ Proposal §8 แถว 4 |

## Card QR-05 — LINE Messaging API ตอบช้าหรือ quota หมด

| Field | Team record |
|---|---|
| Requirement/feature/stakeholder source | FR-11, FR-16 (Proposal §3.2) · ตารางที่ 10 แถว Realtime Notification · ตารางที่ 11 แถว LINE Notification Test · ตารางที่ 12 แถว 7 และแถว 9 |
| Situation/context | FR-11 กำหนด response time เฉลี่ย ≤ 3 วินาที · LINE Developers Free tier มีขีดจำกัดจำนวน push message ต่อเดือน · ผู้พัฒนายังไม่คุ้นเคยกับ Webhook ของ LINE Messaging API (ตามประเมินใน §8) |
| Quality risk statement | เมื่อ LINE API มีความล่าช้า ขัดข้อง หรือ quota หมดในช่วงที่มีการจองพร้อมกันหลายรายการ ทีมงานและลูกค้าจะไม่ได้รับการแจ้งเตือนตามเวลา ทำให้ FR-11/FR-16 และ NFR-01 (Performance) ไม่ผ่าน |
| Quality concern | Performance efficiency + Reliability |
| Impact and rationale | การแจ้งเตือนเรียลไทม์คือกลไกที่แก้ปัญหาหลัก P-08/P-09 ของกระบวนการเดิม (Proposal §3.5) · พลาดการแจ้งเตือน = ประสบการณ์ย้อนกลับไปแบบเดิม |
| Verification question/action | PoC การเชื่อม LINE Sandbox เสร็จหรือยัง · มี integration test TC-11 ที่วัด response time จริงหรือไม่ · มี fallback เป็น in-app notification ตามแผนรับมือ §8 แถว 9 หรือไม่ |
| Validation question/action | ในชั่วโมงเร่งด่วนของการจอง (ตามข้อมูลบริษัท) การแจ้งเตือนยังทันหรือไม่ · ทีมงานยอมรับความไว 3 วินาทีหรือไม่ |
| Planned evidence | PoC note + screenshot จาก LINE Sandbox · TC-11 (วัดเวลา) · monitoring log ของ error rate · code ของ fallback path |
| Evidence status | Planned (ยังไม่ทำ PoC) |
| Evidence path/owner/next action | Owner: Peachu · Next action: จัด spike ต้น Sprint ที่พัฒนา FR-11 (ตามแผนรับมือ §8 แถว 7); อ้างงานของ อรรถวิทย์และคณะ (2568) [4] ที่วัด response time 2.35 วินาที เป็น baseline |

## Peer check and revision

> โครงงาน ENGSE212 เป็นโครงงานคนเดียวตาม Proposal §9.2; ไม่มี peer ภายในทีม จึงใช้ self-review โปร่งใสและขอให้อาจารย์ที่ปรึกษาตรวจเป็นลำดับถัดไป

| Check | Result / comment | Revision made / open action |
|---|---|---|
| ทุก card trace ไปยัง source จริงได้ | Pass · ทุกใบอ้างถึง FR/NFR/ตาราง/§ ของ Proposal v1 ที่ตรวจได้ | — |
| risk statement มี event/condition และ impact | Pass · ใช้รูปแบบ "เมื่อ…จะเกิด…ทำให้…" | — |
| V&V action ตอบ risk ไม่ใช่คำกว้าง | Pass · V action ชี้ไปที่ TC-ID หรือ artifact · Validation ชี้ไปที่ผู้ใช้จริง | — |
| evidence status เป็นความจริง | Pass · ทุก card เป็น Planned/Not Ready เพราะยังไม่เริ่ม Implement; ไม่มีการใส่ Pass/Fail | — |
| ครอบคลุม critical slice ของโครงงาน | Pass · QR-01 (payment slip integrity) ตรงกับ critical slice ที่เลือกไป W02 | — |

## Team conclusion

- Critical risk/feature ที่เลือกไป Week 02: **QR-01** (payment slip integrity — FR-05 + FR-11 + FR-17) เป็น critical slice เพราะเป็นปัญหาหลักของกระบวนการเดิม (P-08) และผูกกับ risk ที่มี impact สูงสุดใน Proposal §8
- สิ่งที่ยังไม่รู้และ owner:
  - จำนวน push message ต่อเดือนที่บริษัทจะใช้จริง (owner: Peachu + บริษัท; รอเริ่ม Sprint)
  - รายละเอียดกฎ early-bird (deposit vs. full-payment) จากบริษัท (owner: Peachu + บริษัท)
  - รูปแบบ consent dialog ที่อาจารย์ที่ปรึกษาแนะนำ (owner: Peachu + อาจารย์ที่ปรึกษา)
- AI Use Declaration: ดู `AI-LOG.md` (ใช้ AI ร่างและเรียบเรียง · ทุกแถวตรวจเทียบกับ Proposal v1)
