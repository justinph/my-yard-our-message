from django.db.models.fields import ImageField
from utils import make_thumbnail, _remove_thumbnails, remove_model_thumbnails, rename_by_field
from django.dispatch import dispatcher
from django.db.models import signals

def _delete(instance=None):
    if instance:
        print '[thumbnail] DELETE', instance
        remove_model_thumbnails(instance)
#

class ImageWithThumbnailField(ImageField):
    """ ImageField with thumbnail support
    
        auto_rename: if it is set perform auto rename to
        <class name>-<field name>-<object pk>.<ext>
        on pre_save.
    """

    def __init__(self, verbose_name=None, name=None, width_field=None, height_field=None, auto_rename=True, **kwargs):
        self.width_field, self.height_field = width_field, height_field
        super(ImageWithThumbnailField, self).__init__(verbose_name, name, width_field, height_field, **kwargs)
        self.auto_rename = auto_rename
    #
    
    def _save(self, instance=None):
        if not self.auto_rename: return
        image = getattr(instance, self.attname)
        import md5, time
        m = md5.new()
        m.update(image)
        m.update(str(time.time()))
        theUID = m.hexdigest()
      
        # MODIFIED BY JUSTIN HEIDEMAN, TO GENERATE TOTALLY UNIQUE NAMES
        # XXX this needs testing, maybe it can generate too long image names (max is 100)
        image = rename_by_field(image, '%s-%s' \
                                     % ( self.name,
                                         theUID
                                        )
                                   )
        print image
        setattr(instance, self.attname, image)
        print instance._get_pk_val()
    #
    
    def contribute_to_class(self, cls, name):
        super(ImageWithThumbnailField, self).contribute_to_class(cls, name)
        dispatcher.connect(_delete, signals.post_delete, sender=cls)
        dispatcher.connect(self._save, signals.pre_save, sender=cls)
    #

    def get_internal_type(self):
        return 'ImageField'
    #
#
