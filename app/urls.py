from django.urls import path, include
from website.views.home import HomeView
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [

    path('', HomeView.as_view(), name='home'),

    path('i18n/', include('django.conf.urls.i18n')),

]

urlpatterns += i18n_patterns(

    path('captcha/', include('captcha.urls')),

    path('', include('website.urls')),

    path('', include('core.urls')),

)
