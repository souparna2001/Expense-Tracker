from django.contrib import admin
from django.urls import path
from budget import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transactions/all/',views.TransactionListView.as_view(),name="transaction-list"),
    path('transactions/add/',views.TransactionCreateView.as_view(),name="transaction-add"),
    path('transactions/<int:pk>/',views.TransactionDetailView.as_view(),name="transaction-detail"),
    path('transactions/<int:pk>/remove/',views.TransactionDeleteView.as_view(),name="transaction-delete"),
    path('transactions/<int:pk>/change/',views.TransactionUpdateView.as_view(),name="transaction-edit"),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('',views.SignInView.as_view(),name="signin"),
    path('signout',views.SignOutView.as_view(),name="signout"),   
     
]

