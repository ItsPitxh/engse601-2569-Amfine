# Week 04 — SRS Review, RTM Lite and Quality Gate A

## เป้าหมาย

เปลี่ยน W03-OUT ให้เป็นหลักฐานการทบทวนแบบมีโครงสร้าง: Review Log ที่แก้ตามได้, RTM v1 ที่ trace ได้สองทิศทาง และ Gate A decision ที่อ้างจากหลักฐาน พร้อม Phase 2 Entry Pack สำหรับ Week 05–08

Week 04 ไม่ได้ให้เขียน SRS ใหม่ทั้งเล่ม และยังไม่อ้างผลทดสอบที่ยังไม่ได้รัน

## Input

- `W03_<TeamName>_Revised-Critical-Requirements_v1.pdf` และไฟล์ work ของ Week 03
- Requirement/SRS ID + version/source of truth
- Proposal, glossary, Quality Risks, Route Map และ design notes เท่าที่มีจริง
- Decision owner/stakeholder ที่เกี่ยวข้อง

## ขั้นตอนทำงาน

1. Prepare — ระบุ scope, SRS version, critical requirements 3–5 ข้อ และ reviewer
2. Understand intent — owner อธิบาย user goal/risk โดยชี้ source
3. Inspect — ใช้มุม Correct, Complete, Consistent, Clear, Feasible, Testable, Traceable
4. Record — บันทึก pass/finding, location, evidence, impact/priority
5. Disposition — Accepted/Revised/Deferred/Rejected พร้อม owner/due
6. Re-check — reviewer ตรวจ revision และผลกระทบต่อ Requirement/AC อื่น
7. Trace — เติม RTM v1: Requirement → Acceptance Basis → Planned Test Level → Planned Evidence → Status/Owner
8. Gate A — ตัดสิน `Ready`, `Conditional` หรือ `Not Ready` จาก Review Log + RTM
9. Pack — ระบุ Phase 2 Entry Pack และ blocker สำหรับ Week 05–08
10. Export W04-OUT และบันทึก AI use เมื่อมี

ใช้ไฟล์ใน `work/` ตามลำดับ 01–05

## งานส่ง — W04-OUT

- Requirements Baseline Package v1 สำหรับ critical requirements 3–5 ข้อ
- ชื่อไฟล์: `W04_<TeamName>_SRS-Review-and-RTM_v1.pdf`
- วางที่: `WEEKS/week-04/submission/`

PDF ต้องรวม Review Scope, SRS Review Log, Requirement Status, RTM v1, Gate A Decision, Phase 2 Entry Pack และ AI Use Declaration เมื่อใช้ AI

## Definition of Done

- [ ] ทุก critical requirement มี source/version และ acceptance basis
- [ ] ทุก finding มี reviewer/disposition; จุดที่แก้มี revision note/re-check
- [ ] RTM trace ไปข้างหน้าและย้อนกลับได้ โดยไม่สร้างผลทดสอบที่ยังไม่เกิด
- [ ] open decision มี owner/due และระบุว่า block Phase 2 ส่วนใด
- [ ] Gate A สอดคล้องกับ Review Log/RTM ไม่ใช่ความรู้สึกของทีม
- [ ] Phase 2 Entry Pack ระบุสิ่งที่พร้อม สิ่งที่มีเงื่อนไข และสิ่งที่ยังไม่พร้อม
- [ ] ชื่อไฟล์ path tag และ `STATUS.md` ตรงกัน

## Handoff ไป Phase 2 — Week 05–08

- Week 05: Candidate component/module/logic + acceptance basis สำหรับ Component/Unit Testing
- Week 06: Interface/API/data flow + integration risks สำหรับ Integration Testing
- Week 07: User journey/stakeholder acceptance basis สำหรับ System/UAT
- Week 08: Rules, partitions, boundaries, decisions/states สำหรับ Test Design Techniques

Gate A `Conditional` หรือ `Not Ready` ไปต่อได้แบบมีเงื่อนไขเมื่อทีมเปิดเผย blocker, owner และ next action ห้ามเปลี่ยนเป็น Ready เพื่อให้เอกสารดูสมบูรณ์
