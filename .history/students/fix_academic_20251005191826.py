import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ten_dung_cua_du_an.settings')
django.setup()

from students.models import Student

# Gọi lại save() để cập nhật học lực cho toàn bộ học sinh
for student in Student.objects.all():
    student.save()

print("✅ Đã cập nhật học lực cho toàn bộ học sinh theo điểm số.")
