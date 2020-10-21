from time import time

from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


def generate_slug(title):
    new_slug = slugify(title, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class TimeStampedModele(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class Post(TimeStampedModele):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    body = models.TextField(max_length=150, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Tag(TimeStampedModele):
    tag = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, unique=True)

    class Meta(TimeStampedModele.Meta):
        ordering = ['-tag']

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})
