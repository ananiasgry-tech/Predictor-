name: Build APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Setup Python
      uses: actions/setup-python@v5
      with:
        python-python: '3.10'

    - name: Install Buildozer and Dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y python3-pip build-essential git ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev
        sudo apt-get install -y libgstreamer1.0-gstreamer-plugins-base1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-codecplay gstreamer1.0-libav libgstrtspserver-1.0-dev gstreamer1.0-rtsp
        sudo apt-get install -y libsqlite3-dev sqlite3 bdb-sql libffi-dev libssl-dev
        pip3 install --user --upgrade buildozer cython virtualenv

    - name: Build APK with Buildozer
      run: |
        export PATH=$PATH:~/.local/bin
        buildozer android debug

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v4
      with:
        name: meu-apk-estavel
        path: bin/*.apk
        
