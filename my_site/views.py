from django.shortcuts import render

# custom view for a 404 error page not found.
def my_custom_page_not_found_view(request,exception):

    return render(request,'404.html', status=404)