from dataclasses import dataclass

@dataclass
class AppConfig:
    debug: bool = False
    host: str = "127.0.0.1"
    port: str = "8050"
