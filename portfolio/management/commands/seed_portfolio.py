from django.core.management.base import BaseCommand

from portfolio.models import Certification, Education, Project, SiteProfile, Skill


class Command(BaseCommand):
    help = "Load starter portfolio content if the database is empty."

    def handle(self, *args, **options):
        profile, created = SiteProfile.objects.get_or_create(
            pk=1,
            defaults={
                "full_name": "T. Vimala",
                "title": "Python Developer",
                "tagline": "Building clean, reliable web applications with Python and Django.",
                "about": (
                    "I am a B.Tech student focused on Information Technology and software "
                    "development. I enjoy working with Python and Django to build practical "
                    "web applications, and I am continuously strengthening my foundation in "
                    "data structures, algorithms, and software engineering."
                ),
                "location": "India",
                "email": "vimala@example.com",
                "github_url": "https://github.com/your-github",
                "linkedin_url": "https://www.linkedin.com/in/your-linkedin",
            },
        )
        self.stdout.write(f"Profile: {'created' if created else 'already exists'} ({profile.full_name})")

        skills = [
            ("Python", 90, "Languages", "bi-filetype-py", 1),
            ("Django", 85, "Frameworks", "bi-globe2", 2),
            ("HTML", 80, "Web", "bi-filetype-html", 3),
            ("CSS", 78, "Web", "bi-filetype-css", 4),
            ("JavaScript", 70, "Web", "bi-filetype-js", 5),
            ("Java", 65, "Languages", "bi-cup-hot", 6),
            ("SQL", 75, "Database", "bi-database", 7),
            ("Git & GitHub", 80, "Tools", "bi-git", 8),
            ("Data Structures & Algorithms", 72, "Fundamentals", "bi-diagram-3", 9),
        ]
        if not Skill.objects.exists():
            Skill.objects.bulk_create(
                [
                    Skill(
                        name=name,
                        proficiency=proficiency,
                        category=category,
                        icon=icon,
                        order=order,
                    )
                    for name, proficiency, category, icon, order in skills
                ]
            )
            self.stdout.write(f"Added {len(skills)} skills.")
        else:
            self.stdout.write("Skills already exist.")

        if not Project.objects.exists():
            Project.objects.bulk_create(
                [
                    Project(
                        title="Python Developer Portfolio",
                        description=(
                            "A responsive personal portfolio built with Django, featuring "
                            "dynamic projects, skills, education, certifications, and a "
                            "working contact form managed from Django Admin."
                        ),
                        technologies="Python, Django, HTML, CSS, JavaScript, Bootstrap",
                        github_url="https://github.com/your-github/python-portfolio",
                        live_url="",
                        featured=True,
                        order=1,
                    ),
                    Project(
                        title="Task Manager API",
                        description=(
                            "A Django REST-style task tracker for creating, updating, and "
                            "organizing daily work. Designed to practice models, forms, "
                            "authentication ideas, and clean CRUD workflows."
                        ),
                        technologies="Python, Django, SQLite, HTML, CSS",
                        github_url="https://github.com/your-github/task-manager",
                        featured=True,
                        order=2,
                    ),
                    Project(
                        title="Student Result Dashboard",
                        description=(
                            "A simple academic dashboard concept for viewing results and "
                            "summaries. Built to practice Django templates, filtering, and "
                            "clear information display."
                        ),
                        technologies="Python, Django, SQL, Bootstrap",
                        github_url="https://github.com/your-github/student-dashboard",
                        featured=False,
                        order=3,
                    ),
                ]
            )
            self.stdout.write("Added sample projects.")
        else:
            self.stdout.write("Projects already exist.")

        if not Education.objects.exists():
            Education.objects.bulk_create(
                [
                    Education(
                        degree="B.Tech",
                        institution="Your College Name",
                        field_of_study="Information Technology",
                        start_year="2022",
                        end_year="2026",
                        description=(
                            "Undergraduate coursework in programming, databases, web "
                            "technologies, and software engineering. Update the college "
                            "name and years from Django Admin."
                        ),
                        order=1,
                    ),
                    Education(
                        degree="Higher Secondary Education",
                        institution="Your School / Junior College",
                        field_of_study="Science / Computer Science",
                        start_year="2020",
                        end_year="2022",
                        description="Completed higher secondary studies with a focus on analytical and computing subjects.",
                        order=2,
                    ),
                ]
            )
            self.stdout.write("Added education entries.")
        else:
            self.stdout.write("Education already exists.")

        if not Certification.objects.exists():
            Certification.objects.bulk_create(
                [
                    Certification(
                        title="Python Programming",
                        issuer="Add issuing organization",
                        date_earned="2024",
                        description="Foundations of Python syntax, problem solving, and application development.",
                        order=1,
                    ),
                    Certification(
                        title="Web Development with Django",
                        issuer="Add issuing organization",
                        date_earned="2025",
                        description="Building database-backed websites with Django views, templates, and forms.",
                        order=2,
                    ),
                    Certification(
                        title="SQL and Databases",
                        issuer="Add issuing organization",
                        date_earned="2025",
                        description="Relational database concepts, queries, and data modeling for applications.",
                        order=3,
                    ),
                ]
            )
            self.stdout.write("Added certifications.")
        else:
            self.stdout.write("Certifications already exist.")

        self.stdout.write(self.style.SUCCESS("Starter portfolio content is ready."))
