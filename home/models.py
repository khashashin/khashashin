from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Profile Image'
    )
    text_under_image = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Write an introduction for the bakery'
        )

    github_section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )

    github_section = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='GitHub Graph section. Will display GraphQL graphic',
        verbose_name='GitHub Graphic'
    )

    twitter_section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )

    twitter_section = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Twitter section. Will display GraphQL graphic',
        verbose_name='Recently twitts'
    )

    contact_section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )

    contact_section = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Contact links section. Will display social links',
        verbose_name='Social Links'
    )

    blog_section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )

    blog_section = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Blog section. Will display social links',
        verbose_name='Blog Posts'
    )
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('image'),
            FieldPanel('text_under_image', classname="full"),
            ], heading="Profile Section"),
        MultiFieldPanel([
            MultiFieldPanel([
                FieldPanel('github_section_title'),
                PageChooserPanel('github_section'),
                ], heading="GitHub Graphics"),
            MultiFieldPanel([
                FieldPanel('twitter_section_title'),
                PageChooserPanel('twitter_section'),
                ], heading="Twitter"),
            MultiFieldPanel([
                FieldPanel('contact_section_title'),
                PageChooserPanel('contact_section'),
                ], heading="Social Links"),
            MultiFieldPanel([
                FieldPanel('blog_section_title'),
                PageChooserPanel('blog_section'),
                ], heading="Blog posts")
        ], heading="Featured homepage sections", classname="collapsible")
    ]

    def __str__(self):
        return self.title
