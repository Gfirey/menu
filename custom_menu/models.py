from django.db import models


class NodeModel(models.Model):
    title = models.CharField(max_length=80)
    parent = models.ForeignKey('self', verbose_name='parent', blank=True, null=True)
    url = models.CharField('additional url (without "/")', max_length=200, blank=False)
    level = models.IntegerField(default=0, editable=False)
    menu = models.ForeignKey('Menu', related_name='contained_items', verbose_name='menu', null=True, blank=True, editable=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.caption

    def save(self, force_insert=False, **kwargs):
        if not self.pk:
            self.url = ''.join([self.get_parent_url(), self.url, '/'])

        super(NodeModel, self).save(force_insert, **kwargs)

    def delete(self, using=None):
        super(NodeModel, self).delete()

    def siblings(self):
        if not self.parent:
            return NodeModel.objects.none()
        else:
            if not self.pk:  # If does not have a pk / not saved
                return self.parent.children()
            else:
                return self.parent.children().exclude(pk=self.pk)

    def has_siblings(self):
        return self.siblings().count() > 0

    def children(self):
        children = NodeModel.objects.filter(parent=self)
        for child in children:
            child.parent = self  # less db queries
        return children

    def has_children(self):
        return self.children().count() > 0

    def caption_with_spacer(self):  # beautiful realisation from treemenus
        spacer = ''
        for i in range(0, self.level):
            spacer += '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        if self.level > 0:
            spacer += '|-&nbsp;'
        return '%s%s' % (spacer, self.caption)

    def get_parent_url(self):
        if not self.parent:
            return NodeModel.objects.none()
        else:
            return self.parent.url


class Menu(models.Model):
    name = models.CharField(max_length=80)
    root_item = models.ForeignKey(NodeModel, related_name='root_item', verbose_name='root item', null=True, blank=True, editable=False)

    def save(self, force_insert=False, **kwargs):
        if not self.root_item:
            root_item = NodeModel()
            root_item.caption = 'root'
            if not self.pk:
                super(Menu, self).save(force_insert, **kwargs)
                force_insert = False
            root_item.menu = self
            root_item.save()
            self.root_item = root_item
        super(Menu, self).save(force_insert, **kwargs)


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name