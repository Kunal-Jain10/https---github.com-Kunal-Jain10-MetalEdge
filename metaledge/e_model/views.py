from django.shortcuts import render

# Create your views here.
def cover(request):
    context = {}
    return render(request, 'cover.html', context)