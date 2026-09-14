# Engineering Monitoring Dashboard

โปรเจกต์รายวิชา การเขียนโปรแกรมและการพัฒนาซอฟต์แวร์ 
เป็นระบบเว็บแอปพลิเคชันจำลองเพื่อการติดตามสถานะของระบบวิศวกรรมต่างๆ พัฒนาด้วย **Python**, **Streamlit** และทดสอบโค้ดด้วย **pytest** 

## 🛠️ สิ่งที่ต้องเตรียม

- Python 3
- Git

## 📥 วิธีการติดตั้ง (Installation)

1. **โคลนโปรเจกต์ลงเครื่อง**
   ```bash
   git clone <repo-url>
   cd engineering-dashboard
   ```

2. **สร้างและเปิดใช้งาน Virtual Environment**
   ```powershell
   # สำหรับ Windows PowerShell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   
   # สำหรับ macOS / Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **ติดตั้งแพ็กเกจที่จำเป็น**
   ```powershell
   pip install -r requirements.txt
   ```

## 🚀 วิธีรันโปรเจกต์ (Running the Dashboard)

เมื่อติดตั้งแพ็กเกจเสร็จสิ้น สามารถรัน Dashboard ได้ด้วยคำสั่ง:

```bash
streamlit run app.py
```
จากนั้นตัวเว็บเบราว์เซอร์จะเปิดลิงก์ `http://localhost:8501` ขึ้นมาโดยอัตโนมัติ คุณสามารถเปลี่ยนหน้าไปยังโมดูลต่างๆ ได้จากเมนูด้านซ้าย

## 🧪 วิธีการรัน Unit Test

เพื่อทดสอบความถูกต้องของระบบและตรวจสอบข้อผิดพลาด ให้รันคำสั่ง:

```bash
python -m pytest -q
```

**หมายเหตุการส่งงาน (QA)**:
- ก่อนเปิด Pull Request สมาชิกทุกคนต้องรันคำสั่ง `pytest -q` และตรวจสอบว่า Test ผ่านทั้งหมด (`100%`)
- ตรวจสอบให้แน่ใจว่าได้แบ่งแยกความรับผิดชอบในส่วน Logic (`services/`), หน้าจอ (`pages/`), และ Unit Test (`tests/`) ออกจากกันอย่างชัดเจน
