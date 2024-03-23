from django.contrib import admin

from courses.models import Subject, Course, Module


@admin.register(Subject)
class CourseAdmin(admin.ModelAdmin):
    list_display: tuple = (
        "title",
        "slug",
    )
    prepopulated_fields: dict = {"slug": ("title",)}


class ModuleInline(admin.TabularInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display: tuple = (
        "title",
        "subject",
        "created",
    )
    list_filter: tuple = (
        "subject",
        "created",
    )
    search_fields: tuple = (
        "title",
        "overview",
    )
    prepopulated_fields: dict = {"slug": ("title",)}
    inlines: tuple = (ModuleInline,)
