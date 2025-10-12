import os
import django
import random
from datetime import date, timedelta
from students.models import Student  

# Khởi động Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Student_Hub.settings') # Thay 'Student_Hub' bằng tên dự án của bạn nếu khác 
django.setup() # Khởi động Django, giups sử dụng các mô hình và chức năng của Django 

# Tạo dữ liệu mẫu cho mô hình Student 
names = ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Hương', 'Khoa', 'Lan', 'Minh', 'Ngọc', 'Phúc', 'Quân', 'Thảo', 'Trang', 'Vinh', 'Yến', 'Tuấn', 'Hải', 'Linh', 'Mai', 'Nam', 'Oanh', 'Phương', 'Quỳnh', 'Sơn', 'Tú', 'Vy']
classrooms = ['10A1', '10A2', '11B1', '11B2', '12C1', '12C2', '12C3', '12C4', '12C5', '12C6', '12C7', '12C8', '12C9', '12C10']
genders = ['Nam', 'Nữ']
statuses = ['Đang học', 'Nghỉ học']

def generate_students(n=50): # Hàm tạo n học sinh mẫu, mặc định là 50 
    for i in range(n):
        name = random.choice(names) + f" {random.randint(1, 99)}"
        age = random.randint(15, 30) # Độ tuổi từ 15 đến 30
        classroom = random.choice(classrooms) # Lớp học ngẫu nhiên
        gender = random.choice(genders)
        status = random.choice(statuses)
        score = round(random.uniform(1.0, 10.0), 1) # Điểm số từ 1.0 đến 10.0
        academic = (
            'Giỏi' if score >= 8 else
            'Khá' if score >= 6.5 else
            'Trung bình' if score >= 5 else
            'Yếu'
        )
        email = f"{name.lower().replace(' ', '')}@example.com" # Tạo email giả định dựa trên tên và số ngẫu nhiên 
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
