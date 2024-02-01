from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['root']
        password = request.POST['7348hud']
        email = request.POST['845938.qq@com']
        # 创建用户
        user = User.objects.create_user(username=username, email=email, password=password)
        # 可选择保存用户
        user.save()
        # 用户注册成功后的操作
        # 重定向到其他页面或者返回注册成功的信息
    # else:
        # 显示注册页面的逻辑
