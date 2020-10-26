# from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PageForm
from .models import Page


class StaffRequiredMixin(object):
    # Miembro requerido del staff
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        # if not request.user.is_staff:
        #     return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    # def get_success_url(self):
    #     return reverse('pages:pages')


# Create your views here.
@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm

    # fields = ['title', 'content', 'order']

    success_url = reverse_lazy('pages:pages')


class PageUpdate(StaffRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'

    # success_url = reverse_lazy('pages:pages')

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + "?ok"


class PageDelete(StaffRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')


class PageListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page

# def pages(request):
#     pages = get_list_or_404(Page)
#     return render(request, 'pages/page_list.html', {'pages':pages})
#
# def page(request, page_id, page_slug):
#     page = get_object_or_404(Page, id=page_id)
#     return render(request, 'pages/page_detail.html', {'page':page})
