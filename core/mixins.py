from django.shortcuts import redirect


class IsSuperUserMixin(object):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('DashboardIndexView')
