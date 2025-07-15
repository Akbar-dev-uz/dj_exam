from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EventForm
from .models import Event


@login_required(login_url='login')
def home(request):
    events = Event.objects.filter()

    search = request.GET.get('event_query')

    if search in ['Past', 'Yuqori', "O‘rta"]:
        events = Event.objects.filter(priority__icontains=search)

    elif search:
        events = Event.objects.filter(title__icontains=search)

    context = {
        "events": events,
    }
    return render(request, template_name='event/home.html', context=context)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, message=f"{event.title} Создан!")
            return redirect('home')
    else:
        messages.warning(request, message=f"Сейчас мы работаем в тестовом режиме!")
        form = EventForm()

    context = {
        "form": form
    }
    return render(request, 'event/create.html', context=context)


def update(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save()
            messages.success(request, message=f"{event.title} Успешно Изменен!")
            return redirect('home')
    else:
        form = EventForm(instance=event)
    context = {
        "form": form,
        "event": event
    }
    return render(request, 'event/update.html', context=context)


def view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    context = {
        "event": event,
    }
    return render(request, template_name='event/view.html', context=context)


def delete(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    event.delete()
    messages.success(request, 'Событие успешно удалено')
    return redirect('home')
