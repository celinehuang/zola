from allauth.account.adapter import DefaultAccountAdapter


class ProfileAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.name = data.get('name')
        user.shipping_addr = data.get('shipping_addr')
        user.save()
        return user