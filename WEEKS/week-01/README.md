# Week 01 — Quality Risk Cards

## เป้าหมาย

ใช้ Proposal และ Requirement/SRS จริงของ ENGSE212 เพื่อเปลี่ยนคำว่า “คุณภาพ” ให้เป็นความเสี่ยงที่ทีมอธิบายได้ว่าอะไรอาจผิด ใครได้รับผลกระทบ ควร Verification/Validation อย่างไร และอยากเห็นหลักฐานอะไร

## ก่อนเริ่ม

- [ ] `PROJECT.md` และ `TEAM.md` ถูกกรอกแล้ว
- [ ] Proposal และ Requirement/SRS ถูกลงทะเบียนใน `INPUTS/input-register.md`
- [ ] สมาชิกทุกคนเปิด source ที่อ้างอิงได้
- [ ] ทีมทราบว่าข้อมูลใดห้ามเผยแพร่หรือส่งให้ AI

หากยังมีเพียง Proposal หรือ SRS บางส่วน ให้เริ่มจาก feature/stakeholder ที่เป็นหัวใจของโครงงาน และระบุช่องว่างเป็น `Not Ready` โดยไม่เดาข้อมูล

## Input

- Proposal/แบบร่างโครงงาน ENGSE212
- Requirement/SRS version ปัจจุบัน
- Stakeholder/user context
- ขอบเขตและสถานะโครงงานปัจจุบัน

## ขั้นตอนทำงาน

1. เลือก requirement/feature/stakeholder situation จริง 3–5 จุด
2. เขียน risk statement ให้เห็น **เหตุการณ์หรือเงื่อนไข + ผลกระทบ**
3. ระบุ quality concern ที่เกี่ยวข้องและเหตุผล
4. แยก Verification กับ Validation action
5. ระบุ evidence ที่มีจริงหรือวางแผน พร้อมสถานะ
6. ให้เพื่อนตรวจว่า risk ไม่เป็นคำกว้างและ trace กลับไปยัง input ได้
7. บันทึกการใช้ AI หากมี แล้ว export เป็นไฟล์เดียว

ใช้แบบกรอก `work/quality-risk-cards.md` และคัดลอก `TEMPLATES/ai-use-declaration.md` เพิ่มเมื่อใช้ AI

## งานส่ง

- 3–5 Quality Risk Cards รวมเป็นไฟล์เดียว
- ชื่อไฟล์: `W01_<TeamName>_Quality-Risk-Cards_v1.pdf`
- วางที่: `WEEKS/week-01/submission/`
- รูปแบบ: PDF 1–3 หน้า หรือเอกสารที่เปิดอ่านได้ พร้อม source/version และสมาชิก/ผู้ทบทวน

## Definition of Done

- [ ] มี 3–5 cards และแต่ละใบเชื่อมกับ requirement/SRS/stakeholder จริง
- [ ] Risk statement บอกเหตุการณ์และ impact ไม่ใช้คำกว้างอย่างเดียว
- [ ] Quality concern สอดคล้องกับบริบทและมีเหตุผลสั้น
- [ ] มี Verification/Validation action และ planned evidence ที่ตรวจได้
- [ ] ใช้ `Existing`, `Planned`, `Not Ready/Not Executed` ตามความจริง
- [ ] มี peer check และ AI Use Declaration เมื่อใช้ AI
- [ ] ชื่อไฟล์ path tag และ `STATUS.md` ตรงกัน

## Handoff ไป Week 02

เลือก risk/feature ที่สำคัญอย่างน้อยหนึ่งรายการจาก W01-OUT เป็น `critical slice` สำหรับวาง Project Quality Route Map จาก Requirements → Design → Implement → Test → Decision
