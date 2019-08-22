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

1. Nvidia-docker version2 설치
   - 먼저 오래된 버전의 도커가 설치되어 있다면, 아래의 명령어를 사용해서 삭제
   - $ sudo apt-get remove docker docker-engine docker.io

   - 그리고 아래의 명령어를 사용하여 설치에 필요한 패키지들을 설치
   - $ sudo apt-get update && sudo apt-get install \ apt-transport-https \ ca-certificates \ curl \ software-properties-common

   - 패키지 저장소 추가
   - 아래의 명령어를 사용하여 도커의 공식 GPG 키와 저장소를 추가해 주시기 바랍니다.

   - $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add – 

   - $ sudo add-apt-repository \ "deb [arch=amd64] https://download.docker.com/linux/ubuntu \ $(lsb_release -cs) \ stable"

   - 그리고 아래의 명령어를 사용하여 docker 패키지가 검색되는지 확인
   - $ sudo apt-get update && sudo apt-cache search docker-ce

   - 만약 현재 우분투 버전에서 설치 패키지가 검색된다면 아래와 같은 내용이 출력
   - docker-ce - Docker: the open-source application container engine



