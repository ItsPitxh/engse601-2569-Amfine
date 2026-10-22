# W03 Peer Review, Revision and AI Record

## Peer review

- Draft commit/version: จะกรอก commit hash หลัง commit (ดู `STATUS.md`)
- Author(s): Peachu
- Reviewer(s): Peachu (self-review) · โครงงาน ENGSE212 เป็นโครงงานผู้ดำเนินงานคนเดียวตาม Proposal §9.2 · ไม่มี peer ภายในทีม — เขียนตรงนี้เพื่อความโปร่งใสและขอให้อาจารย์ที่ปรึกษาตรวจเป็นลำดับถัดไปตามแนวทาง `TEAM.md`
- Date: 2026-10-22

| Finding ID | Requirement/AC location | Finding/question | Disposition | Revision made / open action | Owner | Re-check |
|---|---|---|---|---|---|---|
| W03-PR-01 | FR-05 original text (Proposal §3.2) | ไม่ระบุประเภท/ขนาดไฟล์ที่อนุญาต · อาจทำให้ TC-05 ตีความได้หลายแบบ | Fix | เพิ่ม JPG/PNG/PDF ≤ 5 MB ใน revised wording · บันทึก open question เรื่องเพดานไฟล์ไปยังบริษัท | Peachu | หลังบริษัทยืนยัน (Sprint 1) |
| W03-PR-02 | FR-11 original text (Proposal §3.2) | ไม่ระบุพฤติกรรมเมื่อ LINE API fail · ไม่มี statistic (P95/mean) ชัด | Fix | เพิ่ม retry 2 ครั้ง + fallback + P95 30 รอบ · บันทึก open question เรื่อง interval retry | Peachu | หลัง PoC |
| W03-PR-03 | FR-15 original text (Proposal §3.2) | ไม่พูดถึงสิทธิของเจ้าของข้อมูลตาม PDPA (right to access/delete) · ไม่กำหนด retention | Fix | เพิ่ม endpoint right-to-access/delete + application-layer encryption · บันทึก open question เรื่อง wording consent | Peachu + อาจารย์ที่ปรึกษา | หลังปรึกษาอาจารย์ |
| W03-PR-04 | TC-05, TC-11, TC-15 (Proposal §3.7 ตารางที่ 9) | TC ยังไม่มีเกณฑ์ Pass เชิงปริมาณ (P95, จำนวนรอบ, field ที่ตรวจ) | Defer | เขียนไว้ใน Acceptance Criteria ของ W03 แทน · test case ของ Phase 2 จะไปขยายใน Week 05+ | Peachu | เมื่อเขียน test suite ใน Sprint 1 |

## Revision note

- จาก draft → revision commit/version: draft แรก (ก่อน commit) · revision นี้เป็นการตรวจ self-review ของ Peachu
- เปลี่ยนอะไรและเพราะอะไร: ขยาย FR-05/FR-11/FR-15 ให้มีเกณฑ์วัดได้ (ปริมาณไฟล์ · P95 timing · เขตข้อมูล PDPA ที่เข้ารหัส) และเพิ่ม Acceptance Criteria ที่ครอบคลุม normal + negative
- ยังมี open issue ใด: 3 ข้อตามตารางด้านบน + wording PDPA consent + retention period
- Reviewer re-check result: **Conditional** · ไปต่อ W04 ได้โดยบันทึก open decision; จะเข้า Ready หลังอาจารย์ที่ปรึกษาตรวจและบริษัทยืนยันพารามิเตอร์

## AI Use Declaration

- ใช้ AI: **Yes**
- ใช้เพื่อ: ร่างโครง Requirement Record และตารางช่วยอ่าน · เรียบเรียงถ้อยคำของ revised wording · เสนอ Acceptance Criteria ที่ครอบคลุม normal + negative (ผู้ดำเนินโครงงานตรวจและตัดส่วนที่ไม่ตรงกับ Proposal ออก)
- Input ที่ให้/วิธีปกป้องข้อมูล: ให้ Proposal v1 ซึ่งเป็นเอกสารของผู้ดำเนินโครงงานเอง · ไม่ได้ให้ข้อมูลลูกค้าจริงของบริษัท · ไม่ได้ให้ credential ใด ๆ
- ข้อเสนอที่ใช้/แก้/ปฏิเสธ:
  - **Accepted**: โครงตารางตรวจ Clear/Complete/Consistent/Feasible/Testable
  - **Modified**: ขนาดไฟล์ 5 MB (AI เสนอ 10 MB · ปรับให้ตรงกับ GitHub upload limit ปกติ) · P95 (AI เสนอค่า mean · ปรับให้สอดคล้องกับ NFR-01 ที่ใช้ P95)
  - **Rejected**: ข้อเสนอให้เพิ่ม field "biometric" ใน PII (ไม่ปรากฏใน Proposal และไม่จำเป็นต่อ scope)
- ตรวจสอบกับ SRS/owner อย่างไร: ทวนทุกแถวกลับกับ Proposal §3.2, §3.4, §3.6, §3.7, §4, §7, §8 เพื่อยืนยันว่าทุก revision มีที่มา
- Verification owner/date: Peachu · 2026-10-22

**ทีม Amfine ยืนยันว่าไม่มี stakeholder decision, approval, test result, log หรือ screenshot ที่ AI/ทีมสร้างขึ้นโดยไม่ได้ดำเนินการจริง** · open question ที่ยัง block Phase 2 ถูกบันทึกไว้ครบในตารางด้านบนและใน `WEEKS/week-04/work/04-gate-a-decision.md`
