# class MarkdownGenerator:

#     def __init__(self):
#         pass

#     def generate(self, knowledge):

#         markdown = "# Enterprise Knowledge Document\n\n"

#         markdown += "## Repository\n\n"
#         markdown += f"{knowledge['repository_name']}\n\n"

#         markdown += "## Description\n\n"
#         markdown += f"{knowledge['repository_description']}\n\n"

#         markdown += "## Generated On\n\n"
#         markdown += f"{knowledge['generated_on']}\n\n"

#         markdown += "---\n\n"

#         markdown += "## Feature Name\n\n"
#         markdown += f"{knowledge['feature_name']}\n\n"

#         markdown += "## Business Functionality\n\n"
#         markdown += f"{knowledge['business_functionality']}\n\n"

#         markdown += "## Problem Solved\n\n"
#         markdown += f"{knowledge['problem_solved']}\n\n"

#         markdown += "## Technical Summary\n\n"
#         markdown += f"{knowledge['technical_summary']}\n\n"

#         markdown += "## Knowledge Transfer\n\n"
#         markdown += f"{knowledge['knowledge_transfer']}\n\n"

#         markdown += "---\n\n"

#         markdown += "## Technologies\n\n"

#         for technology in knowledge["technologies"]:
#             markdown += f"- {technology}\n"

#         markdown += "\n"

#         markdown += "## Frameworks\n\n"

#         for framework in knowledge["frameworks"]:
#             markdown += f"- {framework}\n"

#         markdown += "\n"

#         markdown += "## Files Modified\n\n"

#         for file in knowledge["files_modified"]:
#             markdown += f"- {file}\n"

#         markdown += "\n"

#         markdown += "## Classes\n\n"

#         for cls in knowledge["classes"]:
#             markdown += f"- {cls}\n"

#         markdown += "\n"

#         markdown += "## Methods\n\n"

#         for method in knowledge["methods"]:
#             markdown += f"- {method}\n"

#         markdown += "\n"

#         markdown += "## APIs\n\n"

#         for api in knowledge["apis"]:
#             markdown += f"- {api}\n"

#         markdown += "\n"

#         markdown += "## Database Changes\n\n"

#         for change in knowledge["database_changes"]:
#             markdown += f"- {change}\n"

#         markdown += "\n"

#         markdown += "## Security Changes\n\n"

#         for security in knowledge["security_changes"]:
#             markdown += f"- {security}\n"

#         markdown += "\n"

#         markdown += "## Configuration Changes\n\n"

#         for configuration in knowledge["configuration_changes"]:
#             markdown += f"- {configuration}\n"

#         markdown += "\n"

#         markdown += "## Dependencies\n\n"

#         for dependency in knowledge["dependencies"]:
#             markdown += f"- {dependency}\n"

#         markdown += "\n"

#         markdown += "## Impact\n\n"
#         markdown += f"{knowledge['impact']}\n\n"

#         markdown += "## Learning Points\n\n"

#         for point in knowledge["learning_points"]:
#             markdown += f"- {point}\n"

#         return markdown


class MarkdownGenerator:

    def __init__(self):
        pass

    def generate(self, knowledge):

        markdown = "# Enterprise Knowledge Base\n\n"

        ###############################################################
        # Organization Summary
        ###############################################################

        markdown += "## Organization Summary\n\n"
        markdown += f"{knowledge.get('organization_summary', '')}\n\n"

        ###############################################################
        # Repository Overview
        ###############################################################

        markdown += "## Repository Overview\n\n"

        for repository in knowledge.get("repositories", []):

            markdown += f"- {repository}\n"

        markdown += "\n"

        ###############################################################
        # Business Domains
        ###############################################################

        markdown += "## Business Domains\n\n"

        for domain in knowledge.get("business_domains", []):

            markdown += f"- {domain}\n"

        markdown += "\n"

        ###############################################################
        # Major Features
        ###############################################################

        markdown += "## Major Features\n\n"

        for feature in knowledge.get("major_features", []):

            markdown += f"- {feature}\n"

        markdown += "\n"

        ###############################################################
        # Functional Modules
        ###############################################################

        markdown += "## Functional Modules\n\n"

        for module in knowledge.get("functional_modules", []):

            markdown += f"- {module}\n"

        markdown += "\n"

        ###############################################################
        # Technologies
        ###############################################################

        markdown += "## Technologies\n\n"

        for technology in knowledge.get("technologies", []):

            markdown += f"- {technology}\n"

        markdown += "\n"

        ###############################################################
        # Frameworks
        ###############################################################

        markdown += "## Frameworks\n\n"

        for framework in knowledge.get("frameworks", []):

            markdown += f"- {framework}\n"

        markdown += "\n"

        ###############################################################
        # Libraries
        ###############################################################

        markdown += "## Libraries\n\n"

        for library in knowledge.get("libraries", []):

            markdown += f"- {library}\n"

        markdown += "\n"

        ###############################################################
        # APIs
        ###############################################################

        markdown += "## APIs\n\n"

        for api in knowledge.get("apis", []):

            markdown += f"- {api}\n"

        markdown += "\n"

        ###############################################################
        # Database Technologies
        ###############################################################

        markdown += "## Database Technologies\n\n"

        for database in knowledge.get("database", []):

            markdown += f"- {database}\n"

        markdown += "\n"

        ###############################################################
        # Security
        ###############################################################

        markdown += "## Security Mechanisms\n\n"

        for security in knowledge.get("security", []):

            markdown += f"- {security}\n"

        markdown += "\n"

        ###############################################################
        # Configuration
        ###############################################################

        markdown += "## Configuration\n\n"

        for configuration in knowledge.get("configuration", []):

            markdown += f"- {configuration}\n"

        markdown += "\n"

        ###############################################################
        # Important Classes
        ###############################################################

        markdown += "## Important Classes\n\n"

        for clazz in knowledge.get("important_classes", []):

            markdown += f"- {clazz}\n"

        markdown += "\n"

        ###############################################################
        # Important Methods
        ###############################################################

        markdown += "## Important Methods\n\n"

        for method in knowledge.get("important_methods", []):

            markdown += f"- {method}\n"

        markdown += "\n"

        ###############################################################
        # Frequently Modified Files
        ###############################################################

        markdown += "## Frequently Modified Files\n\n"

        for file in knowledge.get("important_files", []):

            markdown += f"- {file}\n"

        markdown += "\n"

        ###############################################################
        # Development Timeline
        ###############################################################

        markdown += "## Development Timeline\n\n"
        markdown += f"{knowledge.get('development_timeline', '')}\n\n"

        ###############################################################
        # Bug Fixes
        ###############################################################

        markdown += "## Major Bug Fixes\n\n"

        for bug in knowledge.get("bug_fixes", []):

            markdown += f"- {bug}\n"

        markdown += "\n"

        ###############################################################
        # Enhancements
        ###############################################################

        markdown += "## Enhancements\n\n"

        for enhancement in knowledge.get("enhancements", []):

            markdown += f"- {enhancement}\n"

        markdown += "\n"

        ###############################################################
        # Knowledge Transfer
        ###############################################################

        markdown += "## Knowledge Transfer Notes\n\n"
        markdown += f"{knowledge.get('knowledge_transfer', '')}\n\n"

        ###############################################################
        # Learning Points
        ###############################################################

        markdown += "## Learning Points\n\n"

        for learning in knowledge.get("learning_points", []):

            markdown += f"- {learning}\n"

        markdown += "\n"

        return markdown
