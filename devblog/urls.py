from django.conf.urls import patterns, include, url
from django.conf import settings

# robots.txt, sitemaps
from django.views.generic.base import TemplateView, RedirectView
from django.contrib.sitemaps import GenericSitemap
from cinekine.metablog.models import Post

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()


# Used for robots.txt
class TextPlainView(TemplateView):
    def render_to_response(self, context, **kwargs):
        return super(TextPlainView, self).render_to_response(
            context, content_type='text/plain', **kwargs)


# Defines the sitemap

def post_priority(post):
    priority = 0.3
    modifier = post.search_priority
    if post.status == Post.EXCLUSIVE:
        modifier += 1

    priority = priority + 0.7 * (modifier / len(Post.PRIORITY_CHOICES))
    return priority


sitemaps = {
    'blog': GenericSitemap(
        {
            'queryset': Post.query([Post.PUBLISHED, Post.EXCLUSIVE]),
            'date_field': 'post_date',
        },
        priority=post_priority
    ),
}


# URLs

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^editor/', include(admin.site.urls)),

    url(r'', include('cinekine.metablog.urls')),

    url(r'^robots\.txt$', TextPlainView.as_view(template_name='robots.txt')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)

handler404 = 'cinekine.metablog.views.except_404_view'

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
