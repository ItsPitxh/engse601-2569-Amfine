# W04-04 — Quality Gate A Decision

## Evidence reviewed

- SRS/Requirement version: Proposal SE-01 v1 (9 ต.ค. 2569) · `INPUTS/proposal/SE-01_Amfine_Proposal_v1_2569-10-09.md`
- W03-OUT: `WEEKS/week-03/work/critical-requirement-review.md` + `peer-review-and-ai.md` (draft v1 ที่ยังไม่ได้ export เป็น PDF)
- Review Log: `WEEKS/week-04/work/02-srs-review-log.md` (RV-01 ถึง RV-07)
- RTM v1: `WEEKS/week-04/work/03-rtm-lite.csv` (5 แถว: FR-05, FR-11, FR-15, FR-17, FR-16)
- Reviewers/decision owner/date: Peachu (self-review) + อาจารย์ที่ปรึกษา นริศ กำแพงแก้ว (จะตรวจต่อ) · 2026-10-22

## Decision

เลือกเพียงหนึ่งสถานะ

- [ ] `Ready` — ไม่มี unresolved critical issue; critical requirements มี acceptance basis และ trace เพียงพอสำหรับ Phase 2
- [x] **`Conditional`** — ไปต่อเฉพาะส่วนที่ระบุ พร้อม conditions, owner และ due
- [ ] `Not Ready` — ยังมี blocker ที่ทำให้ test/design basis สำคัญตัดสินไม่ได้

## Evidence-based rationale

- FR-05 (RV-01, RV-05) · มี AC ที่ตัดสิน Pass/Fail ได้แล้ว (`WEEKS/week-03/work/critical-requirement-review.md` REQ-01 E) · ยังรอ open question เรื่องเพดานไฟล์จากบริษัท ซึ่งเป็นการ **ปรับพารามิเตอร์** ไม่ใช่การเปลี่ยน requirement ชั้นต้น → **ให้ไปต่อแบบมีเงื่อนไข**
- FR-11 (RV-02, RV-06) · trace ครบจาก §3.2 → §5.2 → §7 → §8 · มี AC + fallback policy แล้ว · ค่าสถิติ P95 vs mean เป็นเงื่อนไขการวัด → **ไปต่อแบบมีเงื่อนไข** โดยยึด P95 เป็น default ก่อน
- FR-15 (RV-03, RV-04, RV-07) · wording ของ PDPA consent และ retention period ยังไม่ตัดสิน และต้องให้อาจารย์ที่ปรึกษาตรวจก่อน · เรื่องนี้เป็น release blocker ไม่ใช่ test blocker → **ให้ Sprint วาง consent flow ไปเริ่มเขียน code ไม่ได้จนกว่าจะได้ decision** · แต่ Sprint อื่น (เช่น FR-05/FR-11) ไปต่อได้
- FR-17, FR-16 · มี wording พอใช้ · AC จะเติมใน Sprint 1 → **ไม่ block Gate A**

สรุป: critical slice ส่วน upload/notify (FR-05 + FR-11 + FR-17) ไปต่อได้แบบมีเงื่อนไข · ส่วน PDPA (FR-15) ยัง Not Ready

## Conditions / blockers / actions

| ID | Condition or blocker | Affected requirement / Phase 2 work | Action | Owner | Due | Re-check evidence |
|---|---|---|---|---|---|---|
| GA-01 | ขนาดไฟล์สูงสุด / รองรับ PDF หรือไม่ / แหล่งของ `reference_id` | FR-05 → W05 Design + Sprint 1 implement | สอบถามบริษัทต้น Sprint 1 (ตามแผนรับมือ QR-01) | Peachu + บริษัท | ต้น Sprint 1 (พ.ย. 2569) | บันทึก email/การประชุม + commit wording ที่ยืนยันแล้วเข้า Proposal v2 |
| GA-02 | P95 vs mean / จำนวน retry / interval / fallback policy ของทีมงาน | FR-11 → PoC + Sprint ที่พัฒนา FR-11 | ทำ PoC LINE Sandbox ตามแผนรับมือ Proposal §8 แถว 7 · ยืนยันค่าสถิติกับบริษัท | Peachu + บริษัท | ก่อน Sprint FR-11 | PoC log + email ยืนยัน |
| GA-03 | wording ของ PDPA consent / retention period / เพิ่ม FR-19 แยกหรือไม่ | FR-15 → Sprint ที่พัฒนา consent flow | ปรึกษาอาจารย์ที่ปรึกษา (นริศ กำแพงแก้ว) ก่อนลงมือ code consent | Peachu + อาจารย์ที่ปรึกษา | ก่อน Sprint consent (คาดในภาคถัดไป) | บันทึกการประชุม + commit Proposal v2 |
| GA-04 | HLD/Detail Design ยังไม่มี | Phase 2 ทั้งหมด (W05–W08) | ร่าง HLD + sequence diagram + ER refinement ใน Sprint 0 | Peachu | ปลาย ต.ค. 2569 | commit ของเอกสาร design ใน `INPUTS/design/` |

## Sign-off

- Requirement owner/representative: บริษัท เอเอ็มที แอมไฟน์ จำกัด · **Not Available** (ยังไม่ได้ขอ sign-off อย่างเป็นทางการสำหรับ revised wording ของ W03)
- Reviewer: Peachu (self-review) · 2026-10-22 · บันทึกตามแนวทาง `TEAM.md`
- Team: Peachu · 2026-10-22

> Sign-off นี้เป็นบันทึกการทบทวนในรายวิชา ไม่ใช่การอนุมัติจาก stakeholder · GA-01 ถึง GA-03 ยังเป็น open condition ที่ต้องปิดก่อนเริ่ม Sprint ที่เกี่ยวข้อง
