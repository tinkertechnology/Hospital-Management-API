from .views import registrationView, CustomAuthToken, patientProfileView
from django.urls import path


app_name='patient'
urlpatterns = [
    path('registration/', registrationView.as_view(), name='api_patient_registration'),
    path('login/', CustomAuthToken.as_view(), name='api_patient_login'),
    path('profile/', patientProfileView.as_view(), name='api_patient_profile'),


]