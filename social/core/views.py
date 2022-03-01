
from django.shortcuts import render
from django.views import generic
from .forms import EventForm
from .models import Event

class IndexView(generic.ListView):
    template_name = 'core/index.html'

    def get_queryset(self):
        return
class EventView(generic.DetailView):
    model = Event
    template_name = 'core/event.html'

class EventCreateView(generic.CreateView):
    template_name = 'core/create.html'
    form_class = EventForm
    success_url = 'event/'

    def form_valid(self, form):

        return super().form_vaild(form)

# class EventUpdateView(generic.UpdateView):
#     model = Event
#     template_name = 'edit.html'

# class EventDeleteView(generic.DeleteView):
#     model = Event
#     template_name = 'delete.html'
#     success_url =

def create(request):
    
    return render(request, 'core/create.html', {'form' : form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm = form.cleaned_data['confirm']

    form = SignupForm()
    return render(request, 'core/signup.html', {'form' : form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # print(email,password)
    form = LoginForm()
    return render(request, 'core/login.html', {'form': form} )

def account(request):
    return render(request, 'core/account.html')


'''
def LoginForm(reguest):
    return render(request, 'core/login.html')
'''