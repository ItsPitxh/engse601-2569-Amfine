# วิธีทำงานร่วมกันและส่งหลักฐานด้วย Git

## Workflow ที่แนะนำ

1. ก่อนเริ่มงานให้ `pull` จาก `main`
2. สร้าง branch ตามสัปดาห์ เช่น `week-02/route-map`
3. แก้ template และเพิ่มหลักฐานทีละส่วน ไม่รอ commit ครั้งเดียวตอนจบ
4. ใช้ข้อความ commit ที่บอกสิ่งที่เปลี่ยน เช่น
   - `docs(W01): add quality risk cards draft`
   - `review(W03): record peer comments and revisions`
   - `submit(W04): add baseline package v1`
5. เปิด Pull/Merge Request หรือให้เพื่อนตรวจ diff ก่อน merge
6. ตรวจ Definition of Done และไฟล์ใน `submission/`
7. Merge เข้า `main` แล้วสร้าง tag ของรอบส่ง
8. บันทึก tag/commit hash ใน `STATUS.md`

## Naming rules

- ชื่อ directory ใน template ใช้ตามเดิม
- `<TeamName>` ต้องตรงกับ `PROJECT.md` และใช้รูปแบบเดิมทุกสัปดาห์
- ไฟล์ส่งใช้ `WXX_<TeamName>_<Artifact>_vN.pdf`
- รูป/ไฟล์สนับสนุนใช้ชื่อสื่อความหมาย เช่น `srs-v0.6-section-3.png` ไม่ใช้ `image1.png`
- เมื่อแก้หลังส่ง เพิ่ม `v2`, `v3` และ tag ใหม่ ไม่ลบประวัติเดิม

## Review rules

- ผู้เขียนหลักไม่ควรเป็นผู้อนุมัติงานของตนเองเพียงคนเดียว
- Reviewer ตรวจทั้งเนื้อหา source/version, path/link และความสอดคล้องกับ Definition of Done
- Comment ที่ยังไม่ปิดต้องระบุ disposition, owner และ next action
- การ merge หมายถึง “ตรวจตามเกณฑ์แล้ว” ไม่ได้หมายความว่า stakeholder อนุมัติ เว้นแต่มีหลักฐานจริง

## สิ่งที่ห้าม commit

- password, token, API key, credential และไฟล์ `.env`
- ข้อมูลส่วนบุคคล/ข้อมูลลับที่ไม่จำเป็น
- dataset ที่ไม่มีสิทธิ์เผยแพร่
- test result, screenshot, log, approval หรือ decision ที่สร้างขึ้นโดยไม่ได้ดำเนินการจริง
- binary ขนาดใหญ่มากโดยไม่ตกลงกับอาจารย์; ให้เก็บในที่ที่ได้รับอนุญาตแล้วใส่ URL/checksum แทน

## เมื่อเกิด conflict หรือ input เปลี่ยน

1. อย่าเลือกทิ้งการเปลี่ยนแปลงของเพื่อนโดยไม่ตรวจ
2. เปิด artifact ทั้งสอง version และตกลง source of truth
3. อัปเดต `INPUTS/input-register.md`
4. ตรวจผลกระทบต่อ W01–W04 และแก้ trace/revision history ที่เกี่ยวข้อง
5. Commit พร้อมอธิบายเหตุผลของการเปลี่ยน baseline
