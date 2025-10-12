import os
import django
import random
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_manager.settings')
django.setup()

from students.models import Student

names = [
  'An','Bình','Chi','Dũng','Hà','Hương','Khoa','Lan','Minh','Ngọc','Phúc','Quân',
  'Thảo','Trang','Vinh','Yến','Tuấn','Hải','Linh','Mai','Nam','Oanh','Phương',
  'Quỳnh','Sơn','Tú','Vy','Xuân','Đức','Hạnh','Khánh','Lộc','Mỹ','Nhi','Phát',
  'Quang','Thành','Trâm','Vân','Đăng','Huy','Kiên','Phú','Quý','Trung','Vũ',
  'Hoàng','Cường','Duy','Giang','Hùng','Khôi','Lâm','Phước','Quí','Thái','Trúc',
  'Vương','Đạt','Đan','Hân','Kha'
]

classrooms = ['10A1','10A2','11B1','11B2','12C1','12C2','12C3','12C4','12C5','12C6','12C7','12C8']
genders = ['M','F','O']  # nếu model dùng 'M'/'F'/'O'
statuses = ['A','N','S']
application_statuses = ['pending','approved','rejected']
payment_statuses = ['paid','unpaid','partial']
addresses = ['TP.HCM','Hà Nội','Đà Nẵng','Cần Thơ','Huế','Nha Trang','Vũng Tàu','Phan Thiết','Biên Hòa','Bình Dương']
notes = ['Không có ghi chú','Đã gọi điện xác nhận','Cần bổ sung hồ sơ','Đã thanh toán một phần']

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
        # thêm suffix nếu trùng
        suffix = 1
        while f"{base_clean}{suffix}@example.com" in used:
            suffix += 1
        email = f"{base_clean}{suffix}@example.com"
    used.add(email)
    return email

n = 300  # số học sinh cần tạo
def generate_students(n):
    used_emails = set()
    for i in range(n):
        first = random.choice(names)
        last = random.choice(names)
        # tránh tên hoàn toàn rỗng hoặc lặp trùng quá nhiều
        if not first: first = 'HọcSinh'
        if not last: last = str(random.randint(1,999))
        name = f"{first} {last} {random.randint(1,99)}"

        age = random.randint(15, 20)  # giới hạn tuổi hợp lý cho HS
        # cân bằng phân bố lớp: dùng random.choice, hoặc force round-robin
        classroom = random.choice(classrooms)

        gender = random.choices(genders, weights=[0.48,0.48,0.04])[0]  # nhẹ cân bằng
        study_status = random.choice(statuses)

        # tạo score có phân bố hợp lý (normal distribution approx)
        score = max(0.0, min(10.0, round(random.gauss(6.5, 1.5), 1)))

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
