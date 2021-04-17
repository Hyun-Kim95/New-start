# Git

## 1. git status

> 저장소의 상태를 확인
>
> 현재 브랜치의 이름과 추가, 변경된 파일 및 디렉토리 목록을 표시

## 2. git add

> git add [file_pattern]
>
> 파일이나 디랙토리를 인덱스에 추가하는 데 사용
>
> 추가할 때 [file_pattern]에 이름을 직접 입력하거나 "*.txt" 처럼 와일드 카드도 사용 가능

## 3. git commit

>git commit -m "A first commit"
>
>인덱스에 추가된 파일이나 폴더의 내용의 커밋 작성

## 4. git branch

> 브랜치에 대한 작업 수행
>
> git branch [branch-name]: 브랜치 만들기
>
> git branch: 브랜치 목록보기
>
> git branch -d [branch-name]: 지정한 브랜치를 삭제

## 5. git checkout

> 로컬 저장소의 브랜치를 전환
>
> git checkout [branch-name]

## 6. git log

> 로컬 저장소의 커밋 히스토리를 탐색
>
> -n옵션: 내역보기의 수를 지정
>
> git log -n 10

## 7. git grep

> 저장소의 파일 내용에서 검색
>
> git grep "검색 단어"

## 8. git clone

> 기존 원격 저장소를 포컬에 다운로드
>
> git clon [url]

## 9. git remote

> 원격 저장소를 조작
>
> git remote: 원격 저장소의 이름 목록을 표시
>
> git remote -v: 원격 저장소에 대한 자세한 목록보기
>
> git remote add [name] [url]: 원격 저장소를 추가
>
> git remote rm [name]: 원격 저장소를 제거

## 10. git reset

> 로컬 저장소의 커밋을 취소
>
> git reset -sogt HEAD ^

## 11. git merge

> 현재 브랜치에 다른 지점에서 변결 사항을 병합하는 데 사용
>
> ex) bug-gix 를 master 브랜치에 병합
>
> git checkout master git merge bug-fix

## 12. git pull

>  원격 브랜치의 변경사항을 캡처하기 위해 사용
>
>  git checkout master git pull origin master



## **필요했던 것**

* 깃허브에  리드미 올리기
  * git clone https://github.com/Hyun-Kim95/python.git
  * git add readme.md
  * git commit -m "커밋메세지"
  * git push origin main
    * master -> master (fetch first) 오류
      * git push origin +master
        * 해결완료

* 깃허브에 파일 올리기
  * 원격 저장소 등록 및 복제
    * git push origin 브랜치이름: 해당 브랜치를 깃허브(원격 저장소)에 등록하기
    * clone의 경우 .git 파일이 없어도 되며 현재 파일 아래에 새롭게 파일 생성하기
    * git clone http 또는 SSH: 원격 저장소의 http 또는 SSH값을 이용해 로컬 저장소에 파일 복제하기
    * git clone /로컬/저장소/경로: 현재 경로에 로컬 저장소 경로 파일 복제하기
    * pull의 경우 .git 파일이 존재해야 한다
    * git pull origin master: 원격 저장소 중 master Branch에서 로컬 저장소로 파일 복제하기
  * 브랜치(Branch) 생성 및 삭제
    * git checkout -b 브랜치이름: 브랜치이름으로 새로운 브랜치를 생성한다
    * git checkout 브랜치이름: 사용하는 브랜치를 브랜치 이름에 해당하는 브랜치로 이동한다
    * git branch -d 브랜치이름: 브랜치 이름으로 된 브랜치를 삭제한다
