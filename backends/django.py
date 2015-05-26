from django.template import TemplateDoesNotExist
from django.template import TemplateSyntaxError
from django.template.backends.base import BaseEngine
from django.template.backends.utils import csrf_input_lazy
from django.template.backends.utils import csrf_token_lazy
from webpages import templates


class WebPagesTemplates(BaseEngine):
    '''
    Backend for Django framework.

    Allow to use WebPages Temlates system inside Django 1.8+ projects.

    Add this code to your settings.py in Django project:
        TEMPLATES = [
            {
                'BACKEND': 'webpages.templates.backends.django.WebPagesTemplates',
                'DIRS': [
                    # replace to path to your project
                    '/home/projects/example.com',
                ],
            },
        ]

    See also: https://docs.djangoproject.com/en/1.8/topics/templates/#custom-backends
    '''

    # Name of the subdirectory containing the templates for this engine
    # inside an installed application.
    app_dirname = 'webpages'

    def __init__(self, params):
        params = params.copy()
        options = params.pop('OPTIONS').copy()
        super(WebPagesTemplates, self).__init__(params)
        self.engine = templates.Engine(**options)

    def from_string(self, template_code):
        try:
            return Template(self.engine.from_string(template_code))
        except templates.TemplateCompilationFailed as exc:
            raise TemplateSyntaxError(exc.args)

    def get_template(self, template_name):
        try:
            return Template(self.engine.get_template(template_name))
        except templates.TemplateNotFound as exc:
            raise TemplateDoesNotExist(exc.args)
        except templates.TemplateCompilationFailed as exc:
            raise TemplateSyntaxError(exc.args)


class Template(object):

    def __init__(self, template):
        self.template = template

    def render(self, context=None, request=None):
        if context is None:
            context = {}
        if request is not None:
            context['request'] = request
            context['csrf_input'] = csrf_input_lazy(request)
            context['csrf_token'] = csrf_token_lazy(request)
        return self.template.render(context)
