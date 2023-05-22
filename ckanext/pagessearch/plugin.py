import ckan.plugins as plugin
import ckan.plugins.toolkit as tk

from ckanext.pagessearch.blueprint import pages

class PagesSearch(plugin.SingletonPlugin):

    plugin.implements(plugin.IBlueprint)
    plugin.implements(plugin.IConfigurer)
    
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
