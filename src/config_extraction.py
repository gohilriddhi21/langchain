import yaml

class ConfigExtraction:
    def __init__(self):
        try:
            with open("config/config.yaml") as file:
                self.config = yaml.safe_load(file)

            self.OPEN_API_KEY = self.config['keys']['openapi_key']
        except yaml.YAMLError as err:
            print(err)

if __name__ == '__main__':
    print(ConfigExtraction().OPEN_API_KEY)