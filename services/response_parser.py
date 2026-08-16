import json


class ResponseParser:

    def __init__(self):
        pass

    def parse(self, response_text):

        if not response_text:
            raise Exception("Empty response received from LLM")

        response_text = response_text.strip()

        # Remove markdown code fences
        if response_text.startswith("```json"):
            response_text = response_text.replace("```json", "", 1)

        if response_text.startswith("```"):
            response_text = response_text.replace("```", "", 1)

        if response_text.endswith("```"):
            response_text = response_text[:-3]

        response_text = response_text.strip()

        try:
            data = json.loads(response_text)

        except json.JSONDecodeError as ex:
            raise Exception(f"Invalid JSON returned by LLM.\n{ex}")

        defaults = {
            "feature_name": "",
            "business_functionality": "",
            "problem_solved": "",
            "knowledge_transfer": "",
            "technical_summary": "",
            "technologies": [],
            "frameworks": [],
            "files_modified": [],
            "classes": [],
            "methods": [],
            "apis": [],
            "database_changes": [],
            "security_changes": [],
            "configuration_changes": [],
            "dependencies": [],
            "impact": "",
            "learning_points": [],
        }

        for key, value in defaults.items():

            if key not in data:
                data[key] = value

        return data
