from django.shortcuts import render

def design_list(request):
    return render(request, 'edenapp/design_list.html', {})
