from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from chronosapi.views import register_user, login_user
from rest_framework import routers
from chronosapi.views import CustomerView
from chronosapi.views import FavoriteWatchView
from chronosapi.views import ReviewView
from chronosapi.views import WatchTypeView
from chronosapi.views import WatchView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customers', CustomerView, 'customer')
router.register(r'favoritewatches', FavoriteWatchView, 'favoritewatch')
router.register(r'reviews', ReviewView, 'review')
router.register(r'watchtypes', WatchTypeView, 'watchtype')
router.register(r'watches', WatchView, 'watch')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
