from django.urls import path

from .views import create_students
from .views import delete_students
from .views import detail_students
from .views import get_students
from .views import update_students

# CRUD Create, Read< Update, Delete

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),                                # List S
    path('create/', create_students, name='create'),                    # Create S
    path('detail/<int:student_id>/', detail_students, name='detail'),   # Read S
    path('update/<int:student_id>/', update_students, name='update'),   # Update S
    path('delete/<int:student_id>/', delete_students, name='delete'),   # Delete S
]
