# W04-05 — Phase 2 Entry Pack (Week 05–08)

| Phase 2 week | Candidate scope from RTM | Input/evidence ready now | Conditional / Not Ready item | Owner/next action | Entry status |
|---:|---|---|---|---|---|
| 05 Component/Unit Testing (ฉบับปรับใหม่ 21 ต.ค. 2569 คือ HLD Review + Requirement-to-Design Trace) | FR-05, FR-11, FR-17 → `payments` service + LINE notification service · FR-15 → consent service (ขึ้นกับ GA-03) | AC ของ FR-05, FR-11, FR-15 ใน `WEEKS/week-03/work/critical-requirement-review.md` · RTM ที่ `03-rtm-lite.csv` | HLD/Detail Design ของ Case X **ยังไม่มีในมือ** (ต้องใช้ `ENGSE206_CaseX_SRS_v1.0_TH` และ `ENGSE601_CaseX_HLD_v0_9_Draft_for_Review_TH` จากอาจารย์ตาม `WEEKS/week-05/README.md`) · HLD ของโครงงานตัวเองก็ยังไม่มี | Peachu · ขอ Case X documents จากอาจารย์ก่อนทำ W05 · ร่าง HLD โครงงานใน Sprint 0 | **Not Ready** · บันทึกว่าไม่มี Case X documents เป็น gap ของ W05 |
| 06 Integration Testing | FR-05 + FR-11 (upload-notify flow) · FR-15 (consent + encryption at rest) | AC + Risk cards (QR-01, QR-04, QR-05) | ยังไม่มี ENGSE212 repo (IN-04) · ยังไม่ได้ implement endpoint ใด | Peachu · สร้าง ENGSE212 repo ก่อน Sprint 1 · implement FR-05 + FR-11 ใน Sprint 1 | **Not Ready** (ภาคนี้ไม่สอน W06 — ตามประกาศรายวิชา) |
| 07 System/UAT | user journey จองทัวร์ + ชำระเงิน + รับยืนยัน (UC-01 ถึง UC-15) | Stakeholder (ตารางที่ 1 ใน Proposal) · UAT scenario 10 รายการตาม Proposal §7 ตารางที่ 11 | ยังไม่ประสานงานกับบริษัท · ยังไม่มี baseline SUS ของกระบวนการเดิม (ตามตารางที่ 14) | Peachu + บริษัท · นัดช่วง UAT 2 ช่วง (ตามแผนรับมือ QR-02) ก่อน ม.ค. 2570 | **Not Ready** (ภาคนี้ไม่สอน W07) |
| 08 Test Design Techniques | partitions ของ file size + file type (FR-05) · boundaries ของ response time (FR-11) · decision table ของ consent + role (FR-15) · state model ของ booking status + payment status | AC ของ W03 · RTM ของ W04 | ขึ้นกับการมี implementation จริงเพื่อ validate test design | Peachu · ใช้ชุด AC เป็นฐาน test design ก่อน Sprint 1 | **Not Ready** (ภาคนี้ไม่สอน W08) |

## Priority handoff

- Critical slice ที่ควร trace ต่อก่อน: **Payment slip workflow** (FR-05 + FR-11 + FR-17) · เพราะปิด risk QR-01 ซึ่งเป็นปัญหาหลักของกระบวนการเดิม (P-08) และเป็น critical slice ที่สืบมาจาก W01 → W02 → W03 → W04
- Requirement/AC ที่พร้อมที่สุด: FR-05-AC-01, FR-05-AC-04, FR-11-AC-01, FR-11-AC-02 (เป็น normal path ที่ไม่มี open parameter ปัจจุบัน)
- Open decision ที่เสี่ยง block หลายสัปดาห์:
  - GA-03 wording ของ PDPA consent — เป็น release blocker ของ FR-15 · ควรนัดอาจารย์ที่ปรึกษาปรึกษาต้นสัปดาห์หน้า
  - GA-04 ไม่มี HLD · กระทบ W05 ของทั้งโครงงาน และกระทบการประเมิน Case X ด้วย (ต้องใช้ Case X HLD)
- สิ่งที่ ENGSE212 ต้องทบทวน/อัปเดต:
  - สร้าง ENGSE212 project repository
  - ร่าง HLD/Detail Design ของ critical slice (sequence diagram upload-notify-approve)
  - จัดสรรเวลา spike/PoC สำหรับ LINE Messaging API + Webhook ต้น Sprint 1
  - เสนอ Proposal v2 เพิ่ม FR-19 Retention Policy ให้ชัดกว่าปัจจุบัน
- AI Use Declaration: ดู `AI-LOG.md` และ `WEEKS/week-03/work/peer-review-and-ai.md` · AI ใช้ร่างและเรียบเรียง · ทุกการตัดสินใจเป็นของผู้ดำเนินโครงงาน
