from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('video_feed/', views.video_feed, name='video_feed'),
    path('process_frame/', views.process_frame, name='process_frame'),
    path('dehaze/', views.dehaze_image_upload, name='dehaze_image'),
    path('uploadvideo/', views.upload_video, name='upload_video'),
    # path('processedvideo/', views.get_processed_video, name='get_processed_video'),
    path('location_data/', views.location_data_handler, name='location_data'),
] 
