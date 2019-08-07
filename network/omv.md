NAS 설치후,

<br/><br/>
## 1. 네트워크 설정
1-1. 고정ip 등록하기
![스크린샷 2019-08-04 오후 9 37 47](https://user-images.githubusercontent.com/44438752/62423911-49f32580-b702-11e9-8fe9-08f8b220e481.png)

<br/><br/><br/><br/>

## 2. HDD 설정
2-1. 저장소 - 디스크 클릭,하드디스크 4개가 인식된걸 확인할 수 있음


![스크린샷 2019-08-04 오후 9 51 41](https://user-images.githubusercontent.com/44438752/62423931-8e7ec100-b702-11e9-95a6-8039568bd8e2.png)

<br/><br/>
2-2. 파티션 생성을 위해 저장소 -파일시스템 클릭. 생성 버튼을 눌러 장치와 레이블(별명), 파일시스템은 ext4로 설정, 후에 마운트 버튼 누르기

![스크린샷 2019-08-04 오후 9 52 11](https://user-images.githubusercontent.com/44438752/62423946-d0a80280-b702-11e9-99cf-14696d7a914f.png)

<br/><br/><br/><br/>

## 3. 사용자 생성

3-1. 그룹에 ssh 추가
![스크린샷 2019-08-04 오후 10 04 36](https://user-images.githubusercontent.com/44438752/62424058-7e67e100-b704-11e9-905c-5f8689216458.png)\

<br/><br/>
3-2. 위치 지정
![스크린샷 2019-08-04 오후 10 06 32](https://user-images.githubusercontent.com/44438752/62424064-8758b280-b704-11e9-9780-6bac0d394f32.png)

<br/><br/>
3-3. 상대경로도 설정(seongsil/)
![스크린샷 2019-08-04 오후 10 06 32](https://user-images.githubusercontent.com/44438752/62618884-553b9080-b950-11e9-8f3f-b536a80417f8.png)


<br/><br/>
3-4. 공유폴더 권한 설정
![스크린샷 2019-08-04 오후 10 07 11](https://user-images.githubusercontent.com/44438752/62424075-ac4d2580-b704-11e9-93fc-25784a9d572b.png)


<br/><br/><br/><br/>

## 4. ssh 설정 
4-1. 포트번호 설정 및 활성화시키기
![스크린샷 2019-08-04 오후 10 18 03](https://user-images.githubusercontent.com/44438752/62424153-c63b3800-b705-11e9-8d7b-7a1152292621.png)

<br/><br/>
4-2. 클라이언트 접속
![스크린샷 2019-08-04 오후 10 17 06](https://user-images.githubusercontent.com/44438752/62424155-d05d3680-b705-11e9-8670-f32f11cb40fe.png)

## 5. ftp 설정
5-1. ssh와 같이 포트번호 설정 및 활성화시키기
5-2. 클라이언트 접속
<>
<br/><br/><br/><br/>

## 6. Ubuntu Linux Samba 공유 폴더 Mount 하기 
6-1. smb 활성화
![스크린샷 2019-08-04 오후 10 17 06](https://user-images.githubusercontent.com/44438752/62620499-6e464080-b954-11e9-94fc-685fc349084c.png)

<br/><br/>
6-2. 공유 폴더 설정
![스크린샷 2019-08-04 오후 10 17 06](https://user-images.githubusercontent.com/44438752/62620486-6ab2b980-b954-11e9-9b6d-826fb7086e1f.png)

<br/><br/>
6-3. 클라이언트 환경에서 samba설치 안되 있을 경우, sudo apt-get install samba-common
![Screenshot from 2019-08-07 21-06-37](https://user-images.githubusercontent.com/44438752/62622674-dea39080-b959-11e9-9b51-b15adb1c591c.png)

6-4. 삼바 서버 확인
![Screenshot from 2019-08-07 21-34-08](https://user-images.githubusercontent.com/44438752/62623249-5d4cfd80-b95b-11e9-80c8-bf221986423b.png)

<br/><br/>

6-4. 클라이언트 환경에 폴더 생성
vi seongsil

<br/><br/>
![aa](https://user-images.githubusercontent.com/44438752/62623485-ec5a1580-b95b-11e9-8ee9-31c8285cbaba.png)
6-5. 마운트 하기
mount -t cifs -o user='사용자이름' //서버주소/공유폴더 마운트경로

![Screenshot from 2019-08-07 21-21-19](https://user-images.githubusercontent.com/44438752/62622679-e06d5400-b959-11e9-8a44-49dbe3c3e4c3.png)

<br/><br/>

6-6. 마운트 잘 되었는지 확인

![aa](https://user-images.githubusercontent.com/44438752/62622990-aea8bd00-b95a-11e9-8ac1-70cee0650ab5.png)


