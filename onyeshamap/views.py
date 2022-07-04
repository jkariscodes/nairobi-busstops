from django.views.generic import TemplateView


class WebMapView(TemplateView):
    """
    View for the web map.
    """
    template_name = 'webmap.html'
