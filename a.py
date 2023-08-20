from googletrans import Translator

# 1. 번역기 생성
translator = Translator()

# 2. 언어 감지를 원하는 문장 설정
sentence = "안녕하세요."

# 3. 언어 감지
detected = translator.detect(sentence)

print(detected)
