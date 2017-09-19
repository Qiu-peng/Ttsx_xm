from django.shortcuts import redirect


def is_login(fn):
    def fun2(request, *args, **kwargs):
        if 'uid' in request.session:
            return fn(request, *args, **kwargs)
        else:
            return redirect('/User/login/')
    return fun2

