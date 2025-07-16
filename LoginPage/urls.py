from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'admins', views.AdminViewSet)
router.register(r'adoption-requests', views.PetAdoptionRequestTableViewSet)
router.register(r'adoptions', views.PetAdoptionTableViewSet)
router.register(r'pending-pets', views.PendingPetForAdoptionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('home', views.home, name='home'),
    path('admin/', views.admin_home, name='admin_home'),  # Add this line
    path('accounts/login/', views.admin_login, name='admin_login'),  # Use the custom login view
    path('admin/home/', views.admin_homepage, name='homepage_admin'),  # Admin homepage view
    path('', views.landing, name='landing'),
    path('pets/', views.pet_list, name='pet_list'),  # URL pattern for the pet list
    path('logout_admin', views.logout_admin, name='logout_admin'),
    path('admin_signup', views.admin_signup, name='super_admin_signup'),
    path('signup', views.signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('homepage', views.homepage, name='homepage'),
    path('logout', views.logout, name='logout'),
    path('pets/<pk>/', views.pet_detail_view, name='pet_detail'),
    path('add_pet', views.add_pet, name='add_pet'),
    path('pending_pets/', views.pending_pets, name='pending_pets'),
    path('pet/<pk>/', views.pet_detail_view, name='pet_detail_view'),
    path('approve/<pk>/', views.approve_pet, name='approve_pet'),
    path('adopt/<pk>/', views.adopt_pet, name='adopt_pet'),
    path('admin_approved_pet/', views.admin_approved_pet, name='admin_approved_pet'),
    path('adoption-requests/', views.list_adoption_requests, name='adoption_requests'),
    path('adoption-requests/<int:request_id>/', views.view_adoption_request, name='view_adoption_request'),
    path('adoption-table/', views.adoption_table_view, name='adoption_table'),
    path('adoption-detail/<int:pk>/', views.adoption_detail_view, name='adoption_detail'),
    path('requests/', views.view_requests, name='view_requests'),
    path('requests/<int:request_id>/', views.view_request, name='view_request'),
    path('requests/<int:request_id>/update_status/<str:new_status>/', views.update_status, name='update_status'),
    path('adopted-history/', views.adopted_history, name='adopted_history'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('admin_approved_pet_detail/<int:pet_id>/', views.admin_approved_pet_detail, name='admin_approved_pet_detail'),
    path('admin_adoption_request/', views.admin_adoption_request, name='admin_adoption_request'),
    path('admin_view_all_requests/', views.admin_view_all_requests, name='admin_view_all_requests'),
    path('admin_view_adoption_request/<int:request_id>/', views.admin_view_adoption_request, name='admin_view_adoption_request'),
    path('admin_view_pending_requests/', views.admin_view_pending_requests, name='admin_view_pending_requests'),
    path('admin_view_review_list/', views.admin_view_review_list, name='admin_view_review_list'),
    path('admin_view_approved_list/', views.admin_view_approved_list, name='admin_view_approved_list'),
    path('admin_view_rejected_list/', views.admin_view_rejected_list, name='admin_view_rejected_list'),
    path('reportadopted_pets/', views.reportadopted_pets, name='reportadopted_pets'),
    path('OwnerReportadopted_pets/', views.OwnerReportadopted_pets, name='OwnerReportadopted_pets'),
    path('reportRequestpet_detail/<int:pet_id>/', views.reportRequestpet_detail, name='reportRequestpet_detail'),  # Detail view for a specific pet
    path('OwnerReportRequestpet_detail/<int:pet_id>/', views.OwnerReportRequestpet_detail, name='OwnerReportRequestpet_detail'),  # Detail view for a specific pet
    path('add_report/<int:pet_id>/', views.add_report, name='add_report'),
    path('report_details/<int:pet_adoption_id>/', views.report_details, name='report_details'),
    path('report/<int:id>/', views.report_detail, name='report_detail'),
    path('adoption/<int:id>/', views.AdoptionDetailView, name='admin_adoption_detail_history'),
    path('admin_report/<int:report_id>/', views.admin_report_detail, name='admin_report_detail'),
    path('post_adoption/<int:id>/edit/', views.post_adoption_edit, name='post_adoption_edit'),
    path('post_adoption/<int:id>/delete/', views.post_adoption_delete, name='post_adoption_delete'),
    path('terms/', views.terms_conditions_view, name='terms_conditions'),
    path('mark-notifications-read/', views.mark_notifications_read, name='mark_notifications_read'),
    path('pet_adoption_terms_and_conditions/', views.pet_adoption_terms_and_conditions, name='pet_adoption_terms_and_conditions'),
    path('track-pwa-install/', views.track_pwa_install, name='track_pwa_install'),
]
