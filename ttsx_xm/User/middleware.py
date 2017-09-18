



class GetPathMiddleware():
    def process_view(self, request, view_func, view_args, view_kwargs):
        #active
        no_urls = [
            '/User/register/',
            '/User/regist/',
            '/User/ishere/',
            '/User/login/',
            '/User/toLogin/',
            '/User/login_out/',
            '/User/toindex/',
            '/User/readName/',
            '/User/remember/',
            '/User/clearSession/',
            '/User/verify_code/',
            '/User/yzm/',
        ]
        # if request.path not in no_urls and 'active' not in request.path:
        if request.path not in no_urls:
            request.session['url_path'] = request.get_full_path()
