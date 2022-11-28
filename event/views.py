from django.shortcuts import render, redirect, get_object_or_404
from slugify import slugify

from .forms import *

# Create your views here.

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Добавить событие', 'url_name': 'addevent'},
    {'title': 'Всё мероприятия', 'url_name': 'allevent'},
]


def home(request):
    return render(request, 'base.html', {'menu': menu,
                                         'title': 'Главная',
                                         }
                  )


def add_event(request):
    if request.POST:
        form = AddEvent(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.slug = slugify(form.name)
            form.save()
            return redirect('home')
    else:
        form = AddEvent()
        form2 = SimpleForm()
        return render(request, 'addevent.html', {'menu': menu,
                                                 'title': 'Добавить мероприятие',
                                                 'form': form,
                                                 'equipment': form2
                                                 }
                      )


def all_events(request):
    event = Events.objects.all()
    return render(request, 'allevent.html', {'menu': menu,
                                             'title': 'Добавить мероприятие',
                                             'event': event
                                             }
                  )


def event_page(request, event_slug):
    event = get_object_or_404(Events, slug=event_slug)
    return render(request, 'eventpage.html', {'menu': menu,
                                              'title': f'Мероприятие {event.name}',
                                              'event': event,
                                              }
                  )
