from django.urls import path

from referrals.views import (
    OrganizationListAPIView,
    OrganizationCreateAPIView,
    OrganizationRetrieveUpdateDestroyAPIView,
    EquipmentListAPIView,
    EquipmentCreateAPIView,
    EquipmentRetrieveUpdateDestroyAPIView,
    ReferralListAPIView,
    ReferralCreateAPIView,
    ReferralRetrieveUpdateDestroyAPIView,
    IncidentListAPIView,
    IncidentCreateAPIView,
    IncidentRetrieveUpdateDestroyAPIView,
    PatientListAPIView,
    PatientCreateAPIView,
    PatientRetrieveUpdateDestroyAPIView
)

app_name = "referrals"

urlpatterns = [
    path("organizations/", OrganizationListAPIView.as_view(), name="organizations"),
    path("organizations/create/", OrganizationCreateAPIView.as_view(), name="organization_create"),
    path("organizations/<int:pk>", OrganizationRetrieveUpdateDestroyAPIView.as_view(), name="organization"),

    path("equipments/", EquipmentListAPIView.as_view(), name="equipments"),
    path("equipments/create/", EquipmentCreateAPIView.as_view(), name="equipment_create"),
    path("equipments/<int:pk>/", EquipmentRetrieveUpdateDestroyAPIView.as_view(), name="equipment"),

    path("referrals/", ReferralListAPIView.as_view(), name="referrals"),
    path("referrals/create/", ReferralCreateAPIView.as_view(), name="referral_create"),
    path("referrals/<int:pk>/", ReferralRetrieveUpdateDestroyAPIView.as_view(), name="referral"),

    path("incidents/", IncidentListAPIView.as_view(), name="incidents"),
    path("incidents/<int:patient>/", IncidentListAPIView.as_view(), name="incidents_filtered"),
    path("incidents/create/", IncidentCreateAPIView.as_view(), name="incident_create"),
    path("incidents/<int:pk>/", IncidentRetrieveUpdateDestroyAPIView.as_view(), name="incidents"),


    path("patients/", PatientListAPIView.as_view(), name="patients"),
    path("patients/<int:patient>/", PatientListAPIView.as_view(), name="patients_filtered"),
    path("patients/create/", PatientCreateAPIView.as_view(), name="patient_create"),
    path("patients/<int:pk>/", PatientRetrieveUpdateDestroyAPIView.as_view(), name="patients"),


]
