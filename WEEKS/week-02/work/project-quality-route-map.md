# W02 Work — Project Quality Route Map

## Context

- Project/team: Amfine · Online Tour Reservation Website for A.M.T. Amfine Co., Ltd.
- Current SDLC status: **Requirements/SRS** (Proposal SE-01 v1 เสนอหัวข้อแล้ว 9 ต.ค. 2569 · ยังไม่เข้า HLD)
- Milestone/sprint/date: ก่อน Sprint 1 (Sprint 1 เริ่ม พ.ย. 2569 ตาม Proposal §9.1 ตารางที่ 13)
- Critical requirement/feature/risk: **Payment slip workflow** (FR-05 แนบหลักฐานการชำระเงิน + FR-11 แจ้งเตือนทีมงานผ่าน LINE + FR-17 ป้องกันหลักฐานซ้ำ + FR-16 แจ้งลูกค้า) · ครอบคลุม UC-06, UC-11, UC-12, UC-13, UC-14, UC-15 · เชื่อมกับ QR-01 ของ W01
- Source/version: `INPUTS/proposal/SE-01_Amfine_Proposal_v1_2569-10-09.md` §3.2 (ตารางที่ 4), §3.4 (ตารางที่ 6), §3.6 (ตารางที่ 8), §8 (ตารางที่ 12 แถว 1)
- Authors/reviewer: Peachu · self-review (โครงงานคนเดียวตาม Proposal §9.2)

## Route Map — one critical slice (Payment slip workflow)

| Phase / Gate | V&V question | Evidence + status | Decision / feedback | Owner / when |
|---|---|---|---|---|
| Requirements/SRS — Gate A | FR-05, FR-11, FR-16, FR-17 มี acceptance criteria ที่ตัดสินผ่าน-ไม่ผ่านได้หรือไม่ · "เรียลไทม์" ของ FR-11 ถูกให้ค่าแน่ชัดหรือยัง · "สลิปซ้ำ" ตัดสินด้วยเขตข้อมูลใด | Proposal §3.2 (FR definitions) · ตารางที่ 8 (RTM: BR-02→FR-11; BR-05→FR-05, FR-11) · W03 Revised Critical Requirements (planned, Peachu) | Pass บางส่วน · FR-11 มี 3 วินาที (อ้างงาน [4]) แล้ว · FR-17 ยังต้องระบุว่าใช้ hash/reference-id เป็น key — เป็น Finding RV-01 ใน W04 Review Log | Peachu · เสร็จก่อน Sprint 1 |
| HLD/Detail Design — Gate B | collection `payments` มี schema รองรับ uniqueness check หรือยัง · มี sequence diagram สำหรับ flow upload-notify-approve หรือยัง · webhook endpoint ของ LINE อยู่ที่ใด | `INPUTS/design/` **Not Ready** · Proposal §5 ให้เพียง Architecture Overview (รูปที่ 6, 7) ไม่ได้ให้ detail design | Not Ready · ต้องสร้าง HLD/Detail Design ใน ENGSE212 Sprint 0; ยังไปต่อไม่ได้ที่ Gate B | Peachu · ต้น Sprint 1 (ก่อนลงมือ code) |
| Implement/Build — Gate C (เตรียมล่วงหน้า) | duplicate check เป็น middleware ก่อนบันทึก `payments` หรือหลัง · การเรียก LINE Messaging API อยู่ใน service layer แยกจาก controller หรือไม่ · log ของ webhook เก็บที่ไหน | `IN-04` ENGSE212 repo **Not Ready** (ยังไม่สร้าง repo โครงงาน) | Not Ready · ตั้งเป้า implement ใน Sprint 1 (พ.ย. 2569) โดยทำ PoC LINE Sandbox ก่อนตามแผนรับมือ Proposal §8 แถว 7 | Peachu · Sprint 1 |
| Test/Defect — Gate C | TC-05 (upload), TC-11 (LINE notify + response time), TC-16 (status change), TC-17 (duplicate slip) ครอบคลุมเงื่อนไข normal + negative หรือไม่ · มีเกณฑ์ Pass ชัด | Proposal §3.7 ตารางที่ 9 (TC-05, TC-11, TC-16, TC-17) · ยังไม่ได้รัน (`Not Executed`) | Not Executed · ชุด TC มีการออกแบบใน Proposal แล้ว แต่ยังรอ implementation ก่อนรันจริง | Peachu · Sprint 1 ปลาย (หลัง endpoint เสร็จ) |
| Release/Portfolio — Gate D | ผลการรันของ TC-05/11/16/17 ตอบ risk QR-01 ได้แค่ไหน · มี residual risk พอให้ตัดสินส่งมอบ feature นี้หรือไม่ | Evidence pack **Not Ready** (ยังไม่มี actual result) · จะใช้ตารางที่ 14 KPI "เวลารับคำสั่งจอง" และ "SUS" ประกอบคำตัดสิน | Not Accept ตอนนี้ · เป็น "Target Gate" ปลายภาคเรียน (ก.พ. 2570 ตามตารางที่ 13) | Peachu + อาจารย์ที่ปรึกษา · ก.พ. 2570 |

## Feedback loop

| Trigger/finding | ย้อนกลับไปแก้ artifact ใด | Evidence ที่ต้องอัปเดต | Owner/when |
|---|---|---|---|
| ถ้า PoC LINE Sandbox ทำ response time ไม่ถึง 3 วินาที (NFR-01 ล้มเหลวเร็ว) | Proposal §3.3 NFR-01 และ §5.2 Technology stack · อาจต้องเปลี่ยนรูปแบบ (เช่น webhook polling) | NFR-01 เกณฑ์ · TC-11 เกณฑ์ Pass · Risk register (เปลี่ยนโอกาส/ผลกระทบของ QR-05) | Peachu · ก่อนปิด Sprint ที่พัฒนา FR-11 |
| ถ้าทีมงานไม่พร้อม UAT ตามแผน (ตรงกับ QR-02) | Proposal §9.1 ตารางที่ 13 (เลื่อนช่วงทดสอบ) · ตารางที่ 11 (ปรับ scenario) | ตารางเวลาทดสอบ · SUS baseline data | Peachu · ทันทีที่ทราบ |
| ถ้าทีมงานยอม "เชื่อหน้าจอ" ก่อน automated duplicate check พร้อม (QR-01) | FR-17 priority (ยกเป็น Blocking) · Sprint planning (ย้ายไว้ก่อน) | ลำดับ Product Backlog · test coverage ของ TC-17 | Peachu · ทันทีที่พบ |

## Evidence gap and next action

| Gap / Not Ready item | Why | Next action | Owner | Target milestone |
|---|---|---|---|---|
| HLD/Detail Design ของ critical slice | ยังไม่เริ่ม design phase | ร่าง sequence diagram ของ upload-notify-approve ใน Sprint 0 (ต.ค.-พ.ย. 2569 ตาม Proposal §9.1) | Peachu | ต้น Sprint 1 |
| ENGSE212 repository (MERN app) | ยังไม่สร้าง | สร้าง repo + CI พื้นฐานใน GitHub ก่อน Sprint 1 เริ่ม | Peachu | ปลาย ต.ค. 2569 |
| Baseline ของ "เวลารับคำสั่งจอง" (KPI ตารางที่ 14) | ยังไม่ได้จับเวลากระบวนการเดิม | นัดบริษัทจับเวลา 5 รายการตามตัวชี้วัดในตารางที่ 14 | Peachu + บริษัท | ก่อน Sprint 1 |
| PoC LINE Sandbox | ยังไม่ทดลอง | ทำ spike ตามแผนรับมือ Proposal §8 แถว 7 | Peachu | Sprint ที่พัฒนา FR-11 |

## Peer review and handoff

- Reviewer + date/commit: Peachu (self-review) · 2026-10-22 · โครงงานคนเดียวตาม Proposal §9.2
- Revision made: ปรับคำถาม V&V ที่กว้างเกินให้ชี้ไปที่ TC-ID และ Finding ID; เพิ่ม feedback loop ที่เชื่อมกับ QR-01, QR-02, QR-05
- Requirement IDs ที่จะเข้า Week 03: **FR-05** (แนบหลักฐาน), **FR-11** (LINE แจ้งทีมงาน), **FR-15** (PDPA consent) · เลือก 3 ข้อก่อนตามแนะนำของ W03 README; FR-15 เข้ามาเพราะผูก QR-04 และเป็น gate ของ release ที่หลีกเลี่ยงไม่ได้
- AI Use Declaration: ดู `AI-LOG.md` (AI ช่วยร่างและเรียบเรียง · ทุกแถวตรวจเทียบกับ Proposal)
