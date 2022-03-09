from django.shortcuts import render, redirect
from django.views import generic
from .forms import EventForm
from .models import Event
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):
    template_name = 'core/index.html'
    model = Event
    paginate_by = 9

    def get_queryset(self):
        return Event.objects.order_by('attendance')

class EventView(generic.DetailView):
    model = Event
    template_name = 'core/event.html'

class EventCreateView(generic.FormView):
    model = Event
    template_name = 'core/create.html'
    form_class = EventForm
    success_url = 'event/'

class EventPreviewView(generic.CreateView):
    model = Event
    template_name = 'core/preview.html'

# class EventUpdateView(generic.UpdateView):
#     model = Event
#     template_name = 'edit.html'

# class EventDeleteView(generic.DeleteView):
#     model = Event
#     template_name = 'delete.html'
#     success_url =

def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('account')
    else:
        form = CreateUserForm()
    return render(request, 'core/signup.html', {'form':form})

@login_required()
def account(request):
    if request.method == "POST":
        update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            profile_form.save()
            messages.success(request, f'Account Updated!')
            return redirect('account')
    else:
        update_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'update_form': update_form,
        'profile_form': profile_form
    }
    return render(request, 'core/account.html', context)