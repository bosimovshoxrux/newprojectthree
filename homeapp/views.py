from django.views.generic import TemplateView


# Create your views here.
class HomeappViews(TemplateView):
    template_name = 'base.html'


class MaruzalarViews(TemplateView):
    template_name = 'Maruzalar.html'


class OyatlarViews(TemplateView):
    template_name = 'Oyatlar.html'


class XadislarViews(TemplateView):
    template_name = 'Xadislar.html'
