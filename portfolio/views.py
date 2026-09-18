from django.conf import settings
from django.contrib import messages
from django.contrib.staticfiles.finders import find
from django.http import FileResponse, Http404
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods

from .forms import ContactForm
from .models import Certification, Education, Project, SiteProfile, Skill


@require_http_methods(["GET", "POST"])
def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you. Your message has been sent and I will get back to you soon.",
            )
            return redirect("/#contact")
        messages.error(request, "Please correct the errors in the form and try again.")
    else:
        form = ContactForm()

    context = {
        "form": form,
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
        "education_list": Education.objects.all(),
        "certifications": Certification.objects.all(),
    }
    return render(request, "portfolio/home.html", context)


@require_GET
def download_resume(request):
    profile = SiteProfile.get_solo()
    if profile.resume_file:
        return FileResponse(
            profile.resume_file.open("rb"),
            as_attachment=True,
            filename=profile.resume_file.name.split("/")[-1],
        )

    found = find(profile.resume_static_path)
    collected = settings.STATIC_ROOT / profile.resume_static_path
    resume_path = found or (collected if collected.exists() else None)
    if not resume_path:
        raise Http404("Resume file is not available yet. Upload one in Admin or add the static PDF.")

    return FileResponse(
        open(resume_path, "rb"),
        as_attachment=True,
        filename="T_Vimala_Resume.pdf",
    )
