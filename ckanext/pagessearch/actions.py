import ckan.plugins as p
from ckanext.pages.utils import pages_show, pages_list_pages



@p.toolkit.side_effect_free
def get_recent_resources(context, data_dict):

    return_limit = p.toolkit.config.get("ckanext.pagessearch.recent_limit", 3)

    data_dict['order_publish_date'] = True
    data_dict['page_type'] = "page"

    pages = p.toolkit.g.pages_dict = p.toolkit.get_action('ckanext_pages_list')(
        context={}, data_dict=data_dict
    )

    print(pages)
    print(pages[0])

    return pages[:return_limit]


    # return pages_list_pages("pages")