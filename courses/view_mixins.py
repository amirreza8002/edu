from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Course


class OwnerCourseMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Course
    fields: tuple[str] = (
        "subject",
        "title",
        "slug",
        "overview",
    )
    success_url = reverse_lazy("manage_course_list")

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerCourseEditMixin(OwnerCourseMixin):
    template_name = "courses/manage/course/form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
