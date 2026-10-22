# Week 03 — Testable Requirements and Acceptance Criteria

## เป้าหมาย

ตรวจ critical requirements 3–5 ข้อจาก SRS จริง ค้น Ambiguous/Incomplete/Inconsistent/Infeasible/Not Testable ปรับข้อความโดยรักษา trace และเขียน Acceptance Criteria ที่ตัดสินผ่าน–ไม่ผ่านได้

## Input

- Requirement/SRS ID, text, version และ location ที่เปิดตรวจได้
- W01 Quality Risk Cards
- W02 critical slice/Route Map
- Stakeholder/business rule และ glossary เท่าที่มีจริง

W01/W02 ไม่ครบก็เริ่มได้ แต่ต้องเลือก requirement จาก Proposal/SRS และบันทึก missing context เป็น open question แทนการเดา

## ขั้นตอนทำงาน

1. เลือก 3 critical requirements ก่อน; เพิ่มเป็น 4–5 เมื่อความเสี่ยง/เวลาจำเป็น
2. บันทึก original ID/text/source/version โดยไม่แก้ต้นฉบับเงียบ ๆ
3. ตรวจ issue type และ Five-check: ความชัด/ไม่กำกวม, ความครบ, ความสอดคล้อง, ความเป็นไปได้ และความสามารถในการทดสอบ
4. เขียน issue/question และยก counterexample เมื่อช่วยเปิด ambiguity
5. ปรับ requirement โดยใช้ actor/trigger/action/observable result/business rule เท่าที่มีหลักฐาน
6. หากตัดสินไม่ได้ ให้บันทึก open question + decision owner + due/decision point และสถานะ `Not Ready`
7. เขียน Acceptance Criteria 2–5 ข้อต่อ requirement; มี normal และ negative/boundary ตาม risk
8. Peer review และแก้ไขอย่างน้อยหนึ่งรอบ
9. บันทึก AI use เมื่อมี แล้ว export W03-OUT

ใช้ `work/critical-requirement-review.md` และ `work/peer-review-and-ai.md`

## งานส่ง — W03-OUT

- Revised Critical Requirements 3–5 ข้อ + Acceptance Criteria ฉบับ v1
- ชื่อไฟล์: `W03_<TeamName>_Revised-Critical-Requirements_v1.pdf`
- วางที่: `WEEKS/week-03/submission/`

ต่อ requirement ต้องมี original ID/text, issue/question, revised wording, AC 2–5 ข้อ และ linked risk/stakeholder

## Definition of Done

- [ ] ทุกข้อ trace ไปยัง SRS ID/version และ risk/stakeholder ได้
- [ ] ผ่านจุดตรวจหรือมี open question/owner สำหรับส่วนที่ยัง Not Ready
- [ ] AC ตัดสินผ่าน–ไม่ผ่านได้ ไม่เพียงทวน requirement
- [ ] มี normal และ negative/boundary criterion ตาม risk
- [ ] ไม่มีผลทดสอบ log screenshot หรือ approval ที่แต่งขึ้น
- [ ] มี peer review, revision note และ AI declaration เมื่อใช้ AI
- [ ] ชื่อไฟล์ path tag และ `STATUS.md` ตรงกัน

## Handoff ไป Week 04

ส่งต่อ original/revised requirement, issue/open question, Acceptance Criteria และ peer-review revision เพื่อสร้าง SRS Review Log, RTM Lite และ Quality Gate A
