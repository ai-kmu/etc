# 엔비디아 도커 환경설정 

1. Nvidia-graphic-driver 설치
   
   - nouveau 설치 확인 및 제거
   - $ lsmod | grep nouveau
   - $ sudo apt-get install vim
   - $ sudo vim /etc/modprobe.d/blacklist-nouveau.conf
   - 생성된 .conf 파일에 아래 두줄 입력 후 저장
   - blacklist nouveau
   - options nouveau modset=0
   - 아래 명령어를 입력 후 재부팅, 만약 화면 안넘어가면 Ctrl + Alt + F4 눌러서 빠져나온 뒤 다시 재부팅
   - $sudo update-initramfs -u
   - $sudo service gdm stop

1. nvidia-driver설치
   - $ sudo add-apt-repository ppa:graphics-drivers/ppa
   - $ sudo apt update
   - $ sudo ubuntu-drivers autoinstall
   - $ sudo reboot

