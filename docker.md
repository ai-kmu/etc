# 엔비디아 도커 환경설정 

1. Nvidia-graphic-driver 설치
   
   - nouveau 설치 확인 및 제거
   - 아래 명령어 실행 후 1줄이상 출력되면 nouveau가 설치된 환경이다. Nvidia 정식 드라이버 설치를 위해선 삭제가 필요하다
   - $ lsmod | grep nouveau
   - Vim 편집기를 설치
   - $ sudo apt-get install vim
   - $ sudo vim /etc/modprobe.d/blacklist-nouveau.conf
   - 생성된 .conf 파일에 아래 두줄 입력 후 저장한다.
   - blacklist nouveau
   - options nouveau modset=0
   - 아래 명령어를 입력 후 재부팅 한다. 만약 화면 안넘어가면 Ctrl + Alt + F4 눌러서 빠져나온 뒤 다시 재부팅
   - $sudo update-initramfs -u
   - 아래 명령어를 입력하면 nouveau 제거가 완료된다.
   - $sudo service gdm stop

1. nvidia-430버전을 설치하기 위한 작업
   - $ sudo add-apt-repository ppa:graphics-drivers/ppa
   - $ sudo apt update
   - $ sudo ubuntu-drivers autoinstall
   - $ sudo reboot

