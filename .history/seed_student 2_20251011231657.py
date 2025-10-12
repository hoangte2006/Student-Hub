import os
import django
import random
from datetime import date, timedelta
from typing import Tuple

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_manager.settings')
django.setup()

from students.models import Student

# --- DỮ LIỆU ĐẦU VÀO CƠ BẢN (KHÔNG ĐỔI) ---
names = [
  'An','Bình','Chi','Dũng','Hà','Hương','Khoa','Lan','Minh','Ngọc','Phúc','Quân',
  'Thảo','Trang','Vinh','Yến','Tuấn','Hải','Linh','Mai','Nam','Oanh','Phương',
  'Quỳnh','Sơn','Tú','Vy','Xuân','Đức','Hạnh','Khánh','Lộc','Mỹ','Nhi','Phát',
  'Quang','Thành','Trâm','Vân','Đăng','Huy','Kiên','Phú','Quý','Trung','Vũ',
  'Hoàng','Cường','Duy','Giang','Hùng','Khôi','Lâm','Phước','Quí','Thái','Trúc',
  'Vương','Đạt','Đan','Hân','Kha'
]

# Danh sách lớp học. Dữ liệu điểm số sẽ được tạo dựa trên tên trong danh sách này.
classrooms = ['10A1','10A2','11B1','11B2','12C1','12C2','12C3','12C4','12C5','12C6','12C7','12C8'] 
genders = ['M','F','O']
statuses = ['A','N','S']
application_statuses = ['pending','approved','rejected']
payment_statuses = ['paid','unpaid','partial']
addresses = ['TP.HCM','Hà Nội','Đà Nẵng','Cần Thơ','Huế','Nha Trang','Vũng Tàu','Phan Thiết','Biên Hòa','Bình Dương']
notes = ['Không có ghi chú','Đã gọi điện xác nhận','Cần bổ sung hồ sơ','Đã thanh toán một phần']
# -----------------------------------------------------


# --- HÀM XÁC ĐỊNH PHÂN BỐ ĐIỂM SỐ DỰA TRÊN TÊN LỚP (CỐT LÕI CỦA GIẢI PHÁP) ---
def get_score_params_by_classroom(classroom_name: str) -> Tuple[float, float]:
    """
    Trả về (mu, sigma) cho phân bố điểm số Gauss dựa trên tên lớp.
    Mu cao và Sigma thấp tạo ra lớp giỏi với điểm tập trung cao.
    """
    
    # Mặc định (cho lớp không rõ)
    default_mu, default_sigma = 6.5, 1.5

    try:
        # Tách Khối (10, 11, 12) và Hậu tố (A1, C5, B2)
        grade_level = int(classroom_name[:2])
        group_suffix = classroom_name[2:]
    except:
        return (default_mu, default_sigma)

    # 1. PHÂN LOẠI THEO NHÓM LỚP (Ưu tiên)
    # Lớp A1/B1/C1 -> Lớp chọn
    if '1' in group_suffix and group_suffix.endswith('1'): 
        # Lớp chọn (ví dụ: 10A1, 12C1)
        # Mu cao, Sigma thấp
        mu = 8.0 + (grade_level - 10) * 0.15 # Tăng nhẹ mu theo khối
        sigma = 0.8
    # Lớp A2/B2/C2 -> Lớp Khá
    elif '2' in group_suffix and group_suffix.endswith('2'):
        # Lớp Khá (ví dụ: 10A2, 12C2)
        mu = 6.8 + (grade_level - 10) * 0.1
        sigma = 1.2
    # Lớp C3 đến C8 -> Lớp Thường/Cần cải thiện (chủ yếu là khối 12)
    elif grade_level == 12 and any(suffix in group_suffix for suffix in ['C3', 'C4', 'C5', 'C6', 'C7', 'C8']):
        mu = 5.5 - (int(group_suffix[-1]) - 3) * 0.1 # Càng C... lớn điểm càng thấp
        sigma = 1.8 + (int(group_suffix[-1]) - 3) * 0.1 # Càng C... lớn sigma càng cao
    else:
        # 2. PHÂN LOẠI THEO KHỐI (Fallback)
        if grade_level == 10:
            mu, sigma = 6.5, 1.4
        elif grade_level == 11:
            mu, sigma = 6.3, 1.5
        else: # grade_level == 12
            mu, sigma = 6.0, 1.6
            
    # Giới hạn mu để đảm bảo tính thực tế
    mu = max(5.0, min(8.5, mu))
    sigma = max(0.5, min(2.5, sigma))
    
    return (mu, sigma)
# -------------------------------------------------------------------------


def clear_students():
    Student.objects.all().delete()
    print("🗑️ Đã xóa tất cả học sinh!")

def score_to_academic_code(score):
    # Trả về mã học lực phù hợp với model (G, K, TB, Y)
    if score >= 8.0:
        return 'G'
    if score >= 6.5:
        return 'K'
    if score >= 5.0:
        return 'TB'
    return 'Y'

def unique_email(base, used):
    base_clean = base.lower().replace(' ', '')
    email = f"{base_clean}@example.com"
    if email in used:
        suffix = 1
        while f"{base_clean}{suffix}@example.com" in used:
            suffix += 1
        email = f"{base_clean}{suffix}@example.com"
    used.add(email)
    return email

n = 10000  # số học sinh cần tạo
def generate_students(n):
    used_emails = set()
    for i in range(n):
        first = random.choice(names)
        last = random.choice(names)
        if not first: first = 'HọcSinh'
        if not last: last = str(random.randint(1,999))
        name = f"{first} {last} {random.randint(1,99)}"

        age = random.randint(15, 20)
        classroom = random.choice(classrooms) # Chọn lớp ngẫu nhiên

        gender = random.choices(genders, weights=[0.48,0.48,0.04])[0]
        study_status = random.choice(statuses)

        # -----------------------------------------------------------------
        # GỌI HÀM MỚI: TẠO PHÂN BỐ ĐIỂM SỐ DỰA TRÊN TÊN LỚP ĐÃ CHỌN
        mu, sigma = get_score_params_by_classroom(classroom)
        
        # TẠO SCORE THEO PHÂN BỐ CHUẨN CỦA LỚP ĐÓ
        score = max(0.0, min(10.0, round(random.gauss(mu, sigma), 1)))
        # -----------------------------------------------------------------

        academic = score_to_academic_code(score)

        base_for_email = f"{first}{last}{random.randint(1,999)}"
        email = unique_email(base_for_email, used_emails)

        birthday = date.today() - timedelta(days=365 * age + random.randint(0, 350))
        address = random.choice(addresses)
        phone = f"09{random.randint(10000000, 99999999)}"
        application_status = random.choice(application_statuses)
        application_date = date.today() - timedelta(days=random.randint(0, 60))
        application_note = random.choice(notes)
        payment_status = random.choice(payment_statuses)
        payment_date = date.today() - timedelta(days=random.randint(0, 30))
        payment_note = random.choice(notes)
        amount_paid = round(random.uniform(0, 5000000), 0)

        Student.objects.create(
            name=name,
            age=age,
            classroom=classroom,
            gender=gender,
            study_status=study_status,
            score=score,
            academic=academic,
            email=email,
            birthday=birthday,
            address=address,
            phone=phone,
            application_status=application_status,
            application_date=application_date,
            application_note=application_note,
            payment_status=payment_status,
            payment_date=payment_date,
            payment_note=payment_note,
            amount_paid=amount_paid
        )

    print(f"✅ Đã tạo {n} học sinh thành công!")

if __name__ == '__main__':
    clear_students()
    generate_students(n)