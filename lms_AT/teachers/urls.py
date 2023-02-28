from django.urls import path


from .views import create_teachers
from .views import delete_teachers
from .views import detail_teachers
from .views import get_teachers
from .views import update_teachers

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),                                # List T
    path('create/', create_teachers, name='create'),                    # Create T
    path('detail/<int:teacher_id>/', detail_teachers, name='detail'),   # Read T
    path('update/<int:teacher_id>/', update_teachers, name='update'),   # Update T
    path('delete/<int:teacher_id>/', delete_teachers, name='delete'),   # Delete T
]
