# W04-03 — RTM Lite Guide

กรอก `03-rtm-lite.csv` หนึ่งแถวต่อ Requirement/Acceptance Basis ที่อยู่ใน review scope

## Forward trace

เริ่มจาก Requirement ID แล้วตรวจว่ามี source/version, linked risk/stakeholder, acceptance basis, planned test level และ planned evidence หรือไม่

## Backward trace

เลือก planned evidence/test level แล้วย้อนกลับได้ว่าหลักฐานนั้นตอบ Requirement และ risk/acceptance basis ใด หากย้อนกลับไม่ได้ ให้บันทึก trace gap ใน Review Log

## กติกา status

- `Existing`: artifact เปิดตรวจได้และมี version/path
- `Planned`: ระบุ owner/next action
- `Not Ready`: ระบุ blocker/decision owner
- `Not Executed`: test design อาจมีแล้ว แต่ยังไม่มี actual result

ช่อง Planned Evidence ห้ามใส่ผล pass/fail, log หรือ screenshot เสมือนรันแล้ว
