from django.db import models
from django.conf import settings

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 글쓴이
    # ForeignKey(외래키)로 만들어져 다른 테이블과 연결됨
    # 기본적으로 1:n (many-to-one)관계이며 연결 대상이 되는 테이블을 인자로 받아들임
    # settings.AUTH_USER_MODEL은 장고에 기본적으로 내장된 유저 모델이다
    # 글들이 작성자 목록 테이블에 연결되도록 settings.AUTH_USER_MODEL를 외래키 인자로 전달하였다.

    title = models.CharField(max_length=100) # 글제목

    image = models.ImageField(blank=True) # 이미지
    # blank 옵션은 필드가 비어 있는 경우를 허용하는가에 대한 옵션이다.

    content = models.TextField(blank=True) # 글 내용
    created_date = models.DateTimeField(auto_now_add=True) # 글 작성 시간
    # auto_now_add 옵션은 객체가 처음 생성될 때의 시간을 자동으로 저장하는 옵션이다.

    published_date = models.DateTimeField(blank=True, null=True) # 글 게시날짜
    # null은 비어있는 값을 데이터베이스에 NULL으로 저장할지에 대한 옵션이다.

    # 관리자 페이지에서 내가 쓴 글을 쉽게 구별하기 위해 써주는 형식 __str__
    def __str__(self):
        return self.title
