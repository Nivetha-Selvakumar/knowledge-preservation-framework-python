from collectors.github_collector import GithubCollector


class GithubAgent:

    def __init__(self):

        self.collector = GithubCollector()

    def activate(self, request):

        print("GitHub Agent Started")

        return self.collector.collect(request)
