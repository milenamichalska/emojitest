from django.urls import include, path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('emojis/', views.SearchEmojiAPIView.as_view()),
    path('meals/', views.MealsAPIView.as_view()),
    path('mealtimes/', views.MealTimesAPIView.as_view()),
    path('test-entries/', views.TestEntryAPIView.as_view())
]
