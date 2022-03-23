from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views import generic
from .forms import EventForm
from .models import Event, Friend_Request
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .filters import FriendFilter

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
            return redirect('account')
    else:
        update_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    all_friend_requests = Friend_Request.objects.filter(to_user = request.user.profile)
    allusers = get_user_model().objects.all()
    current = Profile.objects.get(id= request.user.id)
    friends = current.friends.all()
    friend_filter = FriendFilter(request.GET,queryset=allusers)
    allusers = friend_filter.qs

    context = {
        'update_form': update_form,
        'profile_form': profile_form,
        'allrequests': all_friend_requests,
        "allusers": allusers,
        "friend_filter": friend_filter,
        "friends": friends

    }
    return render(request, 'core/account.html', context)

@login_required
def send_friend_request(request,userID):
    result = 'friend request already sent'
    from_user = request.user.profile
    to_user = User.objects.get(id=userID).profile
    friend_request, created = Friend_Request.objects.get_or_create(from_user=from_user,to_user=to_user)
    if created:
        result = 'friend request sent'
    context = {
        "result": result,
    }
    return render(request, 'core/friends.html', context)


@login_required
def accept_friend_request(request, requestid):
    friend_request = Friend_Request.objects.get(id=requestid)
    friend_request.to_user.user.friends.add(friend_request.from_user)
    friend_request.from_user.user.friends.add(friend_request.to_user)
    friend_request.delete()
    result = 'friend request accepted'
    context = {
        "result": result,
    }
    return render(request, 'core/friends.html', context)

@login_required
def decline_friend_request(request, requestid):
    friend_request = Friend_Request.objects.get(id=requestid)
    friend_request.delete()
    result = 'friend request declined'
    context = {
        "result": result,
    }
    return render(request, 'core/friends.html', context)
