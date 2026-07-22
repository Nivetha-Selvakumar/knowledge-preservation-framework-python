from collectors.github_collector import GithubCollector

class GithubAgent:

    def __init__(self):

        self.collector = GithubCollector()

    def collect(self):

        return self.collector.collect()