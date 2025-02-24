from ninja import Router


class MyRouter(Router):
    def api_operation(self, *a, **kw):
        kw["by_alias"] = True
        return super().api_operation(*a, **kw)
