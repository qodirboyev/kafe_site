from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from home_app.models import Comment


# Create your views here.


class HomeView(ListView):
    template_name = "home_app/home.html"
    model = Comment



class Add_comment(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = "home_app/add_comment.html"
    fields = ['comment', 'star']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class Update_comment(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Comment
    template_name = 'home_app/update_comment.html'
    fields = ['comment', 'star']

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user



class Delete_comment(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Comment
    template_name = "home_app/delete_comment.html"
    success_url = reverse_lazy('home')
    context_object_name = 'item'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
