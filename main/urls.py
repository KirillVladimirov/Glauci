from django.urls import path
from django.views.generic import TemplateView

app_name = "main"

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "load-sources/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="load_sources",
    ),
    path(
        "sources/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="sources",
    ),
    path(
        "categories/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="categories",
    ),
    path(
        "learning-strategy/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="strategy",
    ),
    path(
        "statistics/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="statistics",
    ),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
]
