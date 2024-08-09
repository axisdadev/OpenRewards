import colorama, yaml

with open("config.yaml") as conf:
    config = yaml.safe_load(conf)

class Logging:
    def info(message: str):
        if config['LOGGING'] == True:
          print(f"{colorama.Fore.WHITE}[LOG] {message}{colorama.Fore.RESET}")
        
    def warn(message: str):
        if config['LOGGING'] == True:
          print(f"{colorama.Fore.YELLOW}[WARN] {message}{colorama.Fore.RESET}")
        
    def error(message: str):
        if config['LOGGING'] == True:
          print(f"{colorama.Fore.RED}[ERROR] {message}{colorama.Fore.RESET}")