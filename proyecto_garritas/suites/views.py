from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

# Create your views here.
from proyecto_garritas.suites.models import Suite


class SuitesDetailView(LoginRequiredMixin, DetailView):
    model = Suite
    slug_field = "name"
    slug_url_kwarg = "name"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


suites_detail_view = SuitesDetailView.as_view()
