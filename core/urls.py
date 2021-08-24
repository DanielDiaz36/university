from core.views import group
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
    path(_('students/'), group.GroupListView.as_view(), name='students'),

]
