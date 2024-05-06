from translate.module1 import TransLate, LangDetect, CodeLang, LanguageList

def test_TransLate():
    # Тест 1
    text1 = "Hello, how are you?"
    src1 = 'en'
    dest1 = 'es'
    translated_text1 = TransLate(text1, src1, dest1)
    print(translated_text1)

    # Тест 2
    text2 = "Bonjour tout le monde"
    src2 = 'fr'
    dest2 = 'de'
    translated_text2 = TransLate(text2, src2, dest2)
    print(translated_text2)

def test_LangDetect():

    # Тест 1
    text1 = "Hello, how are you?"
    detected_lang1 = LangDetect(text1, 'lang')
    print(f"Виявлена мова для тексту '{text1}': {detected_lang1}")

    # Тест 2
    text2 = "Hola, ¿cómo estás?"
    confidence2 = LangDetect(text2, 'confidence')
    print(f"Впевненість виявлення мови для тексту '{text2}': {confidence2}")

def test_CodeLang():

     # Тест 1: Пошук коду ISO-639 за назвою мови
    lang1 = "english"
    iso_code1 = CodeLang(lang1)
    expected_code1 = 'en'
    print(f"Код ISO-639 для мови '{lang1}': {iso_code1}")
    assert iso_code1 == expected_code1, f"Unexpected ISO code. Expected: {expected_code1}, Got: {iso_code1}"

    # Тест 2: Пошук коду ISO-639 за назвою мови (неспівпадіння регістрів)
    lang2 = "spanish"
    iso_code2 = CodeLang(lang2)
    expected_code2 = 'es'
    print(f"Код ISO-639 для мови '{lang2}': {iso_code2}")
    assert iso_code2 == expected_code2, f"Unexpected ISO code. Expected: {expected_code2}, Got: {iso_code2}"

def test_defLanguageList():

    # Тест 1: Створення списку мов для тексту
    text = "Hello, how are you?"
    result = LanguageList(out='screen', text=text)
    print(result)

    # Тест 2: Експорт списку мов у файл CSV
    result = LanguageList(out='file', text=text)
    print(result)


if __name__ == "__main__":

    print("Тести для функції TransLate: ")
    test_TransLate()

    print("\nТести для функції LangDetect: ")
    test_LangDetect()

    print("\nТести для функції CodeLang: ")
    test_CodeLang()

    print("\nТести для функції LanguageList:\n")
    test_defLanguageList()
