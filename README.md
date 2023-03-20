# Ansible Коллекция - files.create_file_by_content

Варианты для установки коллекции:
- Создание архива на основе этого репозитория при помощи команды ```ansible-galaxy collection build```, и локальная установка ```ansible-galaxy collection install <archivename>.tar.gz```;
- Подключение коллекции через requirements.yml

[Пример использования](./playbooks/site.yml)

Параметры:
- path - путь до файла, например "/tmp/1.txt"
- content - содержимое файла, например "Hello world"