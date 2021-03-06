# palindrome.py

txt = input() #อีเกรดเดอร์ควาย
txt = txt.strip()
# สมมติให้ text = "AABB"

# เก็บความยาวตัวอักษร
l = len(txt)-1
# จะได้ l = 3

# ให้เริ่มจาก case ว่าไม่ใช่ หาเคสที่ใช่
status = "N"
# ประกาศตัวแปรมาเช็คเฉพาะในหนึ่งรอบ

# วนตามจำนวนความยาวตัวอักษร เริ่มนับที่ 0
for i in range(0,l+1):
    # ให้ลูปนี้เป็น palindrome แล้วค่อยหากรณีเท็จ
    oneLoop = True
    # เราจะตัดข้อความท่อนแรกมาต่อท่อนหลังจนจบ
    # เช่น ถ้าเป็น AABB เราจะตัดแบบนี้ (ตัดตาม slash)
    # ตัดเป็น       /AABB         A/ABB       AA/BB       AAB/B
    # ได้เป็น       AABB          ABBA        BBAA        BAAB
    # จะพบว่าข้อความท่อนแรกคือตัวที่ i ตามจำนวนครั้งที่วนลูป ถึงตัวสุดท้าย
    # และท่อนหลังคือตัวแรกถึง i
    # ให้ joint เท่ากับข้อความที่เกิดจากการต่อ
    joint = txt[i:] + txt[:i]
    # วนเป็นจำนวนครั้งเท่ากับครึ่งหนึ่งของความยาวสตริง
    for j in range(0,int((l+1)/2)):
        # ถ้าตัวที่ i เท่ากับตัวที่ (ความยาว-i)
        if joint[j]!=joint[l-j]:
            # ให้เป็น false
            oneLoop = False
        # วนจนเสร็จ ถ้า oneLoop ยังจริง (ก็คือไม่มีรอบไหนที่ไม่เท่ากัน)
    if oneLoop:
        status = "Y"

# จบลูปแล้วค่อยสั่ง print
print(status)
