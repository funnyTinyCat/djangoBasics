from django.shortcuts import render
from django.http import  HttpResponseNotFound, Http404


posts = [
    {
        "id":1,
        "title":'Let\'s explore python',
        "content":'Python is interpreted, high level, general purpose programming language. Widely used in the fields of web development, data science and machine learning.'
    },
    {
        "id":2,
        "title":'Let\'s explore Javascript.',
        "content":'Javascript is interpreted, high level, general purpose programming language. Widely used in the fields of web development.'
    },
    {
        "id":3,
        "title":'Django the best web framework',
        "content":'Django is used by almost every big tech company like facebook, google, youtube, instagram etc,..'
    }
]

categories = [
    'Programming',
    'Food',
    'Travel'
]

# Create your views here.
def home(request):

    html = ""
    for post in posts:
        html += f'''
            <div>
                <a href="/posts/{post['id']}/">
                    <h1>{post['id']} - {post['title']}</h1>
                </a>
                <p>{post['content']}</p>
            </div>
        '''
    name = "Jeff Bezos"
    return render(request, 'posts/home.html', {"posts":posts, 'username':'oliver'})

def post(request, id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
         
        return render(request, "posts/post.html", {'post_dict':post_dict})
    else:
        raise Http404()

def google(request, id):
    url = reverse("post", args=[id])
    return HttpResponseRedirect(url)

