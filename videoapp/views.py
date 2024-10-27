# videoapp/views.py

from django.shortcuts import render, redirect
from .forms import VideoForm
from .models import Video
import os
from django.conf import settings
from moviepy.editor import VideoFileClip, vfx


def result(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'videoapp/result.html', {'video': video})

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video_instance = form.save()

            # 비디오 처리
            input_path = os.path.join(settings.MEDIA_ROOT, video_instance.original_video.name)
            output_filename = f'processed_{video_instance.id}.mp4'
            output_path = os.path.join(settings.MEDIA_ROOT, 'videos/processed/', output_filename)

            # 비디오 로드
            clip = VideoFileClip(input_path)

            # 흑백 효과 적용
            gray_clip = clip.fx(vfx.blackwhite)

            # 비디오 저장 (H.264 코덱 사용)
            gray_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

            # 리소스 해제
            clip.close()
            gray_clip.close()

            # 처리된 비디오 저장
            video_instance.processed_video.name = f'videos/processed/{output_filename}'
            video_instance.save()

            return redirect('result', video_id=video_instance.id)
    else:
        form = VideoForm()
    return render(request, 'videoapp/upload.html', {'form': form})

