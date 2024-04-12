from django.views import generic
from .models import Entry
from django.contrib.auth.models import User
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# class EntryListSearch(generic.ListView):
#     queryset = Entry.objects.order_by('-restype')
#     template_name = 'search_results.html'

class EntryList(generic.ListView):
    queryset = Entry.objects.order_by('-restype')
    template_name = 'library.html'

class EntryDetail(generic.DetailView):
    model = Entry
    template_name = 'entry_detail.html'

# class SearchResultsView(generic.ListView):
#     model = Entry
#     template_name = 'search_results.html'

class SearchResultsView(generic.ListView):
    model = Entry
    template_name = "search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Entry.objects.filter(
            Q(name__icontains=query)  | Q(description__icontains=query) 
        )
        return object_list

# @login_required
def entry_detail(request, slug):
    template_name = 'entry_detail.html'
    entry = get_object_or_404(Entry, slug=slug)
    comments = entry.comments.filter(active=True)
    new_comment = None
    # user = User.get_username(User)
    # user_email = User.objects.get()
    # Comment posted
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.entry = entry
            new_comment.name = request.user
            new_comment.email = request.user.email
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'entry': entry,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

