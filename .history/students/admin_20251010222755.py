@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'classroom', 'gender', 'academic', 'study_status', 'score', 'email', 'birthday', 'is_deleted']
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('name', 'age', 'classroom', 'gender', 'study_status', 'academic', 'score', 'email', 'birthday')
        }),
        ('Thông tin liên hệ', {
            'fields': ('address', 'phone')
        }),
        ('Hồ sơ', {
            'fields': ('application_date', 'application_status', 'application_note')
        }),
        ('Thanh toán', {
            'fields': ('payment_date', 'payment_status', 'payment_note', 'amount_paid')
        }),
        ('Khác', {
            'fields': ('is_deleted',)
        }),
    )
