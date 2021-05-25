from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import request
from .models import Show
from datetime import datetime, date



def shows(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, "shows.html", context)

def add_show(request):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')

        Show.objects.create(
            title = request.POST["title"],
            network = request.POST["network"],
            description = request.POST["description"],
            release_date = datetime.strptime(request.POST["release_date"], "%m/%d/%Y")
        )        
        return redirect('/')
    else:
        return render(request, "add-show.html")

def edit_show(request, show_id):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{show_id}/edit')

        show_to_edit = Show.objects.get(id=show_id)
        # UPDATE
        show_to_edit.title = request.POST["title"]
        show_to_edit.network = request.POST["network"]
        show_to_edit.description = request.POST["description"]
        show_to_edit.release_date = datetime.strptime(request.POST["release_date"], "%m/%d/%Y")
        show_to_edit.updated_at = date.today()
        show_to_edit.save()
        return redirect(f'/shows/{show_id}')
    else:
        context = {
            "edit_show_info": Show.objects.get(id=show_id)
        }
        return render(request, "edit-show.html", context)

def show_info(request, show_id):
    context = {
        "show_info": Show.objects.get(id=show_id)
    }
    return render(request, "show-info.html", context)

def delete_show(request, show_id):
    show_to_delete = Show.objects.get(id=show_id)
    show_to_delete.delete()

    return redirect('/')