# W04-01 — Review Scope and Preparation

| Field | Team record |
|---|---|
| Project/team | Amfine · Online Tour Reservation Website for A.M.T. Amfine Co., Ltd. |
| SRS/Requirement source + version/commit | Proposal SE-01 v1 (9 ต.ค. 2569) · `INPUTS/proposal/SE-01_Amfine_Proposal_v1_2569-10-09.md` · ส่วน Requirement อยู่ใน §3.2 ตารางที่ 4 (FR-01 ถึง FR-18) |
| Review date/session | 2026-10-22 (self-review session) |
| Critical slice / requirement IDs (3–5) | FR-05 (แนบหลักฐานการชำระเงิน), FR-11 (แจ้งเตือนทีมงานผ่าน LINE), FR-15 (PDPA Consent + Encryption) · เป็น critical slice เดียวกับ W02 (payment slip workflow) + layer PDPA ที่หลีกเลี่ยงไม่ได้ |
| Linked W01 risks / W02 route / W03 output | QR-01 (slip reuse) · QR-04 (PDPA) · QR-05 (LINE API) · W02 route map (critical slice: payment slip workflow) · W03 revised wording ของ FR-05/FR-11/FR-15 (ดู `WEEKS/week-03/work/critical-requirement-review.md`) |
| Author/Requirement owner | Peachu |
| Reviewer(s) | Peachu (self-review) + อาจารย์ที่ปรึกษา นริศ กำแพงแก้ว (จะตรวจเป็นลำดับถัดไป ยังไม่ลงลายมือ) |
| Recorder/facilitator | Peachu |
| Out of scope | FR อื่น ๆ (FR-01 ถึง FR-04, FR-06 ถึง FR-10, FR-12, FR-13, FR-14, FR-16, FR-17, FR-18) · NFR ทุกข้อ · UC อื่นนอก UC-04, UC-06, UC-15 · เอกสาร HLD/Design (ยังไม่มี) |

## Sources available

| Artifact | Path/URL + version | Status | How used in review |
|---|---|---|---|
| Proposal | `INPUTS/proposal/SE-01_Amfine_Proposal_v1_2569-10-09.md` v1 · 9 ต.ค. 2569 | Existing | เอกสารต้นทางของทุก FR ที่ตรวจในสัปดาห์นี้ · อ้างทั้ง §3.2, §3.4, §3.6, §3.7, §4, §5, §7, §8 |
| Requirement/SRS | รวมอยู่ใน Proposal §3 (ยังไม่แยกเล่ม SRS) | Existing (ฝังใน Proposal) | — |
| W03-OUT | `WEEKS/week-03/work/critical-requirement-review.md` + `peer-review-and-ai.md` | Existing | ใช้เป็นชุด revision ที่กำลังตรวจซ้ำใน Review Log |
| Glossary/business rule | รวมอยู่ใน Proposal §1.3 (TO-BE processes) + §5.1.1 (data model) | Existing (ฝัง) | ใช้ตรวจเรื่อง early-bird rule และ `payments` schema |
| Design/interface notes | `INPUTS/design/` **Not Ready** · มีเพียง Architecture Overview ใน Proposal §5 รูปที่ 6, 7 | Not Ready | ยังตรวจ Gate B ไม่ได้ · บันทึกเป็น blocker ของ Phase 2 (ดู `05-phase-2-entry-pack.md`) |
