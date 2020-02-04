from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from file.forms import UploadFileForm


class FileUploadView(LoginRequiredMixin, View):

    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.uploaded_by = request.user
            upload.save()
        return redirect('index')

    def get(self, request):
        return render(request, 'upload.html', {'form': UploadFileForm()})
