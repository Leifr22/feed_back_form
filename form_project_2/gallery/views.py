from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .forms import GalleryUplads
# Create your views here.
from django.views import View
from django.http import HttpResponseRedirect
from .models import Gallery


# def storage_file(file):
#     with open(f'gallery_tmp/{file.name}.jpg','wb+') as new_file:
#         for chunk in file.chunks():
#             new_file.write(chunk)


# class GalleryView(View):
#     def get(self,request):
#         form=GalleryUplads()
#         return render(request,'gallery/load_file.html', {'form': form})
#     def post(self,request):
#         form=GalleryUplads(request.POST,request.FILES)
#         if form.is_valid():
#             # storage_file(form.cleaned_data['image'])
#             new_image=Gallery(image=form.cleaned_data['image'])
#             new_image.save()
#             return HttpResponseRedirect('load_file')
#         return render(request, 'gallery/load_file.html', {'form': form})

class GalleryView(CreateView):
    model = Gallery
    template_name = 'gallery/load_file.html'
    fields = '__all__'
    success_url = 'load_file'
class ListGallery(ListView):
    model=Gallery
    template_name ='gallery/list_file.html'
    context_object_name ='records'
