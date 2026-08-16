import requests


class GithubApiService:

    BASE_URL = "https://api.github.com"

    # ==========================================================
    # COMMON HEADERS
    # ==========================================================

    def _headers(self, token: str):

        return {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    # ==========================================================
    # GET ALL USER REPOSITORIES
    # ==========================================================

    def get_repositories(self, token: str):

        url = f"{self.BASE_URL}/user/repos"

        response = requests.get(
            url, headers=self._headers(token), params={"per_page": 100}, timeout=30
        )

        response.raise_for_status()

        return response.json()

    # ==========================================================
    # GET ONE REPOSITORY
    # ==========================================================

    def get_repository(self, token: str, owner: str, repo: str):

        url = f"{self.BASE_URL}/repos/" f"{owner}/{repo}"

        print(f"Fetching repository: " f"{owner}/{repo}")

        response = requests.get(url, headers=self._headers(token), timeout=30)

        response.raise_for_status()

        return response.json()

    # ==========================================================
    # GET COMMITS
    # ==========================================================

    def get_commits(self, token: str, owner: str, repo: str):

        url = f"{self.BASE_URL}/repos/" f"{owner}/{repo}/commits"

        response = requests.get(
            url, headers=self._headers(token), params={"per_page": 100}, timeout=30
        )

        response.raise_for_status()

        return response.json()

    # ==========================================================
    # GET COMMIT DETAILS
    # ==========================================================

    def get_commit_details(self, token: str, owner: str, repo: str, sha: str):

        url = f"{self.BASE_URL}/repos/" f"{owner}/{repo}/commits/{sha}"

        response = requests.get(url, headers=self._headers(token), timeout=30)

        response.raise_for_status()

        return response.json()

    # ==========================================================
    # GET ISSUES
    # ==========================================================

    def get_issues(self, token: str, owner: str, repo: str):

        url = f"{self.BASE_URL}/repos/" f"{owner}/{repo}/issues"

        response = requests.get(
            url,
            headers=self._headers(token),
            params={"state": "all", "per_page": 100},
            timeout=30,
        )

        response.raise_for_status()

        return response.json()

    # ==========================================================
    # GET PULL REQUESTS
    # ==========================================================

    def get_pull_requests(self, token: str, owner: str, repo: str):

        url = f"{self.BASE_URL}/repos/" f"{owner}/{repo}/pulls"

        response = requests.get(
            url,
            headers=self._headers(token),
            params={"state": "all", "per_page": 100},
            timeout=30,
        )

        response.raise_for_status()

        return response.json()

    # ==========================================================
    # GET README
    # ==========================================================

    def get_readme(self, token: str, owner: str, repo: str):

        url = f"{self.BASE_URL}/repos/" f"{owner}/{repo}/readme"

        response = requests.get(url, headers=self._headers(token), timeout=30)

        response.raise_for_status()

        data = response.json()

        return data.get("content")

    # ==========================================================
    # GET EXISTING WEBHOOKS
    # ==========================================================

    def get_webhooks(self, token: str, owner: str, repository_name: str):

        url = f"{self.BASE_URL}/repos/" f"{owner}/{repository_name}/hooks"

        print(f"Fetching GitHub webhooks for " f"{owner}/{repository_name}")

        response = requests.get(url, headers=self._headers(token), timeout=30)

        response.raise_for_status()

        return response.json()

    # ==========================================================
    # CREATE GITHUB WEBHOOK
    # ==========================================================

    def create_webhook(
        self, token: str, owner: str, repository_name: str, webhook_url: str
    ):

        print("=" * 80)
        print("REGISTERING GITHUB WEBHOOK")
        print("=" * 80)

        if not token:
            raise ValueError("GitHub token is required")

        if not owner:
            raise ValueError("Repository owner is required")

        if not repository_name:
            raise ValueError("Repository name is required")

        if not webhook_url:
            raise ValueError("Webhook URL is required")

        print(f"Repository : " f"{owner}/{repository_name}")

        print(f"Webhook URL: " f"{webhook_url}")

        # ======================================================
        # GITHUB WEBHOOK API
        # ======================================================

        url = f"{self.BASE_URL}/repos/" f"{owner}/{repository_name}/hooks"

        # ======================================================
        # CHECK EXISTING WEBHOOK
        # ======================================================

        existing_webhooks = self.get_webhooks(
            token=token, owner=owner, repository_name=repository_name
        )

        for webhook in existing_webhooks:

            config = webhook.get("config", {})

            existing_url = config.get("url")

            if existing_url == webhook_url:

                print("=" * 80)
                print("GITHUB WEBHOOK ALREADY EXISTS")
                print("=" * 80)

                print(f"Webhook ID: " f"{webhook.get('id')}")

                return webhook

        # ======================================================
        # CREATE NEW WEBHOOK
        # ======================================================

        payload = {
            "name": "web",
            "active": True,
            "events": ["push", "pull_request", "issues"],
            "config": {"url": webhook_url, "content_type": "json", "insecure_ssl": "0"},
        }

        print("Creating new GitHub webhook...")

        response = requests.post(
            url, headers=self._headers(token), json=payload, timeout=30
        )

        response.raise_for_status()

        result = response.json()

        print("=" * 80)
        print("GITHUB WEBHOOK REGISTERED SUCCESSFULLY")
        print("=" * 80)

        print(f"Webhook ID: " f"{result.get('id')}")

        print(f"Webhook URL: " f"{result.get('config', {}).get('url')}")

        return result
