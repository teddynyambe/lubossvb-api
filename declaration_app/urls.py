from django.urls import path
from .views import save_declaration
from .views import get_all_declarations

urlpatterns = [
    # Define other URL patterns for your app here

    # URL pattern for the register_user view
    path('declaration', save_declaration, name='save_declaration'),

    # Get all declarations
    path('declarations/', get_all_declarations, name='all_declarations'),
]
