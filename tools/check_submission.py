#!/usr/bin/env python3
"""ตรวจความครบเบื้องต้นของ repo ทีม ENGSE601 ตาม SUBMISSIONS.md

ไม่ให้คะแนน และไม่ตัดสินเนื้อหา · ผู้สอนเป็นผู้ตรวจ
ใช้:  python3 tools/check_submission.py [โฟลเดอร์ของ repo]
"""
import os, re, sys, glob

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..'))
ITEMS = [
    ('G1', 'W01 Quality Risk Cards', 'WEEKS/week-01/submission/W01_*_Quality-Risk-Cards_v*.pdf'),
    ('G2', 'W02 Project Quality Route Map', 'WEEKS/week-02/submission/W02_*_Project-Quality-Route-Map_v*.pdf'),
    ('G3', 'W03 Revised Critical Requirements', 'WEEKS/week-03/submission/W03_*_Revised-Critical-Requirements_v*.pdf'),
    ('G4', 'W04 SRS Review และ RTM', 'WEEKS/week-04/submission/W04_*_SRS-Review-and-RTM_v*.pdf'),
    ('G5', 'W05 Requirement-to-Design Trace', 'WEEKS/week-05/submission/W05_*_Requirement-to-Design-Trace_v*.pdf'),
    ('G6', 'ใบงานครั้งที่ 1 ส่วน B', '01-plan/S1-B_*.pdf'),
    ('G7', 'ใบงานครั้งที่ 2 ส่วน B', '02-test-design/S2-B_*.pdf'),
]
ID_RE = re.compile(r'\b6\d{10}-\d\b')
TEXT_EXT = ('.md', '.txt', '.csv', '.json', '.js', '.ts', '.py', '.java', '.html')
lines, warns = [], []

def ok(m): lines.append('✅ ' + m)
def no(m): lines.append('⬜ ' + m)
def warn(m): warns.append('⚠️ ' + m)

for code, name, pat in ITEMS:
    found = glob.glob(os.path.join(ROOT, pat))
    (ok if found else no)(f'{code} {name}: ' + (', '.join(os.path.relpath(f, ROOT) for f in found) if found else f'ยังไม่พบไฟล์ `{pat}`'))

ex = os.path.join(ROOT, '03-test-execution')
report = os.path.join(ex, 'execution-report.md')
pdf = glob.glob(os.path.join(ex, 'S34-B1_*.pdf'))
rep_txt = open(report, encoding='utf-8', errors='replace').read() if os.path.isfile(report) else ''
filled = rep_txt and rep_txt.count('[กรอก]') < 10
(ok if (filled or pdf) else no)('G8 ตารางผล B1: ' + ('กรอก execution-report.md แล้ว' if filled else ('พบ ' + os.path.basename(pdf[0]) if pdf else 'execution-report.md ยังเป็นแบบว่าง และไม่พบ S34-B1_<TeamName>.pdf')))
tests = [f for f in glob.glob(os.path.join(ex, 'tests', '**', '*'), recursive=True) if os.path.isfile(f) and not f.endswith('README.md')]
(ok if tests else no)(f'G8 โค้ดทดสอบใน 03-test-execution/tests/: {len(tests)} ไฟล์')
evid = [f for f in glob.glob(os.path.join(ex, 'evidence', '**', '*'), recursive=True) if os.path.isfile(f) and not f.endswith('README.md')]
(ok if evid else no)(f'G8 หลักฐานใน 03-test-execution/evidence/: {len(evid)} ไฟล์')
for link in re.findall(r'\]\((evidence/[^)\s]+)\)', rep_txt):
    if not os.path.exists(os.path.join(ex, link)):
        warn(f'execution-report.md ลิงก์ไปไฟล์ที่ไม่มีอยู่: {link}')
team = open(os.path.join(ROOT, 'TEAM.md'), encoding='utf-8', errors='replace').read() if os.path.isfile(os.path.join(ROOT, 'TEAM.md')) else ''
(ok if 'ใครทำส่วนไหน' in team and team.count('[กรอก]') < 6 else no)('G9 TEAM.md มีตาราง “ใครทำส่วนไหน” และกรอกแล้ว')
ai = open(os.path.join(ROOT, 'AI-LOG.md'), encoding='utf-8', errors='replace').read() if os.path.isfile(os.path.join(ROOT, 'AI-LOG.md')) else ''
(ok if ai and '[กรอก]' not in ai else no)('G9 AI-LOG.md กรอกแล้ว หรือเขียนว่าไม่ได้ใช้ AI')

for dp, dn, fn in os.walk(ROOT):
    if '.git' in dp.split(os.sep):
        continue
    for f in fn:
        p = os.path.join(dp, f); rel = os.path.relpath(p, ROOT)
        if ID_RE.search(f):
            warn(f'ชื่อไฟล์มีรหัสนักศึกษา: {rel}')
        if re.search(r'S\d+-A_|S34-A', f):
            warn(f'พบไฟล์ส่วน A (งานเดี่ยว) ใน repo: {rel} · ส่วน A ส่งทาง Google Form เท่านั้น')
        if f.endswith(TEXT_EXT) and os.path.getsize(p) < 2_000_000:
            try:
                if ID_RE.search(open(p, encoding='utf-8', errors='ignore').read()):
                    warn(f'พบรูปแบบรหัสนักศึกษาในไฟล์: {rel} · repo เป็น Public ให้ลบออก')
            except OSError:
                pass

out = ['## ผลตรวจความครบเบื้องต้น ENGSE601', '', 'ตรวจเฉพาะว่ามีไฟล์ครบหรือไม่ ไม่ได้ตรวจเนื้อหา · กำหนดส่ง ศุกร์ 23 ต.ค. 2569 23:59', ''] + lines
if warns:
    out += ['', '### ต้องแก้'] + warns
out += ['', 'อย่าลืมสร้าง Release `engse601-submit` เมื่อพร้อมส่ง ดู SUBMISSIONS.md']
text = '\n'.join(out)
print(text)
summ = os.environ.get('GITHUB_STEP_SUMMARY')
if summ:
    open(summ, 'a', encoding='utf-8').write(text + '\n')
sys.exit(0)
