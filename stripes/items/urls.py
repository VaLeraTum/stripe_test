from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:id>/', views.item_detail),
    path('order/<int:id>/', views.order_detail),
    path('buy/<int:id>/', views.create_checkout_session),
    path('buy_order/<int:id>', views.create_checkout_session_order),
    path('cancel/', views.cancel),
    path('success', views.success)
]
