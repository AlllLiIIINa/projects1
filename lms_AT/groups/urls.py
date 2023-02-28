from django.urls import path


from .views import create_groups
from .views import delete_groups
from .views import detail_groups
from .views import get_groups
from .views import update_groups

app_name = 'groups'

urlpatterns = [
    path('', get_groups, name='list'),                              # List G
    path('create/', create_groups, name='create'),                  # Create G
    path('detail/<int:group_id>/', detail_groups, name='detail'),   # Read G
    path('update/<int:group_id>/', update_groups, name='update'),   # Update G
    path('delete/<int:group_id>/', delete_groups, name='delete'),   # Delete G
