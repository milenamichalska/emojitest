from django.urls import include, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
    path('emojis/', views.SearchEmojiAPIView.as_view()),
    path('meals/', views.MealsAPIView.as_view()),
    path('mealtimes/', views.MealTimesAPIView.as_view()),
    path('test-entries/', views.TestEntryAPIView.as_view())
]
