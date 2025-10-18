# quindar_technical_challenge

This service takes a daily csv of station bytes received and sent. It then looks for discrepancies.

To get the container working run:

```bash
docker compose build
docker compose up
```

you can then curl it to ensure it returns the expected response

```bash
curl localhost:8000
```

You can also interact with it in a web browser go to
```bash
localhost:8000/docs
```

You can run tests with 

```bash
pytes
```

I have never set up git hub actions so I am quite confident I did it incorrectly!
