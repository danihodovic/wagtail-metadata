import jinja2
from jinja2.ext import Extension
from wagtailmetadata import tags


@jinja2.contextfunction
def meta_tags(context, model_name):
    request = context['request']
    if model_name:
        page = context[model_name]
    else:
        page = context['self']

    return jinja2.Markup(tags.meta_tags(request, page))


class WagtailMetadataExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)

        self.environment.globals.update({
            'meta_tags': meta_tags,
        })
