import di
import os


container = di.Container()


class ConfigReader:
    def get_config(self):
        pass


class EnvironmentConfigReader(ConfigReader):
    def get_config(self):
        return {
            "logging": {"level": os.environ.get("LOGGING_LEVEL", "debug")},
            "greeting": os.environ.get("GREETING", "Hello world"),
        }


container.bind(di.Dependant(EnvironmentConfigReader), ConfigReader)


class Greeter:
    def greet(self):
        pass


class ConsoleGreeter(Greeter):
    def __init__(self, config_reader: ConfigReader):
        self.config = config_reader.get_config()

    def greet(self):
        print(self.config["greeting"])


container.bind(di.Dependant(ConsoleGreeter), Greeter)

provider = container.solve(di.Dependant(Greeter))


def di_main():
    greeter = container.execute_sync(provider)
    assert isinstance(greeter, ConsoleGreeter)


if __name__ == "__main__":
    di_main()
