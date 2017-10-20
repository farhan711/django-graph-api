
### Install 

    pip install -r requirements.txt

### Introducing Graph API

In the newest version of the Graph API, introducing new Pages features, requiring access tokens in more places and improving the behavior of Open Graph objects.


### URL API Changes

Website owners may update Open Graph objects but are limited in how frequently they may do so. Previously, GET /{url} would trigger a scrape if that URL had not been encountered before. With v2.10, these requests will not trigger a scrape nor an update to the Open Graph object. This means that API callers are less likely to be rate limited when they intentionally update Open Graph objects.

When making a GET request against a URL we haven't scraped before, we will also omit the og_object field. To trigger a scrape and populate the og_object, issue a POST /{url}?scrape=true. Once scraped, the og_object will remain cached and returned on all future read requests
