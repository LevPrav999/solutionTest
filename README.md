# Flask CI/CD demo

Минимальный backend для практики на GitHub Actions.

## Локально

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
python -m ruff check .
python -m pytest -q
python app.py
```

Проверка: http://127.0.0.1:5000/health -> `{ "status": "ok" }`.

## GitHub Actions

- Папка `starter/`: приложение и тесты, workflow нужно написать самостоятельно по презентации.
- Папка `solution/`: полный пример `.github/workflows/pipeline.yml`.
- GitHub: создать **новый репозиторий** и перенести содержимое **одной** из этих папок в корень репозитория.
- Вкладка **Actions** покажет CI, вкладка **Packages** — опубликованный GHCR-образ.

## Важно

- `publish` выполняется только после успешного `test` в ветке `main`; для PR выполняется только CI.
- GHCR-образ — это **Continuous Delivery**, а не автоматическое обновление приложения на сервере.
- Права `packages: write` выделены только заданию публикации, используется `GITHUB_TOKEN`.
- Если выпуск в GHCR не проходит с ошибкой `permission_denied`, проверьте права Actions и права пакета (package linking/access).
- Образ в GitHub Packages может быть приватным. Для `docker pull` на своём компьютере может понадобиться вход в GHCR или изменение видимости.
- Версии внешних Actions в производственных workflow рекомендуется фиксировать по полному commit SHA.

Документация:
- https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
- https://docs.github.com/en/actions/tutorials/build-and-test-code/python
- https://docs.github.com/en/actions/tutorials/publish-packages/publish-docker-images
