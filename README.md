# episen_big_data

## First way

Install java via https://code.visualstudio.com/docs/languages/java


``
pip install virtualenv
virtual_env pyspark_env
source pyspark_env/bin/activate
pip install pyspark
```

Download `pyspark_init.py`

```
spark-submit pyspark_init.py
```

## Second way

- Download `docker-compose.yml`
- Install docker if not already done and launch it
- In a terminal `docker-compose up`, this will download all required images and launch all you need to run spark locally
