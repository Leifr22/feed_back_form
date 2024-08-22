from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView
from .forms import FeedbackForm
from .models import Feedback
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
class FeedBackViewUpdate(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'

class FeedBackView(CreateView):
    model=Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'
    # def form_valid(self, form):
    #     form.save()
    #     return super(FeedBackView,self).form_valid(form)

# class FeedBackView(View):
#     def get(self,request):
#         form=FeedbackForm()
#         return render(request, 'feedback/feedback.html', context={'form': form})
#     def post(self,request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/done')
#         return render(request, 'feedback/feedback.html', context={'form': form})
class UpdateFeedbackView(View):
    def get(self, request, id_feedback):
        feed = get_object_or_404(Feedback, id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request, id_feedback):
        feed = get_object_or_404(Feedback, id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
        else:
            form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})
class DoneView(TemplateView):
     template_name = 'feedback/done.html'

# class ListFeedBack(TemplateView):
#     template_name = 'feedback/list_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context['all_feed'] = Feedback.objects.all()
#         return context
class ListFeedBack(ListView):
    template_name = 'feedback/list_feedback.html'
    model=Feedback
    paginate_by=2
    def get_queryset(self):
        queryset=super().get_queryset()
        # filter=queryset.filter(rating__gt=2)
        return queryset
class DetailFeedBack(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback

    # def get_context_data(self,**kwargs):
    #     context=super().get_context_data(**kwargs)
    #     id_feedback=kwargs['id_feedback']
    #     feedback=Feedback.objects.get(id=id_feedback)
    #     context['info']=feedback
    #     return context

