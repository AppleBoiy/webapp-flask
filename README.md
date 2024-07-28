## scripts

- init db

```shell
flask --app flaskr run --debug
```

- run dev/prod with specific config

```bash
./scripts/run.sh [dev/prod]
```

- make it installable

```bash
./scripts/setup.sh
```

- run app `with default config`

```shell
flask --app flaskr run --debug
```

- build

```shell
python -m build --wheel
```

#### Production

- run app `with production config`

```shell
flask --app flaskr run --debug
```