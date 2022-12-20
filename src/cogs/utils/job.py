
from dotenv     import load_dotenv
from json       import dump, dumps, loads
from os         import getenv
from os.path    import exists
from requests   import get


class JOB:    
    def __init__(self):
        load_dotenv(verbose=True)

        self.filepath   = 'res/job.json'
        self.init       = {
            'wd': []
        }

    def load(self, filepath = None):
        if not filepath: filepath = self.filepath

        if exists(filepath):
            with open(filepath, 'r') as r:
                return loads(r.read())

        return loads(dumps(self.init))

    def get_new(self):
        jobs = loads(dumps(self.init))
        prev = self.load()
        new  = []

        # WD
        url = getenv('URL1')
        api = getenv('API1')

        while api:
            res = loads( get(url + api).text )
            api = res['links']['next']
            jobs['wd'] += [ data['id'] for data in res['data'] ]

        new += [ f"{url}/wd/{job}" for job in list(set(jobs['wd']) - set(prev['wd'])) ]

        dump(jobs, open(self.filepath, 'w'))

        return new


if __name__ == "__main__":
    print(JOB().get_new())
