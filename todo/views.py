from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


@login_required
def task_list(request):

    if request.method == "POST":
        title = request.POST.get("title")

        if title:
            Task.objects.create(
                title=title,
                user=request.user
            )

        return redirect("task_list")

    tasks = Task.objects.filter(
        user=request.user
    )

    return render(
        request,
        "todo/task_list.html",
        {"tasks": tasks}
    )


@login_required
def delete_task(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    task.delete()

    return redirect("task_list")


@login_required
def toggle_task(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    task.completed = not task.completed

    task.save()

    return redirect("task_list")