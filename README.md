# quindar_technical_challenge

Im writing this to be quick and dirty, will advice later

To get the container working run:

```bash
docker compose build
docker compose up
```

you can then curl it to ensure it returns the expected response

```bash
curl localhost:8000
```

```
{"Hello":"World"}
```

You can run tests with 

```bash
pytes
```

