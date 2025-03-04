from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from surface.models import UserBlog  




def register(request):
    if request.method == 'GET':
        return render(request, 'surface/register.html')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
    
    # Kiểm tả xem password có rỗng không
    if not password:
        messages.error(request, 'Password are required.')
        return render(request, 'surface/register.html')
    
    user = UserBlog.objects.filter(username=username)
    if user.exists():
        messages.info(request, 'Username is taken.')
        return render(request, 'surface/register.html')
    else:
        user = UserBlog(username=username, email=email, phone=phone)
        user.set_password(password)
        user.save()
        messages.info(request, 'User created.')

    return redirect('surface:login')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'surface/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Username and Password are required.')
            return render(request, 'surface/login.html')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully!')
            return redirect('blogApp:home')
        else:
            messages.error(request, 'Username or Password is incorrect.')
            return render(request, 'surface/login.html')
    
    return render(request, 'surface/login.html')

def logout_action(request):

    if request.method == 'POST':
        confirm = request.POST.get('confirm')
        if confirm == 'yes':
            logout(request)
            messages.success(request, 'Logout successfully!')
            return redirect('blogApp:home')
        else:  # confirm == 'no' hoặc không chọn
            return redirect('blogApp:home')
    
    # Nếu là GET, hiển thị trang chủ
    return render(request, 'surface/logout.html')
