from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class SiteProfile(models.Model):
    """
    Editable site-wide profile. Keep a single row and update it from Admin.
    """

    full_name = models.CharField(max_length=120, default="T. Vimala")
    title = models.CharField(max_length=120, default="Python Developer")
    tagline = models.CharField(
        max_length=255,
        default="Building clean, reliable web applications with Python and Django.",
    )
    about = models.TextField(
        default=(
            "I am a B.Tech student with a strong interest in Information Technology, "
            "Python, Django, web development, and software engineering. I enjoy turning "
            "ideas into well-structured applications and continuously improving my skills "
            "through projects, practice, and certifications."
        )
    )
    location = models.CharField(max_length=120, blank=True, default="India")
    email = models.EmailField(default="vimala@example.com")
    github_url = models.URLField(blank=True, default="https://github.com/your-github")
    linkedin_url = models.URLField(blank=True, default="https://www.linkedin.com/in/your-linkedin")
    profile_image = models.ImageField(upload_to="profile/", blank=True, null=True)
    resume_file = models.FileField(
        upload_to="resume/",
        blank=True,
        null=True,
        help_text="Upload a PDF resume. If empty, the default static resume path is used.",
    )
    resume_static_path = models.CharField(
        max_length=255,
        default="portfolio/files/T_Vimala_Resume.pdf",
        help_text="Static file path used when no uploaded resume is set.",
    )

    class Meta:
        verbose_name = "Site profile"
        verbose_name_plural = "Site profile"

    def __str__(self):
        return self.full_name

    @classmethod
    def get_solo(cls):
        profile = cls.objects.first()
        if profile is None:
            profile = cls.objects.create()
        return profile


class Skill(models.Model):
    name = models.CharField(max_length=80)
    proficiency = models.PositiveSmallIntegerField(
        default=75,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="Skill level from 1 to 100.",
    )
    category = models.CharField(max_length=80, blank=True, default="Core")
    icon = models.CharField(
        max_length=80,
        blank=True,
        default="bi-code-slash",
        help_text="Bootstrap Icons class, for example bi-filetype-py",
    )
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    technologies = models.CharField(
        max_length=255,
        help_text="Comma-separated list, for example Django, Python, Bootstrap",
    )
    github_url = models.URLField(blank=True)
    live_url = models.URLField("Live demo URL", blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "order", "-created_at"]

    def __str__(self):
        return self.title

    def tech_list(self):
        return [item.strip() for item in self.technologies.split(",") if item.strip()]


class Education(models.Model):
    degree = models.CharField(max_length=150)
    institution = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=150, blank=True)
    start_year = models.CharField(max_length=10, blank=True)
    end_year = models.CharField(max_length=10, blank=True, default="Present")
    description = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "-end_year"]
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} — {self.institution}"


class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=150)
    date_earned = models.CharField(max_length=40, blank=True)
    credential_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]
        verbose_name = "Certification / Achievement"
        verbose_name_plural = "Certifications / Achievements"

    def __str__(self):
        return f"{self.title} — {self.issuer}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}: {self.subject}"
