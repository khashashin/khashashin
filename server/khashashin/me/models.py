from django.db import models


class Me(models.Model):

    first_name = models.CharField(max_length=500, default='', blank=True)
    last_name = models.CharField(max_length=500, default='', blank=True)

    # Profile Picture
    img_width = models.SmallIntegerField(default=250, blank=True)
    img_height = models.SmallIntegerField(default=250, blank=True)
    tmb_width = models.SmallIntegerField(default=250, blank=True)
    tmb_height = models.SmallIntegerField(default=250, blank=True)
    image = models.ImageField(width_field=img_width,
                              height_field=img_height, blank=True)
    tmb_image = models.ImageField(
        width_field=tmb_width, height_field=tmb_height, blank=True)

    slogan = models.CharField(max_length=500, default='', blank=True)

    title = models.CharField(max_length=500, default='', blank=True)

    about = models.TextField(default='', blank=True)

    phone_number = models.CharField(max_length=500, default='', blank=True)
    email = models.EmailField(default='', blank=True)
    website = models.CharField(max_length=500, default='', blank=True)
    # Address
    street = models.CharField(max_length=500, default='', blank=True)
    street_number = models.SmallIntegerField(default=0, blank=True)
    state = models.CharField(max_length=500, default='', blank=True)
    land = models.CharField(max_length=500, default='', blank=True)
    zip = models.SmallIntegerField(default=0000, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Me"
        verbose_name_plural = "Me"


class SocialAccounts(models.Model):
    platform = models.CharField(max_length=500, default='', blank=True)
    url = models.CharField(max_length=500, default='', blank=True)
    icon = models.ImageField(blank=True)
    user = models.ForeignKey(Me, on_delete=models.CASCADE,
                             blank=True, null=True, related_name='social_accounts')

    def __str__(self):
        return self.platform

    class Meta:
        verbose_name = "Social Account"
        verbose_name_plural = "Social Accounts"


class Work(models.Model):
    title = models.CharField(max_length=500, default='', blank=True)
    company = models.CharField(max_length=500, default='', blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    is_current = models.BooleanField(blank=True)
    conclusion = models.TextField(default='', blank=True)

    doc1 = models.FileField(blank=True)
    doc2 = models.FileField(blank=True)
    doc3 = models.FileField(blank=True)
    user = models.ForeignKey(Me, on_delete=models.CASCADE,
                             blank=True, null=True, related_name='work')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "Work"


class Education(models.Model):
    title = models.CharField(max_length=500, default='', blank=True)
    university = models.CharField(max_length=500, default='', blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    is_current = models.BooleanField(blank=True)
    conclusion = models.TextField(default='', blank=True)

    doc1 = models.FileField(blank=True)
    doc2 = models.FileField(blank=True)
    doc3 = models.FileField(blank=True)
    user = models.ForeignKey(Me, on_delete=models.CASCADE,
                             blank=True, null=True, related_name='education')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"


class Skills(models.Model):
    scope = models.CharField(max_length=500, default='', blank=True)
    percentage = models.SmallIntegerField(default=100, blank=True)

    doc1 = models.FileField(blank=True)
    doc2 = models.FileField(blank=True)
    doc3 = models.FileField(blank=True)
    user = models.ForeignKey(Me, on_delete=models.CASCADE,
                             blank=True, null=True, related_name='skills')


class Projects(models.Model):
    title = models.CharField(max_length=500, default='', blank=True)
    subtitle = models.CharField(max_length=500, default='', blank=True)

    img_width = models.SmallIntegerField(default=250, blank=True)
    img_height = models.SmallIntegerField(default=250, blank=True)
    tmb_width = models.SmallIntegerField(default=250, blank=True)
    tmb_height = models.SmallIntegerField(default=250, blank=True)
    image = models.ImageField(width_field=img_width,
                              height_field=img_height, blank=True)
    tmb_image = models.ImageField(
        width_field=tmb_width, height_field=tmb_height, blank=True)
    user = models.ForeignKey(Me, on_delete=models.CASCADE,
                             blank=True, null=True, related_name='projects')


class ContactMessages(models.Model):
    name = models.CharField(max_length=500, default='', blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField(default='', blank=True)
