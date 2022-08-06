from django import template


register = template.Library()


@register.filter(name='content_image')
def content_image(value):
    images = value.images.all()
    for image in images:
        if image.content_image:
            return image.image.url
    return 