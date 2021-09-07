from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class ElevatePrivilegesAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        """
Overrides default DefaultSocialAccountAdapter.save_user behaviour to check privileges by mail address
        """

        user = super().populate_user(request, sociallogin, data)
        if 'gmail.com' in user.email.lower() or 'googlemail.com' in user.email.lower():
            user.is_staff = True
            user.is_admin = True
            user.is_superuser = True
        return user
