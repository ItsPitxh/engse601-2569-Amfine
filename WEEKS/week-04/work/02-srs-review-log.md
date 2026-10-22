# W04-02 — SRS Review Log

> ตรวจซ้ำ (re-check) ของ W03 revised wording + ขยายไปที่ Correct/Traceable ซึ่งไม่ได้ตรวจเต็มใน W03

| Finding ID | Req ID / version / location | Lens | Pass/Finding + evidence/counterexample | Impact / priority | Disposition | Revision / decision | Owner / due | Re-check status/evidence |
|---|---|---|---|---|---|---|---|---|
| RV-01 | FR-05 · Proposal v1 §3.2 · W03 revised | Testable | **Finding** · W03 เพิ่ม 5 MB เพดานไฟล์ แต่ TC-05 ใน Proposal §3.7 ยังเป็นเพียง "อัปโหลดเข้า payments" · ต้องเพิ่มการวัด size/type Pass criterion | Major · ส่งผลต่อการตัดสิน Pass ของ Sprint 1 | Accepted | เพิ่ม AC FR-05-AC-02/AC-03 ใน W03 แล้ว · จะอัปเดต TC-05 เป็น TC-05.a/b/c ตอนเริ่ม Sprint 1 | Peachu · ก่อนเขียน test ของ Sprint 1 | Open · รอ open question เรื่องเพดานไฟล์จริงจากบริษัท |
| RV-02 | FR-11 · Proposal v1 §3.2 · W03 revised | Testable | **Finding** · "เฉลี่ยไม่เกิน 3 วินาที" แปลงเป็น P95 แล้วใน W03 · ต้องยืนยันกับบริษัทว่ายอมรับ P95 vs mean | Major · กระทบเกณฑ์วัดใน TC-11 | Accepted (conditional) | ใช้ P95 ไปก่อน และบันทึกเป็น open decision · ถ้าบริษัทยืนยัน mean จะย้อนกลับไปแก้ FR-11 wording | Peachu + บริษัท · ก่อน Sprint FR-11 | Open |
| RV-03 | FR-15 · Proposal v1 §3.2 · W03 revised | Complete | **Finding** · ขาด retention period ที่ Proposal §4.1 ระบุว่า "มี" แต่ไม่ให้ตัวเลข · ขาด wording consent ที่ตรวจกับที่ปรึกษาด้านกฎหมาย | Critical · เป็น release blocker ของ PDPA | Deferred (รอ decision จากอาจารย์ที่ปรึกษา) | ปัจจุบันระบบจะเขียน assumption retention 2 ปี แต่ยังไม่ fix จนกว่าอาจารย์ที่ปรึกษาจะตรวจ | Peachu + อาจารย์ที่ปรึกษา · ก่อน Sprint consent | Open |
| RV-04 | FR-15 · Proposal v1 §4.1 (In-scope PDPA) | Traceable | **Finding** · §4.1 บอกว่ามี "Retention Policy" แต่ไม่มี FR-ID ที่สอดคล้อง · ขาด FR แยกสำหรับ Retention/Deletion | Major | Accepted · ขอเพิ่ม FR ใหม่ (FR-19) หรือขยาย FR-15 ให้คลุม retention schedule ชัด | Revised wording ของ FR-15 ใน W03 ครอบคลุม right-to-delete แล้ว · เสนอให้ Proposal v2 เพิ่ม FR-19 "Retention Policy" แยก | Peachu · เสนอใน Sprint Review ครั้งแรก | Open |
| RV-05 | FR-05 + FR-17 · Proposal v1 §3.2 | Consistent | **Finding** · FR-17 พูดถึง "ป้องกันไฟล์เดียวกันซ้ำ" และ "แสดงจำนวนเงิน · วันเวลา · ภาพหลักฐาน" แต่ FR-05 ไม่ได้ list field เหล่านี้ที่ลูกค้าต้องให้ · ควรทำให้ consistent | Minor | Accepted | revised FR-05 ใน W03 เพิ่ม `amount`, `paid_at`, `reference_id` แล้ว · ไม่ต้องแก้ FR-17 เพิ่มเติม | Peachu · เสร็จแล้วใน W03 | Closed · อ้าง `WEEKS/week-03/work/critical-requirement-review.md` REQ-01 |
| RV-06 | FR-11 · Proposal v1 §7 ตารางที่ 11 แถว LINE Notification Test | Traceable | Pass · เกณฑ์ 3 วินาที + 100% ความถูกต้องของข้อมูล ปรากฏทั้งใน §3.2 FR-11, §5.2 ตารางที่ 10, §7 ตารางที่ 11, §8 ตารางที่ 12 แถว 7 · trace ได้ครบ | Minor | — | — | — | Closed |
| RV-07 | FR-15 · Proposal v1 §3.7 TC-15 | Testable | **Finding** · TC-15 ระบุระดับ Security แต่ไม่ได้ให้ list "สิ่งที่ตรวจ" (consent record · encrypted field · right-to-access endpoint) | Major | Accepted | จะขยาย TC-15 เป็น TC-15.a (consent), TC-15.b (encryption at rest), TC-15.c (right-to-access), TC-15.d (right-to-delete) ก่อน Sprint consent · AC ใน W03 เป็น template | Peachu · ก่อน Sprint consent | Open |

## Requirement status after review

| Requirement ID | Status | Acceptance basis | Remaining open issue | Owner/due | Reason/evidence |
|---|---|---|---|---|---|
| FR-05 | **Conditional** | FR-05-AC-01 ถึง FR-05-AC-04 ใน `WEEKS/week-03/work/critical-requirement-review.md` | ขนาดไฟล์สูงสุดจริง · อนุญาต PDF หรือไม่ · reference_id มาจากไหน | Peachu + บริษัท · ก่อน Sprint 1 implement | RV-01, RV-05 |
| FR-11 | **Conditional** | FR-11-AC-01 ถึง FR-11-AC-04 ใน W03 | P95 vs mean · จำนวน retry/interval · fallback policy ของทีมงาน | Peachu + บริษัท · ก่อน Sprint ที่พัฒนา FR-11 | RV-02, RV-06 |
| FR-15 | **Not Ready** | FR-15-AC-01 ถึง FR-15-AC-05 ใน W03 (ยังมี wording ที่ต้องแก้ตามอาจารย์ที่ปรึกษา) | wording consent · retention period · ที่ปรึกษาทางกฎหมาย · เพิ่ม FR-19 แยกหรือไม่ | Peachu + อาจารย์ที่ปรึกษา · ก่อน Sprint consent | RV-03, RV-04, RV-07 |

> หมายเหตุ: ข้อเสนอแก้ไข (`Proposed revision`) ไม่ใช่ stakeholder decision จนกว่าผู้มีอำนาจยืนยัน · ที่นี่ FR-05/FR-11 ยัง `Conditional` เพราะต้องให้บริษัทยืนยัน · FR-15 `Not Ready` เพราะต้องให้อาจารย์ที่ปรึกษาตรวจ consent wording
