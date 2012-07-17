"""
This code should be copy and pasted into blog/urls.py
"""


from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^logout/$', 'reg.views.do_logout'),
    url(r'^login/$', 'reg.views.do_login'), 
    url(r'^signup/$', 'reg.views.register'),
    url(r'^/?next=/$', 'reg.views.do_login'), 
    
)
