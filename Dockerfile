# 베이스 이미지 선택 (Python 3.12 버전 사용)
FROM python:3.12

# 작업 디렉토리 생성
WORKDIR /app

# 시스템 패키지 업데이트 및 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    gcc \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# 필요한 파이썬 패키지 복사
COPY requirements.txt /app/

# 파이썬 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . /app/

# 포트 공개
EXPOSE 8000

# 명령어 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

