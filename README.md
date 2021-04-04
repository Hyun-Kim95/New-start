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

