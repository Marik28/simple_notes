import os
import re


def main():
    """Устанавливает переменные окружения для запуска сервера Django и запуска postgresql"""
    with open(".env.dev", 'r', encoding='utf-8') as f:
        for line in f.readlines():
            result = re.match(r'(\w+)=(.+)', line)
            env_name, env_value = result.groups()
            os.environ[env_name] = env_value
