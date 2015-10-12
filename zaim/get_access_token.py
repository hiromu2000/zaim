# coding: utf-8
import os
import zaim
import six
from builtins import input

def main():
    consumer_key = os.environ.get("ZAIM_CONSUMER_KEY", "")
    consumer_secret = os.environ.get("ZAIM_CONSUMER_SECRET", "")
    callback_uri = os.environ.get("ZAIM_CALLBACK_URI", "")
    assert consumer_key, 'Please set "ZAIM_CONSUMER_KEY".'
    assert consumer_secret, 'Please set "ZAIM_CONSUMER_SECRET".'
    assert callback_uri, 'Please set "ZAIM_CALLBACK_URI".'
    api = zaim.Api(consumer_key, consumer_secret)

    authorize_url = api.get_authorize_url(callback_uri)
    six.print_("AUTHORIZE_URL:", authorize_url)
    six.print_("Please visit AUTHORIZE_URL w/ your browser, and login w/ your Zaim credentials.")
    six.print_("When redirected to your callback URI, find the oauth_verifier in the address bar.")
    oauth_verifier = input("oauth_verifier? : ")
    six.print_("OAUTH_VERIFIER:", oauth_verifier)
    access_token = api.get_access_token(oauth_verifier)
    six.print_("ACCESS_TOKEN:", access_token)

if __name__ == '__main__':
   main() 
