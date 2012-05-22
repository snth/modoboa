from django.conf.urls.defaults import *
from django.conf import settings
from modoboa.extensions import *
from modoboa.lib import parameters

prefix = settings.MODOBOA_WEBPATH
if prefix != "":
    if prefix.startswith("/"):
        prefix = prefix[1:]
    if not prefix.endswith("/"):
        prefix += "/"

urlpatterns = patterns('',
    (r'^%s$' % prefix, 'modoboa.lib.webutils.topredirection'),
    (r'^%sadmin/' % prefix, include('modoboa.admin.urls')),
    (r'^%suserprefs/' % prefix, include('modoboa.userprefs.urls')),
    (r'^%sdemo/' % prefix, include('modoboa.demo.urls')),
    (r'^%stemplot/' % prefix, include('templot.frontends.modoboa.urls')),
    (r'^accounts/login/$', 'modoboa.auth.views.dologin'),
    (r'^accounts/logout/$', 'modoboa.auth.views.dologout'),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', 
     {'packages': ('modoboa',),}),
    *exts_pool.load_all(prefix)
)

if settings.DEBUG:
    urlpatterns += patterns(
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes' : True}),
        url(r'', include('django.contrib.staticfiles.urls')),
        )


