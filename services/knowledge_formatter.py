from datetime import datetime

# class KnowledgeFormatter:

#     def __init__(self):
#         pass

#     def format(self, repository, knowledge):

#         formatted = {
#             "repository_name": repository.get("name", ""),
#             "repository_description": repository.get("description", ""),
#             "generated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             "feature_name": knowledge.get("feature_name", ""),
#             "business_functionality": knowledge.get("business_functionality", ""),
#             "problem_solved": knowledge.get("problem_solved", ""),
#             "technical_summary": knowledge.get("technical_summary", ""),
#             "knowledge_transfer": knowledge.get("knowledge_transfer", ""),
#             "technologies": knowledge.get("technologies", []),
#             "frameworks": knowledge.get("frameworks", []),
#             "files_modified": knowledge.get("files_modified", []),
#             "classes": knowledge.get("classes", []),
#             "methods": knowledge.get("methods", []),
#             "apis": knowledge.get("apis", []),
#             "database_changes": knowledge.get("database_changes", []),
#             "security_changes": knowledge.get("security_changes", []),
#             "configuration_changes": knowledge.get("configuration_changes", []),
#             "dependencies": knowledge.get("dependencies", []),
#             "impact": knowledge.get("impact", ""),
#             "learning_points": knowledge.get("learning_points", []),
#         }

#         return formatted


class KnowledgeFormatter:

    def __init__(self):
        pass

    def format(self, knowledge):

        return {
            "organization_summary": knowledge.get("organization_summary", ""),
            "repositories": knowledge.get("repositories", []),
            "business_domains": knowledge.get("business_domains", []),
            "major_features": knowledge.get("major_features", []),
            "functional_modules": knowledge.get("functional_modules", []),
            "technologies": knowledge.get("technologies", []),
            "frameworks": knowledge.get("frameworks", []),
            "libraries": knowledge.get("libraries", []),
            "apis": knowledge.get("apis", []),
            "database": knowledge.get("database", []),
            "security": knowledge.get("security", []),
            "configuration": knowledge.get("configuration", []),
            "important_classes": knowledge.get("important_classes", []),
            "important_methods": knowledge.get("important_methods", []),
            "important_files": knowledge.get("important_files", []),
            "development_timeline": knowledge.get("development_timeline", ""),
            "bug_fixes": knowledge.get("bug_fixes", []),
            "enhancements": knowledge.get("enhancements", []),
            "knowledge_transfer": knowledge.get("knowledge_transfer", ""),
            "learning_points": knowledge.get("learning_points", []),
        }
