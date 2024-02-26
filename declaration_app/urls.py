from django.urls import path
from .views import save_declaration
from .views import get_all_declarations
from .views import get_all_declarations_made

urlpatterns = [
    # Define other URL patterns for your app here

    # URL pattern for the register_user view
    path('declaration', save_declaration, name='save_declaration'),

    # Get all declarations by member
    path('declarations', get_all_declarations, name='all_declarations'),

    # Get all declarations by all
    path('declarations/all', get_all_declarations_made, name='all_declarations'),
]
