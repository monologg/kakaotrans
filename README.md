# Kakaotrans

Unofficial python API for [Kakao translate service](https://translate.kakao.com).

## Installation

```bash
$ pip install kakaotrans
```

## Usage

### Basic Usage

```python
>>> from kakaotrans import Translator
>>> translator = Translator()
>>> translator.translate("Try your best rather than be the best.")
# '최고가 되기보다는 최선을 다하라.'
>>> translator.translate("최고가 되기보다는 최선을 다하라.", source='kr', target='de')
# 'Tun Sie Ihr Bestes, anstatt das Beste zu sein.'
```

### Separate the query into multiple sentences

Translation query might include multiple sentences. If you set separate_lines=True, translator will automatically separate the query and return the list of multiple sentences.

```python
from kakaotrans import Translator

translator = Translator()

translator.translate("""지난해 3월 오픈한 카카오톡 주문하기는 현재까지 약 250만명의 회원을 확보했다.
            전 국민에게 친숙한 카카오톡 UI를 활용하기 때문에 별도의 앱을 설치할 필요 없이 카카오톡 내에서 모든 과정이 이뤄지는 것이 특징이다.""",
            source='kr', target='en', separate_lines=True)
# ['The ordering of KakaoTalk, which opened in March last year, has secured about 2.5 million members to date.', 'Because it uses KakaoTalk UI, which is familiar to the whole nation, it is characterized by all the processes in KakaoTalk without having to install a separate app.']
```

### Save translated result as file

```python
>>> from kakaotrans import Translator
>>> translator = Translator()
>>> translator.translate("Try your best rather than be the best.", save_as_file=True, file_name='result.txt')
```

## Reference

- [googletrans](https://github.com/ssut/py-googletrans)
- [pypapago](https://github.com/Beomi/pypapago)
