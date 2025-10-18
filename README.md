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


I am out of time. I want to do more but I have 5 minutes so I will take that time to explain where I was going. I created a models file that would have one model for telemeters and the other for rows in the CSV. It would make it easy to add expected and optional telemeters and include expected parameters. I would add a global config to drive the healthy value and unhealthy value thresholds.

I would then integrate that into the handler so from the API layer the handler just does everything and the API can return neatly formatted data.

Overall I am moderately happy with this. It does the job as I understand it. But there are a lot of improvements I would like to make. I developed in a way that it would be easy to explain what to do with each next step. This is to simulate working with others where I could pass off individual tasks or the whole project if I had to shift gears.
