from googletrans import Translator, LANGUAGES
import pandas as pd

def TransLate(text: str, src: str, dest: str) -> str:
    translator = Translator()

    if dest not in LANGUAGES:
        raise ValueError(f"Invalid destination language: {dest}")

    if src != 'auto':
        if src not in LANGUAGES:
            raise ValueError(f"Invalid source language: {src}")
        detected_src = src
    else:
        # Автоматично визначити мову вхідного тексту
        detected_lang = translator.detect(text)
        detected_src = detected_lang.lang

    translated = translator.translate(text, src=detected_src, dest=dest)

    return translated.text

def LangDetect(text : str, set : str) -> str:
    translator = Translator()

    if set not in ('lang', 'confidence', 'all'):
        raise ValueError("Invalid mode. Please use 'lang', 'confidence', or 'all'.")

    detection_result = translator.detect(text)
    detected_lang = detection_result.lang
    confidence = detection_result.confidence

    if detected_lang not in LANGUAGES:
        raise ValueError(f"Invalid detected language: {detected_lang}")

    if set == 'lang':
        return detected_lang
    elif set == 'confidence':
        return confidence
    else:
        return detected_lang, confidence


def CodeLang(lang: str) -> str:

    res = ""

    lang_lower = lang.lower()

    for code, name in LANGUAGES.items():
        if name.lower() == lang_lower:
           res = code

    if res == "":
        res = "unknown"

    return res


def LanguageList(out: str = "screen", text: str = None) -> str:

    translator = Translator()

    data = []
    for code, name in LANGUAGES.items():
        language_info = {'N': len(data) + 1, 'Language': name, 'ISO-639 code': code}
        if text:
            try:
                translation = translator.translate(text, dest=code)
                language_info['Text'] = translation.text
            except Exception as e:
                language_info['Text'] = f"Translation error: {str(e)}"
        data.append(language_info)

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Determine the output destination
    if out == 'screen':
        # Output the table to the screen
        print(df.to_string(index=False))
        return "Ok"
    elif out == 'file':
        # Output the table to a file (CSV format)
        file_name = 'language_table.csv'
        df.to_csv(file_name, index=False)
        print(f"Table exported to '{file_name}'")
        return "Ok"
    else:
        return "Invalid output format. Please use 'screen' or 'file'."