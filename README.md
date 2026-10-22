# ENGSE601 — Team V&V Evidence Repository

> Template สำหรับแต่ละกลุ่ม ใช้เก็บข้อมูลตั้งต้น งานระหว่างทำ และหลักฐานส่งของ ENGSE601 ที่เชื่อมกับโครงงาน ENGSE212

> ## อัปเดต 21 ต.ค. 2569 · อ่านก่อน
>
> **ส่งงานกลุ่มทั้งหมดภายในศุกร์ 23 ต.ค. 2569 เวลา 23:59** ผ่าน repo นี้ ตามรายการใน [SUBMISSIONS.md](SUBMISSIONS.md) แล้วสร้าง Release ชื่อ `engse601-submit`
>
> | งาน | วางที่ |
> |---|---|
> | W01–W05 | `WEEKS/week-01` ถึง `week-05` ในโฟลเดอร์ `submission/` |
> | ใบงานครั้งที่ 1 ส่วน B | [01-plan/](01-plan/) |
> | ใบงานครั้งที่ 2 ส่วน B | [02-test-design/](02-test-design/) |
> | ใบงานรวม 3–4 ส่วน B1 และ B3 | [03-test-execution/](03-test-execution/) · [TEAM.md](TEAM.md) · [AI-LOG.md](AI-LOG.md) |
>
> - repo เป็น **Public** · ห้ามใส่รหัสนักศึกษา และห้ามวางงานเดี่ยวส่วน A
> - ไม่ต้องทำใบงานรวม 3–4 ส่วน B2 และสัปดาห์ที่ 6–17
> - ทีมที่สร้าง repo ไปแล้ว ดูวิธีอัปเดตใน [UPDATE-2569-10.md](UPDATE-2569-10.md) · ทีมที่ยังไม่มี repo กด **Use this template**
> - ดูตัวอย่างที่ทำครบทุกชิ้น (Team00 · Case X): https://github.com/se-rmutl/ENGSE601-Team00-CaseX-Example · ห้ามคัดลอก

## 1. เริ่มต้นตรงนี้

ก่อนเริ่ม Week 01 ให้ทีมทำตามลำดับนี้

1. สร้าง repository ของทีมจาก template นี้ และตั้งชื่อแนะนำเป็น `engse601-<year>-<team-name>`
2. กำหนด repository เป็น **Public** เพื่อให้ผู้สอนอ่านและดาวน์โหลดไปตรวจได้ · ห้ามใส่รหัสนักศึกษาและข้อมูลส่วนบุคคล
3. เพิ่มสมาชิกทุกคนและอาจารย์ตามสิทธิ์ที่กำหนด
4. กรอก [PROJECT.md](PROJECT.md) และ [TEAM.md](TEAM.md)
5. นำ Proposal, Requirement/SRS และเอกสารออกแบบที่มีอยู่มา **วางหรือเชื่อมโยง** ตาม [INPUTS/README.md](INPUTS/README.md)
6. กรอก [INPUTS/input-register.md](INPUTS/input-register.md) ให้เห็นชื่อเอกสาร version, owner และ source of truth
7. อ่าน [CONTRIBUTING.md](CONTRIBUTING.md) เพื่อใช้ branch, commit, review และ tag ให้เป็นวิธีเดียวกันทั้งทีม
8. ตรวจรายการพร้อมเริ่มใน [STATUS.md](STATUS.md) แล้วจึงเปิด `WEEKS/week-01/README.md`

## 2. หลักการใช้ repository

```text
READ        เอกสารสอน/Worksheet จาก Course Repo หรือ LMS
   ↓
INPUT       Proposal + Requirement/SRS + artifact จริงจาก ENGSE212
   ↓
WORK        กรอก template และบันทึกการทบทวนใน WEEKS/week-XX/work/
   ↓
CHECK       Peer review + Definition of Done + ตรวจการใช้ AI
   ↓
SUBMIT      Export PDF ไปที่ WEEKS/week-XX/submission/
   ↓
TRACE       Commit + tag + บันทึก URL/commit hash ใน STATUS.md
   ↓
HANDOFF     ใช้ output เป็น input ของสัปดาห์ถัดไปและงาน ENGSE212
```

เอกสารใน `INPUTS/` คือข้อมูลต้นทาง ไม่ควรแก้ทับโดยไม่เปลี่ยน version ส่วนไฟล์ใน `work/` แก้ได้ระหว่างทำ และไฟล์ใน `submission/` คือสำเนาที่ทีมประกาศว่าใช้ส่งในรอบนั้น

## 3. สถานะหลักฐานที่ต้องใช้ตรงกัน

| Status | ใช้เมื่อ | สิ่งที่ต้องอ้างอิง |
|---|---|---|
| `Existing` | หลักฐานมีอยู่จริงและเปิดตรวจได้ | path/URL, version/build, วันที่หรือ commit |
| `Planned` | วางแผนจะสร้าง แต่ยังไม่เกิด | owner, next action, ช่วงเวลาที่คาดไว้ |
| `Not Ready` | ยังทำไม่ได้เพราะมี decision/input/blocker ขาด | blocker, decision owner, next action |
| `Not Executed` | ออกแบบการทดสอบแล้วแต่ยังไม่ได้รัน | test/case ที่วางแผนไว้; **ห้ามใส่ผลสมมติ** |

ห้ามสร้าง test result, log, screenshot, approval, stakeholder decision หรือหลักฐานที่ทีมไม่ได้ดำเนินการจริง หากใช้ AI ต้องเปิดเผยและตรวจข้อเสนอเทียบกับ artifact ของทีมเสมอ

## 4. แผนหลักฐาน Week 01–04

| Week | ใช้อะไรเป็น Input | ทำอะไร | ไฟล์ส่งมาตรฐาน | นำไปใช้ต่อ |
|---|---|---|---|---|
| 01 | Proposal, Requirement/SRS, stakeholder context | Quality Risk Cards 3–5 รายการ | `W01_<TeamName>_Quality-Risk-Cards_v1.pdf` | เลือก critical risk/feature ใน Week 02 |
| 02 | W01 + สถานะ SDLC ของ ENGSE212 | Project Quality Route Map 1 critical slice | `W02_<TeamName>_Project-Quality-Route-Map_v1.pdf` | ตั้ง V&V questions/evidence/gates และเลือก requirement สำหรับ Week 03 |
| 03 | SRS จริง + W01/W02 | ตรวจ testability, ปรับ 3–5 requirements, เขียน Acceptance Criteria | `W03_<TeamName>_Revised-Critical-Requirements_v1.pdf` | เป็น input ของ Review Log และ RTM Lite |
| 04 | W03-OUT + SRS/version + risk/design notes | Requirement Review, RTM v1, Gate A | `W04_<TeamName>_SRS-Review-and-RTM_v1.pdf` | Phase 2 Entry Pack สำหรับ Component/Integration/System/UAT |

รายละเอียด ขั้นตอน แบบกรอก และ Definition of Done อยู่ใน README ของแต่ละสัปดาห์

> หมายเหตุเรื่อง path: เอกสารสอน Week 01–02 ระบุ `01-foundation/` และ `02-quality-route-map/` เป็นทางเลือกชั่วคราวสำหรับทีมที่ยังไม่มีโครงสร้าง เมื่อใช้ template นี้ให้ถือ `WEEKS/week-01/submission/` และ `WEEKS/week-02/submission/` เป็นตำแหน่งมาตรฐาน เพื่อไม่ให้เกิดไฟล์ซ้ำสองที่

## 5. วิธีส่งงานรายสัปดาห์

1. ทีมทำงานใน branch เช่น `week-03/requirement-review`
2. กรอก template ใน `work/` และอัปเดต reference ไปยัง input จริง
3. ให้สมาชิกที่ไม่ใช่ผู้เขียนหลักทำ peer review และบันทึกผล
4. ตรวจ Definition of Done ใน README ของสัปดาห์
5. Export ไฟล์ส่งเป็น PDF ด้วยชื่อมาตรฐาน แล้ววางใน `submission/`
6. Commit ด้วยรูปแบบ `submit(W03): revised critical requirements v1`
7. Merge เข้า `main` เมื่อทีมตรวจครบ
8. สร้าง tag เช่น `w03-submission-v1`
9. กรอก tag, commit hash และ URL ใน [STATUS.md](STATUS.md)
10. ส่ง URL ของ repository พร้อม tag/commit hash ผ่านช่องทางที่อาจารย์กำหนด

หากแก้หลังส่ง ให้เพิ่ม version และ tag เช่น `v2` ห้ามแทนที่ประวัติโดยไม่อธิบายเหตุผลใน `STATUS.md`

## 6. โครงสร้างสำคัญ

```text
.
├── PROJECT.md                 ข้อมูลและสถานะโครงงาน ENGSE212
├── TEAM.md                    สมาชิก บทบาท และผู้รับผิดชอบ
├── STATUS.md                  สถานะและหลักฐานการส่งรายสัปดาห์
├── CONTRIBUTING.md            วิธีทำงานร่วมกันด้วย Git
├── INPUTS/                    Proposal/SRS/design และทะเบียน input
├── TEMPLATES/                 แบบบันทึกกลางที่ใช้ซ้ำได้
├── SUBMISSIONS.md             หน้าส่งงานกลุ่มหน้าเดียว (ใช้ตั้งแต่ 21 ต.ค. 2569)
├── 01-plan/                   ใบงานครั้งที่ 1 ส่วน B
├── 02-test-design/            ใบงานครั้งที่ 2 ส่วน B
├── 03-test-execution/         ใบงานรวม 3–4 ส่วน B1 · tests/ · evidence/
└── WEEKS/
    ├── week-01/ ... week-05/  คำสั่ง งานระหว่างทำ และจุดวางไฟล์ส่ง
    └── week-06/ ... week-17/  ไม่ได้ใช้ในภาคนี้
```

## 7. Source of truth

- สถานะและ source of truth ของ Proposal/SRS/Design: `INPUTS/input-register.md`
- สถานะการส่ง ENGSE601: `STATUS.md`
- โค้ด/build จริงของ ENGSE212: ใส่ URL และ commit/build reference ใน `PROJECT.md`; ไม่จำเป็นต้องคัดลอก source code มาที่ repo นี้
- หากข้อมูลไม่ตรงกัน ให้ยึด artifact version ที่ระบุใน input register และบันทึกการเปลี่ยนแปลงก่อนใช้งานต่อ
