# skt-fly-teamHashTag-NLP
```
SKT FLY AI 프로젝트 <VideoDot: 5분 뚝딱 자동 브이로그 생성 서비스>
```
### 개발 배경
하루를 영상으로 기록하는 MZ 세대를 위한 앱 서비스입니다. 영상 편집에 오랜 시간을 소요되고 영상 편집 기술의 부재로 인해 브이로그 제작의 어려움이 있는 사용자를 위해 쉽고 빠른 원클릭 자동 브이로그 생성 서비스를 개발하게 되었습니다.

### 특징
1. 사용자가 원하는 핵심 주제를 중심으로 브이로그가 생성되며 썸네일과 해시태그도 자동으로 추출됩니다.
2. 사용자는 가족과 친구들에게 일상을 공유할 수 있는 "한뼘 사이 소셜피드"를 이용할 수 있습니다. 댓글과 좋아요 기능도 포함되어 있습니다.

### 담당 역할
NLP팀에서 [qqq3964](https://github.com/qqq3964/SKT_Project) 팀원과 **(1) BERT모델 기반 문서의 토픽 분류 모델**과 **(2) 해시태그 추출 알고리즘**을 공동으로 개발하였습니다.

### 개발 환경
- **Language**</br>
![python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![pytorch](https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
- **Team Collaboration Tool**</br>
![github](https://img.shields.io/badge/github-100000?style=for-the-badge&logo=github&logoColor=white)
![notion](https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white)

### (1) BERT모델 기반 문서의 주제 분류 모델
✅ *[Classification-Notebook 파일](https://github.com/soyeong-kim/skt-fly-teamHashTag-NLP/tree/main/Classification-Notebook)*</br>
- 브이로그 인기 분야 10개 클래스(가족, 스터디, 뷰티, 반려동물, 운동/스포츠, 음식, 여행, 연애/결혼, 문화생활, 직장인)로 데이터셋을 구축합니다.
- 해당 데이터셋을 Multilingual BERT로 Fine-tuning하여 토픽 분류 모델을 만들었습니다.
- 영상의 구간별 음성 텍스트를 BERT모델 기반 문서의 주제 분류 모델을 활용하여 핵심 구간을 선정했습니다.

### (2) 해시태그 추출 알고리즘
✅ *[Hashtag-Notebook 파일](https://github.com/soyeong-kim/skt-fly-teamHashTag-NLP/tree/main/Hashtag-Notebook)*</br>
- 핵심 구간의 음성을 Speech Recognition API를 통해 텍스트로 변환하여 KeyBERT 모델을 통해 Top-1 명사를 추출합니다.
- 핵심 구간의 이미지에서 YOLOv5를 통해 객체명을 추출합니다.
- 사전 학습된 Word2Vec 모델을 사용하여 핵심 구간의 Top-1 명사와 객체명 사이의 유사도를 계산하고 유사도가 높은 객체명을 추출합니다.
- 따라서 해시태그 후보로 Top-1 명사, 객체명이 추출됩니다.

### 팀원 소개
📌 [Team Repository](https://github.com/skt-fly-teamHashTag)</br>
|[eunsun53](https://github.com/skt-fly-teamHashTag/ML-total)|[BBIYAC](https://github.com/skt-fly-teamHashTag/Frontend)|[JOOYUNHAK](https://github.com/JOOYUNHAK/skt-fly-ai-team-hashtag-backend)|[qqq3964](https://github.com/qqq3964/SKT_Project)|[rkskek1226](https://github.com/rkskek1226/SKT_FLY_AI_Challenger_HashTag)|
|:----------:|:----------:|:----------:|:----------:|:----------:|
|**팀장&AI팀-Vision**</br>영상 요약 추출|**프론트엔드**</br>사용자의 화면 개발|**백엔드**</br>DB 설계와 클라우드 배포|**AI팀-NLP**</br> 해시태그 추출|**AI팀-Vision**</br>썸네일 추출|

### 데모 영상
➡️ [Demo Video](https://github.com/skt-fly-teamHashTag/Frontend/blob/master/README.md#%EC%8B%A4%ED%96%89-%EC%98%81%EC%83%81) 링크를 통해 브이로그 자동 생성 앱의 데모 영상을 확인할 수 있습니다.
