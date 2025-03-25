import ckan.plugins as plugin
import ckan.plugins.toolkit as tk
from ckanext.pagessearch.actions import get_recent_resources

from ckanext.pagessearch.blueprint import pages

class PagesSearch(plugin.SingletonPlugin):

    plugin.implements(plugin.IBlueprint)
    plugin.implements(plugin.IConfigurer)
    plugin.implements(plugin.IActions)
    plugin.implements(plugin.ITemplateHelpers)
    
    def get_blueprint(self):
        
        """
        Get the new pages blueprint and load it
        """

        return pages
    
    def update_config(self, config):

        """
        Add templates to plugin
        """

        tk.add_template_directory(config, "templates")

    def get_actions(self):
        """
        Get actions for the citations
        """
        
        return {"get_recent_resources": get_recent_resources}
    
    def list_recent_resources(self):

        return get_recent_resources(None, {})
    
    def get_helpers(self):

        return {"get_recent_resources": self.list_recent_resources}
