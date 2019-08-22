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
   
   - 도커 CE 설치

   - $ sudo apt-get update && sudo apt-get install docker-ce
   - 일반 사용자계정으로 docker 명령어를 사용하기 위해서는 아래의 명령어로 그룹을 추가

   - $ sudo usermod -aG docker $USER
   - 위의 명령어를 사용하여 일반 사용자를 docker 그룹에 추가하지 않았을 경우 일반 사용자로 docker 명령어 실행시 아래와 같은 오류가 발생 
   - Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get     http://%2Fvar%2Frun%2Fdocker.sock/v1.39/containers/json?all=1: dial unix /var/run/docker.sock: connect: permission denied
   - 따라서, 일반 사용자에서 docker 명령어 실행 시 permission denied 오류가 발생하지 않도록 사용자 그룹을 추가
   - 루트권한으로
   - $ curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \ sudo apt-key add - 
   - $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID) 
   - $ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \ sudo tee /etc/apt/sources.list.d/nvidia-docker.list 
   - $ sudo apt-get update

   - $ sudo apt-get install -y nvidia-docker2

   - 오류 발생시
   - $ sudo usermod -a -G docker $USER 
   - $ sudo service docker restart
   - $ sudo reboot
1. 이미지 설치
   - docker pull korca2002/milab2:0.0
   - 동작 확인
   - docker run --runtime=nvidia --rm -it -n milab korca2002/milab2:0.0 bash
   - docker run --runtime=nvidi -d --rm -p 8888:8888 -v /home/$USER:/home/milab -n milab korca2002/milab2:0.0
   - docker run --runtime=nvidi -d --rm -p 8888:8888 -v /home/$USER:/home/milab -n milab -e JUPYTER_ENABLE_LAB=yes korca2002/milab2:0.0




