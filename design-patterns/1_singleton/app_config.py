class AppConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    config1 = AppConfig()
    config2 = AppConfig()

    print(config1 is config2)  # True
