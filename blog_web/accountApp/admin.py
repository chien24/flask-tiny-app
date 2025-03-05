# account/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserBlog

class UserBlogAdmin(UserAdmin):
    # Các trường hiển thị trong danh sách
    list_display = ('username', 'email', 'phone', 'is_active', 'is_staff', 'date_joined')
    # Các trường có thể lọc
    list_filter = ('is_active', 'is_staff')
    # Các trường có thể tìm kiếm
    search_fields = ('username', 'email', 'phone')
    # Sắp xếp mặc định
    ordering = ('username',)

    # Tùy chỉnh form chỉnh sửa
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'phone', 'bio')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'password1', 'password2'),
        }),
    )

# Đăng ký model với admin
admin.site.register(UserBlog, UserBlogAdmin)