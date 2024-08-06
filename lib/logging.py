import colorama

class Logging:
    def info(message: str):
        print(f"{colorama.Fore.WHITE}[LOG] {message}{colorama.Fore.RESET}")
        
    def warn(message: str):
        print(f"{colorama.Fore.YELLOW}[WARN] {message}{colorama.Fore.RESET}")
        
    def error(message: str):
        print(f"{colorama.Fore.RED}[ERROR] {message}{colorama.Fore.RESET}")