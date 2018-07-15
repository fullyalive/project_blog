# dojo/views_cbv.py

from django.http import HttpResponse
from django.views.generic import View, TemplateView


class PostListView1(View):
    def get(self, request):
        name = '공유'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
        <h1>fullyalive</h1>
        <p>{name}</p>
        <p>hello, stragners!</p>

        <hr/>
        '''


post_list1 = PostListView1.as_view()


class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'

    # 이거 없으면 변수 호출 안됨(공유<)
    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context

post_list2 = PostListView2.as_view()


class PostListView3(object):
    pass


class ExcelDownloadView(object):
    pass
