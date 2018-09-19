from behave import given, when, then
from Common.commonFunc import WebCommon


@given ('i go to the site {url}')
def go_to_url(context, url):

    print("Navigating to the site: {}".format(url))

    context.driver = WebCommon.go_to(url)


