from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    translator = MyMemoryTranslator(source='english', target='french')
    frenchText = translator.translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    translator = MyMemoryTranslator(source='french', target='english')
    englishText = translator.translate(frenchText)
    return englishText
