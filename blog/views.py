from django.views import generic
from django.shortcuts import HttpResponse, get_object_or_404
from django.shortcuts import redirect, render
from .forms import LikeForm
from .models import Post, Comment


class PostList(generic.ListView):
    queryset = Post.objects.values('pk', 'img', 'name', 'created_date').filter(
        published=True
    )
    template_name = 'blog/index.html'


class PostDetail(generic.View):
    model = Post
    template_name = 'blog/post_detail.html'

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'], published=True)
        comments = Comment.objects.values(
            'text',
            'created_date',
            'user__username',
        ).filter(post__pk=kwargs['pk'])
        context = {
            'post': post,
            'comments': comments,
            'likes_count': post.get_total_likes()
        }
        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponse('no auth')
        text = request.POST.get('comment')
        if text is None:
            post = get_object_or_404(Post, pk=kwargs['pk'])
            post.likes.add(request.user)
        elif text != '':
            comment = Comment.objects.filter(post=Post(pk=kwargs['pk']),
                                             user=request.user)
            if comment:
                comment.update(text=text)
            else:
                Comment.objects.create(post=Post(pk=kwargs['pk']),
                                       user=request.user, text=text)

        return redirect(f'/blog/{kwargs["pk"]}/', *args, **kwargs)
