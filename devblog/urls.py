from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.base import TemplateView, RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()


class TextPlainView(TemplateView):
    def render_to_response(self, context, **kwargs):
        return super(TextPlainView, self).render_to_response(
            context, content_type='text/plain', **kwargs)


urlpatterns = patterns('',
    # CKEditor
    url(r'^ckeditor/', include('ckeditor.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^editor/', include(admin.site.urls)),

    url(r'', include('cinekine.metablog.urls')),

    url(r'^robots\.txt$', TextPlainView.as_view(template_name='robots.txt')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
)

handler404 = 'cinekine.metablog.views.except_404_view'

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
