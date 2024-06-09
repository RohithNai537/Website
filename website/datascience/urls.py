from django.urls import path
from . import views

urlpatterns = [
    path('home-ds/',views.ds_home_view,name='ds_home'),
    path('home-ds/seaborn',views.ds_seaborn_view,name='ds_seaborn'),
    path('home-ds/stats',views.ds_stats_view,name='ds_stats'),
    path('home-ds/numpy',views.ds_numpy_view,name='ds_numpy'),
    path('home-ds/seaborn/barplot',views.barplot_view,name='barplot'),
    path('home-ds/seaborn/histplot',views.histplot_view,name='histplot'),
    path('home-ds/seaborn/catplot',views.catplot_view,name='catplot'),
    path('home-ds/seaborn/pairplot',views.pairplot_view,name='pairplot'),
    path('home-ds/seaborn/boxplot',views.boxplot_view,name='boxplot'),
    path('home-ds/seaborn/lineplot',views.lineplot_view,name='lineplot'),
    path('home-ds/seaborn/scatterplot',views.scatterplot_view,name='scatterplot')

]
