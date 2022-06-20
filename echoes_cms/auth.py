"""This houses the adapter class that we use with allauth."""
import os

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    """Use the default social account adapter, except make is_open_for_signup
    depend on an environment variable."""
    def is_open_for_signup(self, request, sociallogin):
        """Along with this, we'll need to add an account/signup_closed.html template."""
        return bool(os.environ.get("OPEN_FOR_SIGNUP", False))
