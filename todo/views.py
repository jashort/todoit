from django.views import generic
from .models import Todo
from .forms import TodoForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class DetailView(generic.edit.FormView):
    form_class = TodoForm
    success_url = reverse_lazy('todo:list')
    template_name = 'todo/detail.html'

    def form_valid(self, form):
        return super(DetailView, self).form_valid(form)

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoCreate(CreateView):
    model = Todo
    success_url = reverse_lazy('todo:list')


class TodoUpdate(UpdateView):
    model = Todo
    success_url = reverse_lazy('todo:list')

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:list')

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
