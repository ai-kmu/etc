# 엔비디아 도커 환경설정 

1. Nvidia-graphic-driver 설치
   
   1. nouveau 설치 확인 및 제거
   1. 아래 명령어 실행 후 1줄이상 출력되면 nouveau가 설치된 환경이다. Nvidia 정식 드라이버 설치를 위해선 삭제가 필요하다
   1. $ lsmod | grep nouveau
   1. Vim 편집기를 설치
   1. $ sudo apt-get install vim
   1. $ sudo vim /etc/modprobe.d/blacklist-nouveau.conf
   1. 생성된 .conf 파일에 아래 두줄 입력 후 저장한다.
   1. blacklist nouveau
   1. options nouveau modset=0
   1. 아래 명령어를 입력 후 재부팅 한다. 만약 화면 안넘어가면 Ctrl + Alt + F4 눌러서 빠져나온 뒤 다시 재부팅
   1. $sudo update-initramfs -u
   1. 아래 명령어를 입력하면 nouveau 제거가 완료된다.
   1. $sudo service gdm stop

1. nvidia-430버전을 설치하기 위한 작업
   1. $ sudo add-apt-repository ppa:graphics-drivers/ppa
   1. $ sudo apt update
   1. $ sudo ubuntu-drivers autoinstall
   1. $ sudo reboot

