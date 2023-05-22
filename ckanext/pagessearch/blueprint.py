from __future__ import annotations

import ckan.plugins as p
import ckan.plugins.toolkit as tk
import ckan.logic as logic
import ckan.lib.helpers as helpers

from ckanext.pages.blueprint import pages
import ckanext.pages.utils as pages_utils

def search_pages(page_type: str):
    """
    page_type: blog or page, dermines which type of page is displayed
    """

    item_limit = tk.config.get('ckanext.pagessearch.item_limit', 10)
      
    # if type is blog, use the default function from ckanext-pages
    if page_type == "blog":
        pages_utils.pages_list_pages(page_type)

    # collect the query variabels from the requests
    extra_vars = {}
    extra_vars["dataset_type"] = tk.config.get("ckanext.pagessearch.type_name", page_type)
    extra_vars['q'] = q = tk.request.args.get('q', '')
    extra_vars['sort_by_selected'] = extra_vars['sorting'] = sorting = tk.request.args.get('sort', '')
    page = int(tk.request.args.get("page", 1))

    # put variables in a format that can be passed to the page_search action
    query_dict: dict[str, Any] = {
        "q": q,
        "rows": item_limit,
        "start": (page-1) * item_limit,
        "sort": sorting
    }

    # get response object from API call
    tk.g.pages_dict = tk.get_action("page_search")(context={}, data_dict=query_dict)

    # ceate the page variable to pass into the template
    tk.g.page = helpers.Page(
        collection=tk.g.pages_dict["results"],
        page=page,
        url=helpers.pager_url,
        items_per_page=10,
        item_count=tk.g.pages_dict["count"]
    )

    # get the items that the API call returned
    tk.g.page.items = tk.g.pages_dict["results"]

    # pass everythying to the template and render
    return tk.render("pages_list_search.html", extra_vars)

def index():
    
    return search_pages("page")


pages.add_url_rule(tk.config.get("ckanext.pagessearch.pages_search_url", "/pages_search"), view_func=index, endpoint="pages_index_new")