import i18n


class LocaleMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(LocaleMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Locale(metaclass=LocaleMeta):
    def __init__(self):
        self.my_locale = "en"
        i18n.load_path.append("./locale")
        i18n.set("filename_format", "{locale}.{format}")

    def get_locale(self):
        return self.my_locale

    def set_locale(self, locale):
        if locale in ["es", "en", "fr", "pt"]:
            self.my_locale = locale

    def get_i18n(self):
        return i18n
