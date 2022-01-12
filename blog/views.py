from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, SiteSettings


class PostList(generic.ListView):
    model = Post()
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.get()
        return context


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        site_settings = SiteSettings.objects.get()
        comments = post.comments.filter(approved=True).order_by('created_at')
        tags = post.tags.all()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'site_settings': site_settings,
                'comments': comments,
                'tags': tags,
            },
        )