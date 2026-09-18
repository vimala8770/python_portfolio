from django.db.utils import OperationalError, ProgrammingError

from .models import SiteProfile


def site_profile(request):
    try:
        return {"site_profile": SiteProfile.get_solo()}
    except (OperationalError, ProgrammingError):
        return {"site_profile": SiteProfile()}
