from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
import json

from .models import Teacher,Student,Course
# Create your views here.
# 定义一个视图函数，
# 要返回一个  对象
def index1(request):      # 命名空间：路由
    return HttpResponse(reverse("courses:index"))

def tests(request):
    return HttpResponse('在views文件。。。')

# url传参
def index2(request, v1, v2):
    return HttpResponse(f"视图函数收到的参数:{v1}-{v2}")

def index3(request):
    name = request.GET.get("name", "")
    age = request.GET.get("age", 0)
    user = {"name":name, "age":age}
    # return HttpResponse(f"views.index视图收到：姓名;{name}，年龄：{age}")
    # 序列化
    json_data = json.dump(user)
    return HttpResponse('vvwishello', json_data, content_type="application/json")

# 通过form表单提交参数 hh
def index4(request):
    name = request.POST.get("name", "pl")
    age = request.POST.get("age", 0)
    return HttpResponse(f"views.index视图收到：姓名;{name}，年龄：{age}")

# 通过json提交参数
def index5(request):
    # 对json数据进行序列化：把json数据转为python数据类型
    # 反序列化
    req_data = json.loads(request.body)
    name = req_data["name"]
    age = req_data["age"]
    return HttpResponse(f"views.index视图收到：姓名;{name}，年龄：{age}")

def index(request):
    # 查询所有的老师,结果是一个Queryset对象，可以进行切片
    teacher = Teacher.objects.all()
    # json_data = serializers.serialize("json", teacher)
    teachers_data = ", ".join([str(t) for t in teacher.values()])  # 或者使用 teacher.values_list()
    teachers_json = json.dumps(teachers_data, indent=4, ensure_ascii=False)

    return HttpResponse(teachers_json, content_type="application/json")  # ,content_type="application/json"  "收到了吗：" + str(teacher)
