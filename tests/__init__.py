
from primaryschool.subjects.yuwen.g_pinyin_missile import Word

word = Word()
for i in range(0,14):
    words = word.get_words(i)
    assert isinstance(words,list)
    assert len(words) > 0 
