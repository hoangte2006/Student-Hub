import os
import django
import random
from datetime import date, timedelta

# Khởi động Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Student_Hub.settings')
django.setup()

from students.models import Student  # Import model

names = ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Hương', 'Khoa', 'Lan', 'Minh', 'Ngọc', 'Phúc', 'Quân', 'Thảo', 'Trang', 'Vinh']
classrooms = ['10A1', '10A2', '11B1', '11B2', '12C1']
genders = ['Nam', 'Nữ']
statuses = ['Đang học', 'Nghỉ học']

def generate_students(n=50):
    for i in range(n):
        name = random.choice(names) + f" {random.randint(1, 99)}"
        age = random.randint(15, 18)
        classroom = random.choice(classrooms)
        gender = random.choice(genders)
        status = random.choice(statuses)
        score = round(random.uniform(4.0, 10.0), 1)
        academic = (
            'Giỏi' if score >= 8 else
            'Khá' if score >= 6.5 else
            'Trung bình' if score >= 5 else
            'Yếu'
        )
        email = f"{name.lower().replace(' ', '')}@example.com"
        birthday = date.today() - timedelta(days=365 * age)

        Student.objects.create(
            name=name,
            age=age,
            classroom=classroom,
            gender=gender,
            status=status,
            score=score,
            academic=academic,
            email=email,
            birthday=birthday
        )
    print(f"✅ Đã tạo {n} học sinh thành công!")

if __name__ == '__main__':
    generate_students()
