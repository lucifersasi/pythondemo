from translate import Translator

translator = Translator(to_lang="ja")
try:
    with open('./read.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('./write.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError:
    print('there is no file of that name dude!')
