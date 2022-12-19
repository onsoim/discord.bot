
from dotenv     import load_dotenv
from json       import loads
from os         import getenv
from requests   import get


class JOB:
    def __init__(self):
        load_dotenv(verbose=True)

    def get_new(self):
        jobs = []

        url = getenv('URL1')
        api = getenv('API1')

        while api:
            res   = loads( get(url + api).text )

            jobs += [ data['id'] for data in res['data'] ]
            api   = res['links']['next']

        return [ f"{url}/wd/{job}" for job in jobs ]


if __name__ == "__main__":
    print(JOB().get_new())
