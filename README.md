# PagesSearch
Adds a page to allow users to search through pages added with the ckanext-pages extension.
NOTE: currently this only works for pages and not for blogs

## Requirements
python3

ckan >= 2.10

ckanext-sitesearch

ckanext-pages

## Installation

1. Activate CKAN virtual enviornment (default location in source install)
```
source /usr/lib/ckan/default/bin/activate
```
2. Clone git repo
```
git clone https://github.com/Drexel-UHC/ckanext-pagessearch.git
```
3. Install package and depdendencies
```
pip install ckanext-pagesearch
pip install ckanext-pagessearch/requirements.txt
```
4. Add pagessearch to ckan.plugins in ckan.ini
5. Restart ckan

## Configuration Options

ckanext.pagessearch.type_name  (default: "page"): name of page type. Displays in the query results string on top of page, e.g. "2 {type_name}s found"

ckanext.pagessearch.pages_search_url (default: "/pages_search"): the endpoint where the search page will be added
