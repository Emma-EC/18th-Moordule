from django.shortcuts import render, redirect, get_object_or_404
from .forms import ActivityForm, CategoryForm
from .models import Activity, Category
from django.db.models import Q


def activities(request):
    index = Activity.objects.all()
    return render(request, "activities/index.html", {"activities": index})


def create(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("activities:index")
        else:
            return render(
                request,
                "activities/create.html",
                {"form": form, "categories": categories},
            )
    else:
        form = ActivityForm()
    return render(
        request,
        "activities/create.html",
        {
            "form": form,
            "categories": categories,
        },
    )


def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("activities:category")
    else:
        form = CategoryForm()

    categories = Category.objects.all()
    return render(
        request,
        "activities/create_category.html",
        {"form": form, "categories": categories},
    )


def update(request, activity_id):
    categories = Category.objects.all()
    activity = get_object_or_404(Activity, id=activity_id)

    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect("activities:index")
        else:
            # 在這裡打印表單錯誤
            print(form.errors)  # 用於調試，查看具體錯誤
            return render(
                request,
                "activities/update.html",
                {
                    "form": form,
                    "activity": activity,
                    "categories": categories,
                    "error_message": "更新失敗，請檢查表單資料。",
                },
            )
    else:
        form = ActivityForm(instance=activity)
    return render(
        request,
        "activities/update.html",
        {
            "form": form,
            "activity": activity,
            "categories": categories,
        },
    )


def delete(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)

    activity.delete()

    return redirect("activities:index")


def confirm_delete(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    if request.method == "POST":
        activity.delete()
        return redirect("activities:index")
    return render(request, "activities/confirm_delete.html", {"activity": activity})

def search(request):
<<<<<<< HEAD
    return render(request,"activities/search.html")

def information(request):
    return render(request,"activities/information.html")
=======
    activities = Activity.objects.all()

    if request.method == "POST":  # 確保處理 POST 請求
        keyword = request.POST.get("keyword", "").strip()  # 去除多餘的空白
        if keyword:
            # 使用 Q 查詢條件比對所有欄位
            activities = activities.filter(
                Q(title__icontains=keyword)
                | Q(description__icontains=keyword)
                | Q(address__icontains=keyword)
            )
        return render(
            request,
            "activities/search.html",
            {"activities": activities, "keyword": keyword},
        )
    return render(request, "activities/search.html", {"activities": activities})
>>>>>>> cf5b71b ( feat:search bar)
