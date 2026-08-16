import json
import os
from datetime import datetime


class ActivityStore:

    def __init__(self):

        self.storage_directory = "storage/activities"

        os.makedirs(self.storage_directory, exist_ok=True)

    def save(self, activities: list):

        if not activities:
            return 0

        saved_count = 0

        for activity in activities:

            repository_id = str(activity.get("repositoryId"))

            file_path = os.path.join(self.storage_directory, f"{repository_id}.json")

            existing = []

            if os.path.exists(file_path):

                try:

                    with open(file_path, "r", encoding="utf-8") as file:

                        existing = json.load(file)

                except Exception:

                    existing = []

            external_id = activity.get("externalId")

            already_exists = any(
                str(item.get("externalId")) == str(external_id) for item in existing
            )

            if already_exists:

                print(f"Activity already exists: " f"{external_id}")

                continue

            activity["storedAt"] = datetime.now().isoformat()

            existing.append(activity)

            with open(file_path, "w", encoding="utf-8") as file:

                json.dump(existing, file, indent=4, ensure_ascii=False)

            saved_count += 1

            print(f"Activity stored: " f"{external_id}")

        return saved_count
