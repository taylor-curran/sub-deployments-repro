# sub-deployments-repro

git clone https://github.com/taylor-curran/sub-deployments-repro.git

cd sub-deployments-repro

conda create --name sub-deployments-repro python=3.10

conda activate sub-deployments-repro

pip install prefect prefect-aws python-dotenv

populate .env file

```text
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
```

aws sso login

prefect work-pool create local-docker --type docker

In the work pool, specify the image as:
`taycurran/test-projects-june11:3.3`

Reminder: Make sure you have a docker desktop running

prefect worker start --pool "local-docker"

prefect deploy --all

prefect deployment run 'sub-deployments/dep-sub-deployments' --param sleep_time_subflows=20

prefect deployment run 'task-wrapped-deployments/dep-task-wrapped' --param sleep_time_subflows=5

