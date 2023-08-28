from django.shortcuts import render, redirect
from .forms import AudioFileForm
from .models import AudioFile

def index(request):
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            audio_file = form.save(commit=False)
            audio_file.file_size = request.FILES['file'].size
            audio_file.file_extension = request.FILES['file'].name.split('.')[-1]
            audio_file.save()
            return redirect('index')
    else:
        form = AudioFileForm()

    audio_files = AudioFile.objects.all()

    return render(request, 'AudioApp/index.html', {'form': form, 'audio_files': audio_files})