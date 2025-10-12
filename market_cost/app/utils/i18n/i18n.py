import json
import os


class I18n:
    def __init__(self, lang="en", i18n_dir="i18n"):
        self.i18n_dir = i18n_dir
        self.lang = lang
        self.translations = {}
        self._load_language(lang)

    def _load_language(self, lang):
        """加载语言文件"""
        lang_path = os.path.join(self.i18n_dir, f"{lang}.json")
        if not os.path.exists(lang_path):
            raise FileNotFoundError(f"语言文件不存在: {lang_path}")

        with open(lang_path, "r", encoding="utf-8") as f:
            self.translations = json.load(f)

    def set_lang(self, lang):
        """切换语言"""
        if lang != self.lang:
            self.lang = lang
            self._load_language(lang)

    def t(self, key, default=None):
        """翻译 key"""
        return self.translations.get(key, default or key)


# 初始化默认语言
i18n = I18n(lang="zh")


# 对外封装函数（全局使用）
def t(key, default=None):
    return i18n.t(key, default)


# 切换语言
def set_lang(lang):
    i18n.set_lang(lang)
