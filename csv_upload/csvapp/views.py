from django.shortcuts import render, redirect
from .forms import CSVUploadForm

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_csv')  # Redirect to avoid resubmission
    else:
        form = CSVUploadForm()
    return render(request, 'csvapp/upload_csv.html', {'form': form})
