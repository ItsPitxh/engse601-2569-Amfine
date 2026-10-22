# Week 02 — Project Quality Route Map

## เป้าหมาย

เชื่อมสถานะจริงของ ENGSE212 กับเส้นทาง Requirements/SRS → Design → Implement/Build → Test/Defect → Release/Portfolio โดยใช้หนึ่ง critical requirement/feature/risk เป็นแกน เห็นคำถาม V&V, หลักฐาน, Quality Gate และ feedback loop

## Input

- W01 Quality Risk Cards หรือ critical risk/feature จาก Proposal/SRS
- สถานะ SDLC และ milestone/sprint ปัจจุบันจาก `PROJECT.md`
- SRS, design note, repository/build information เท่าที่มีจริง

## ขั้นตอนทำงาน

1. เลือก critical slice เพียงหนึ่งรายการ ไม่ต้อง map ทั้งระบบ
2. ระบุสถานะโครงงานปัจจุบันและ milestone/sprint
3. เขียน V&V question ในแต่ละช่วงของ SDLC
4. ระบุ evidence และสถานะ `Existing/Planned/Not Ready/Not Executed`
5. เชื่อม Gate A–D หรือ decision point ที่เหมาะสม
6. ระบุ owner/when และ feedback loop อย่างน้อยหนึ่งจุด
7. Peer review ว่า flow อ่านได้และไม่มี evidence สมมติ
8. Export route map เป็นหนึ่งหน้า; แนบ AI declaration หน้า 2 ได้เมื่อใช้ AI

ใช้ `work/project-quality-route-map.md`

## งานส่ง

- Project Quality Route Map v1 หนึ่งหน้า
- ชื่อไฟล์: `W02_<TeamName>_Project-Quality-Route-Map_v1.pdf`
- วางที่: `WEEKS/week-02/submission/`

## Definition of Done

- [ ] ระบุสถานะจริงและ critical slice
- [ ] เห็น flow Requirements/SRS → Design → Implement → Test → Decision แม้บางช่วงยังไม่พร้อม
- [ ] ทุกช่วงมี V&V question และ evidence ที่ตรวจได้หรือวางแผนชัด
- [ ] evidence status ซื่อสัตย์
- [ ] มี Gate/decision point, owner/when และ feedback loop อย่างน้อย 1 จุด
- [ ] ผ่าน peer review และมี AI Use Declaration เมื่อใช้ AI
- [ ] ชื่อไฟล์ path tag และ `STATUS.md` ตรงกัน

## Handoff ไป Week 03

เลือก Requirement ID 3–5 ข้อที่สัมพันธ์กับ critical slice/risks เพื่อทำ testability review และ Acceptance Criteria โดยให้เริ่มจาก 3 ข้อก่อน
