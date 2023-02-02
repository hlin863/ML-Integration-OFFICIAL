from sorl.thumbnail import ImageField, get_thumbnail

class MyPhoto(models.Model):
    image = ImageField()

    def save(self, *args, **kwargs):
        if self.image:
            self.image = get_thumbnail(self.image, '300x300', quality=99, format='JPEG')
        super(MyPhoto, self).save(*args, **kwargs)

MyPhoto(image=Image.open('my_photo.jpg')).save()