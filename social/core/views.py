from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import AccessMixin
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import EventForm, AttendeeForm
from .models import Event, Friend_Request
from .forms import *
from django.contrib.auth.decorators import login_required
from .filters import FriendFilter
from django.urls import reverse

class IndexView(ListView):
    template_name = 'core/index.html'
    model = Event
    paginate_by = 9

    def get_queryset(self):
        if 'search' and 'sort' in self.request.GET:
            query = self.request.GET.get('search')
            sort_by = self.request.GET.get('sort')
            if query[0:2] == '%23':
                object_list = Event.objects.filter(title__icontains=(query)).order_by(sort_by)
            else:
                object_list = Event.objects.filter(tags__icontains=(query)).order_by(sort_by)

        elif 'search' in self.request.GET:
            query = self.request.GET.get('search')
            object_list = Event.objects.filter(title__icontains=(query))
            if query[0:2] == '%23':
                object_list = Event.objects.filter(title__icontains=(query))
            else:
                object_list = Event.objects.filter(tags__icontains=(query))

        elif 'sort' in self.request.GET:
            sort_by = self.request.GET.get('sort')
            object_list = Event.objects.order_by(sort_by)

        else:
            object_list = Event.objects.order_by('-attendance')
        
        for object in object_list:
            object.tags = object.tags.split()
            
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['slideshow_event_list'] = Event.objects.order_by('-attendance')[:5]
        return context

class EventView(DetailView, FormMixin, AccessMixin):
    model = Event
    template_name = 'core/event.html'
    form_class = AttendeeForm

    def get_success_url(self):
        return reverse('event', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        elif form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        event = self.get_object()
        if "interested" in self.request.POST:
            print("Interested")
            form.instance.event = event
            form.instance.user = self.request.user
            event.attendance += 1
            form.save()
            event.save()
        elif "not-interested" in self.request.POST:
            print("Not Interested")
            Attendee.objects.filter(event=self.get_object(), user=self.request.user).delete()
            event.attendance -= 1
            event.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if Attendee.objects.filter(event=self.get_object(), user=self.request.user):    
                context["attending"] = True
            else:
                context["attending"] = False
        self.object.tags = self.object.tags.split()
        return context
    


class EventCreateView(CreateView, AccessMixin):
    model = Event
    template_name = 'core/create.html'
    form_class = EventForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if not self.request.user.groups.filter(name="Organiser").exists():
            # Redirect the user to somewhere else - add your URL here
            raise Http404("You are no authorised to create events!")
        
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EventEditView(UpdateView, AccessMixin):
    model = Event
    template_name = 'core/create.html'
    form_class = EventForm

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user == self.get_object().user:
            raise Http404("You are not allowed to edit this event!")
        
        return super().dispatch(request, *args, **kwargs)
        

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
    current = Profile.objects.get(id=request.user.id)
    friends = current.friends.all()
    friend_filter = FriendFilter(request.GET,queryset=allusers)
    allusers = friend_filter.qs
    userEvents = Event.objects.filter(event__in=Attendee.objects.filter(user=request.user))
    friendEvents = []
    for friend in friends:
        friendEvents += Event.objects.filter(event__in=Attendee.objects.filter(user=friend))

    print(friendEvents)
    for event in userEvents:
            event.tags = event.tags.split()

    for event in friendEvents:
            event.tags = event.tags.split()

    context = {
        'update_form': update_form,
        'profile_form': profile_form,
        'allrequests': all_friend_requests,
        "allusers": allusers,
        "friend_filter": friend_filter,
        "friends": friends,
        "userEvents": userEvents,
        "friendEvents" : friendEvents
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
