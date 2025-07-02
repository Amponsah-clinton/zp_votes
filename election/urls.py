from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name='login'),
    path('vote/', views.vote_view, name='vote'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('stats/', views.stats_view, name='stats'),
    path('report/', views.vote_report_view, name='vote_report'),
    path('export-votes/', views.export_votes_csv, name='export_votes'),
    path('upload-learners/', views.upload_learners_view, name='upload_learners'),
     path('download-report/', views.generate_election_report, name='download_report'),   
    path('report_download/', views.report_page_view, name='report_page'),
    path('adminpage/', views.adminpage, name='adminpage'),
       path('download-learners-doc/', views.download_learners_doc, name='download_learners_doc'),
        path('download/learners/', views.download_learners_word, name='download_learners'),
    path('download/results/', views.download_results_summary, name='download_results'),
     path('download-staff-credentials/', views.download_staff_credentials_word, name='download_staff_credentials'),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

