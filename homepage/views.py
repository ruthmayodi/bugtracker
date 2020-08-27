from django.shortcuts import render, HttpResponseRedirect, reverse 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from custom_user.models import MyUser
from homepage.models import Bugs
from homepage.forms import AddTicket, LoginForm


@login_required
def index_view(request):
    new_tickets = Bugs.objects.filter(status=Bugs.Status.NEW)
    in_progress_tickets = Bugs.objects.filter(status=Bugs.Status.IN_PROGRESS)
    done_tickets = Bugs.objects.filter(status=Bugs.Status.DONE)
    invalid_tickets = Bugs.objects.filter(status=Bugs.Status.INVALID)
    return render(
        request, 
        'home.html',
        {
            'title': 'Bug Tracker',
            'new_tickets': new_tickets,
            'in_progress_tickets': in_progress_tickets,
            'done_tickets': done_tickets,
            'invalid_tickets': invalid_tickets
        }
    )

@login_required
def ticket_view(request, ticket_id):
    data = Bugs.object.filter(id=ticket_id).first()
    return render(request, 'ticket_view.html', {'data': data})

@login_required
def user_view(request, user_id):
    new_tickets = Bugs.objects.filter(status=Bugs.Status.NEW, id=user_id)
    in_progress_tickets = Bugs.objects.filter(status=Bugs.Status.IN_PROGRESS, id=user_id)
    done_tickets = Bugs.objects.filter(status=Bugs.Status.DONE, id=user_id)
    invalid_tickets = Bugs.objects.filter(status=Bugs.Status.INVALID, id=user_id)
    user_info = MyUser.objects.filter(id=user_id).first()
    return render(
        request, 
        'user_view.html',
        {
            'title': 'Bug Tracker',
            'new_tickets': new_tickets,
            'in_progress_tickets': in_progress_tickets,
            'done_tickets': done_tickets,
            'invalid_tickets': invalid_tickets,
            'user_info': user_info
        }
    )


@login_required
def add_ticket_view(request):
    if request.method == 'POST':
        form = AddTicket(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Bugs.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                filed_by=request.user
            )
            return HttpResponseRedirect(reverse('home'))
    form = AddTicket()
    return render(request, 'generic_form.html', {'form': form})






