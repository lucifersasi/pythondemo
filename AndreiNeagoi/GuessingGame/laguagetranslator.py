from translate import Translator
import io

translator = Translator(to_lang="ja")
try:
    with io.open('./test_en.txt', mode='r', encoding="utf-8") as my_file:
        text = my_file.read()
        changed_text = translator.translate(text)
        with io.open('./test_ja.txt', mode='w', encoding="utf-8") as my_file2:
            my_file2.write(changed_text+'\n')
except FileNotFoundError as e:
    print('there is no file of that name dude!')
