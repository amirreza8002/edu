from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .view_mixins import OwnerCourseMixin, OwnerCourseEditMixin


class ManageCoursesListView(OwnerCourseMixin, ListView):
    template_name: str = "courses/manage/course/list.html"
    permission_required: str = "courses.view_course"


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required: str = "courses.add_course"


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    permission_required: str = "courses.change_course"


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name: str = "courses/manage/course/delete.html"
    permission_required: str = "courses.delete_course"
