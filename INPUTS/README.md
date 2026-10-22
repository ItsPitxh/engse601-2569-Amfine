# INPUTS — ข้อมูลตั้งต้นจาก ENGSE212

โฟลเดอร์นี้เก็บหรือเชื่อมโยง artifact ที่ ENGSE601 นำมาใช้ตรวจสอบ ห้ามถือว่าไฟล์ล่าสุดคือ source of truth เพียงเพราะชื่อดูใหม่กว่า ให้กรอก version และสถานะใน `input-register.md`

## สิ่งที่ต้องมีอย่างน้อยก่อน Week 01

- Proposal/แบบร่างโครงงานที่ผ่านการเสนอหัวข้อ
- Requirement หรือ SRS ที่มีอยู่ แม้ยังไม่สมบูรณ์
- รายชื่อ stakeholder/user และบริบทปัญหาเท่าที่เปิดเผยได้
- URL ของ ENGSE212 project repository หรือพื้นที่ทำงานของทีม
- ข้อมูลสถานะ SDLC ปัจจุบันและ milestone/sprint

ถ้ามี ให้เพิ่ม HLD/detail design, prototype, glossary, risk list, decision log และเอกสาร interface/API แต่ไม่ต้องรอให้ครบจึงเริ่ม Week 01 ให้ระบุสิ่งที่ขาดเป็น `Not Ready` พร้อม owner/next action

## วิธีเพิ่ม input

1. เลือกว่าจะเก็บไฟล์จริงใน repo หรือเก็บในระบบที่ได้รับอนุญาตแล้วใส่ URL
2. ตั้งชื่อให้มี artifact และ version เช่น `SRS_v0.6_2026-07-17.pdf`
3. วางไฟล์/ลิงก์ในโฟลเดอร์ที่เกี่ยวข้อง
4. เพิ่มหนึ่งแถวใน `input-register.md`
5. ระบุ `Current`, `Superseded`, `Draft` หรือ `Not Ready`
6. เมื่อเปลี่ยน version ให้เพิ่มแถวใหม่และบันทึกผลกระทบ ห้ามแก้ทับโดยไม่มีประวัติ

## Privacy และ AI

- ลบ/ปกปิดข้อมูลส่วนบุคคลหรือข้อมูลลับที่ไม่จำเป็น
- ห้าม commit credential
- ห้ามส่ง artifact ที่เป็นความลับให้ AI โดยไม่มีสิทธิ์
- หากใช้ URL ต้องตรวจว่าผู้สอนและสมาชิกที่เกี่ยวข้องเปิดได้ โดยไม่ใส่ password ลงใน repo
