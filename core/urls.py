from core.views import group, student
from django.urls import path
from django.utils.translation import gettext_lazy as _


urlpatterns = [

    #   Groups
    path(_('groups/'), group.GroupListView.as_view(), name='groups'),

    path(_('groups/add/'), group.GroupAddView.as_view(), name='add_group'),

    path(_('groups/edit/<int:pk>/'), group.GroupEditView.as_view(), name='edit_group'),

    path(_('groups/delete/<int:pk>/'), group.GroupDeleteView.as_view(), name='delete_group'),

    path(_('groups/details/'), group.GroupDetailsAjaxView.as_view(), name='details_group'),


    #   Students
    path(_('students/'), student.StudentListView.as_view(), name='students'),

    path(_('students/add/'), student.StudentAddView.as_view(), name='add_student'),

    path(_('students/edit/<int:pk>/'), student.StudentEditView.as_view(), name='edit_student'),

    path(_('students/delete/<int:pk>/'), student.StudentDeleteView.as_view(), name='delete_student'),

    path(_('students/enable/<int:pk>/'), student.StudentEnableView.as_view(), name='enable_student'),

    path(_('students/disable/<int:pk>/'), student.StudentDisableView.as_view(), name='disable_student'),

    path(_('students/details/'), student.StudentDetailsAjaxView.as_view(), name='details_student'),

]
