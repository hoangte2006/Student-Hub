import os
import django
import random
from datetime import date, timedelta

# Khởi động Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_manager.settings')  # Đổi lại nếu dự án tên khác
django.setup()

from students.models import Student

names = ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Hương', 'Khoa', 'Lan', 
         'Minh', 'Ngọc', 'Phúc', 'Quân', 'Thảo', 'Trang', 'Vinh', 'Yến', 
         'Tuấn', 'Hải', 'Linh', 'Mai', 'Nam', 'Oanh', 'Phương', 'Quỳnh', 
         'Sơn', 'Tú', 'Vy', 'Xuân', 'Yến', 'Đức', 'Hạnh', 'Khánh', 'Lộc'
         , 'Mỹ', 'Nhi', 'Phát', 'Quang', 'Thành', 'Trâm', 'Vân', 'Đăng'
         , 'Huy', 'Kiên', 'Linh', 'Phú', 'Quý', 'Thảo', 'Trung', 'Vũ']

classrooms = ['10A1', '10A2', '11B1', '11B2', '12C1', '12C2', '12C3', '12C4', '12C5', '12C6', '12C7', '12C8']
genders = ['M', 'F', 'O']
gender = random.choice(genders)
statuses = ['Đang học', 'Nghỉ học', 'Đã tốt nghiệp']
academics = ['G', 'K', 'TB', 'Y']
application_statuses = ['Chưa nộp', 'Đã nộp', 'Đang xét']
payment_statuses = ['Chưa thanh toán', 'Đã thanh toán', 'Đang xử lý']
addresses = ['TP.HCM', 'Hà Nội', 'Đà Nẵng', 'Cần Thơ', 'Huế', 'Nha Trang']
notes = ['Không có ghi chú', 'Đã gọi điện xác nhận', 'Cần bổ sung hồ sơ', 'Đã thanh toán một phần']

def generate_students(n=500):
    for i in range(n):
        name = random.choice(names) + f" {random.randint(1, 99)}"
        age = random.randint(15, 30)
        classroom = random.choice(classrooms)
        gender = random.choice(genders)
        study_status = random.choice(statuses)
        score = round(random.uniform(1.0, 10.0), 1)
        academic = (
            'Giỏi' if score >= 8 else
            'Khá' if score >= 6.5 else
            'Trung bình' if score >= 5 else
            'Yếu'
        )
        email = f"{name.lower().replace(' ', '')}@example.com"
        birthday = date.today() - timedelta(days=365 * age)
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
    generate_students()
