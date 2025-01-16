from django.urls import path
from . import views
from .views import CreatePersonalView, TablePersonalView, PersonalEditView, UserDetailView

urlpatterns = [
    #path para crear personal
    path('create_personal/', CreatePersonalView.as_view(), name='create_personal'),
    #path para mostrar la tabla del personal
    path('personal_table/', TablePersonalView.as_view(), name='table_personal'),
    #path para crear personal
    path('personal/<int:pk>/', PersonalEditView.as_view(), name='edit_personal'),
    path('personal/details_<int:pk>/', UserDetailView.as_view(), name='detail_personal'),
    
]
