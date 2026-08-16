import json


class PromptBuilder:

    def __init__(self):
        pass

    def build_prompt(self, enterprise_context):

        prompt = f"""
You are an Enterprise Knowledge Preservation AI.

You are provided with GitHub data collected from multiple repositories belonging to the same organization.

Analyze all repositories together and generate a comprehensive enterprise knowledge document.

Enterprise GitHub Context:

{json.dumps(enterprise_context, indent=2)}

------------------------------------------------------------

Analyze and identify:

1. Overall Organization Purpose
2. Repository Summaries
3. Business Domains
4. Major Features
5. Functional Modules
6. Technologies Used
7. Frameworks
8. Libraries
9. APIs
10. Database Technologies
11. Security Mechanisms
12. Configuration Files
13. Important Classes
14. Important Methods
15. Frequently Modified Files
16. Development Timeline
17. Bug Fixes
18. Enhancements
19. Knowledge Transfer Notes
20. Learning Points

Return ONLY valid JSON.

JSON Format:

{{
    "organization_summary": "",
    "repositories": [],
    "business_domains": [],
    "major_features": [],
    "functional_modules": [],
    "technologies": [],
    "frameworks": [],
    "libraries": [],
    "apis": [],
    "database": [],
    "security": [],
    "configuration": [],
    "important_classes": [],
    "important_methods": [],
    "important_files": [],
    "development_timeline": "",
    "bug_fixes": [],
    "enhancements": [],
    "knowledge_transfer": "",
    "learning_points": []
}}

Return JSON only.
Do not include markdown.
Do not include explanations.
"""

        return prompt
