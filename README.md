# SAI API 서버

IC light(https://github.com/lllyasviel/IC-Light) 오픈소스를 이용하여 이미지의 배경과 분위기를 수정해주는 SAI 서비스 API 서버입니다.

## 시작하기

```bash
$ git clone https://github.com/kimgangmin-thinkingfriends/SAI.git

$ conda create --name sai-api-server python=3.10
$ conda activate sai-api-server
$ pip install -r requirements.txt

$ cd src
$ nano .env

INPUT_IMAGE_PATH="{원본 이미지 경로}"
OUTPUT_IMAGE_PATH="{생성 이미지 경로}"
API_KEY="{API 키}"

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=postgres

$ python main.py
```
