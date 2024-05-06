from translate.module2 import TransLate, LangDetect, CodeLang, LanguageList


# Демонстрація функції TransLate
def test_TransLate():
    text1 = "Hello, how are you?"
    src1 = 'en'
    dest1 = 'es'
    translated_text1 = TransLate(text1, src1, dest1)
    print(f"Переклад '{text1}' з {src1} на {dest1}: {translated_text1}")

    text2 = "Bonjour tout le monde"
    src2 = 'fr'
    dest2 = 'de'
    translated_text2 = TransLate(text2, src2, dest2)
    print(f"Переклад '{text2}' з {src2} на {dest2}: {translated_text2}")


# Демонстрація функції LangDetect
def test_LangDetect():
    text1 = "Hello, how are you?"
    detected_lang = LangDetect(text1, 'lang')
    confidence = LangDetect(text1, 'confidence')
    print(f"Detected language for '{text1}': {detected_lang}, confidence: {confidence}")

    text2 = "Bonjour tout le monde!"
    detected_lang = LangDetect(text2, 'lang')
    confidence = LangDetect(text2, 'confidence')
    print(f"Detected language for '{text2}': {detected_lang}, confidence: {confidence}")

    text3 = "Hola mundo!"
    detected_lang = LangDetect(text3, 'lang')
    confidence = LangDetect(text3, 'confidence')
    print(f"Detected language for '{text3}': {detected_lang}, confidence: {confidence}")



# Демонстрація функції CodeLang
def test_CodeLang():
    lang1 = "english"
    iso_code1 = CodeLang(lang1)
    print(f"Код ISO-639 для мови '{lang1}': {iso_code1}")

    lang2 = "spanish"
    iso_code2 = CodeLang(lang2)
    print(f"Код ISO-639 для мови '{lang2}': {iso_code2}")


# Демонстрація функції LanguageList
def test_LanguageList():
    text5 = "Hello, world!"
    print("\nСписок мов з перекладом тексту:")
    LanguageList(out='screen', text=text5)

    print("\nЕкспорт списку мов у файл CSV:")
    LanguageList(out='file', text=text5)


if __name__ == "__main__":

    print("Тести для функції TransLate: ")
    test_TransLate()

    print("\nТести для функції LangDetect: ")
    test_LangDetect()

    print("\nТести для функції CodeLang: ")
    test_CodeLang()

    print("\nТести для функції LanguageList:\n")
    test_LanguageList()