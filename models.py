
class Orders(models.Model):
    OrderCode = models.CharField(max_length=25, verbose_name="Sipariş Kodu")
    AuthorUser = models.CharField(max_length=30, verbose_name="Siparişi Oluşturan")
    PaymentMethod = models.CharField(max_length=150, choices=PAYMENTMETHODMODUL, verbose_name="Ödeme Şekli")
    TotalPrice = models.DecimalField(default=0, max_digits=10, decimal_places=4, verbose_name="Genel Sipariş Tutarı")
    ShippingAddres = models.BinaryField(blank=True, null=True, verbose_name="Teslimat Adresi")
    ShippingCityCountry = models.CharField(max_length=150, verbose_name="Teslimat Şehir / Ülke")
    InvoiceAddres = models.BinaryField(blank=True, null=True, verbose_name="Fatura Adresi")
    InvoiceCityCountry = models.CharField(max_length=150, verbose_name="Fatura Şehir / Ülke")
    ShippingCorp = models.CharField(max_length=150, verbose_name="Kargo Firması")
-    ShippingNo = models.CharField(blank=True, null=True, max_length=250, verbose_name="Kargo Sipariş Numarası")
    CreateDate = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    LastUpdateDate = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")
    Status = models.CharField(max_length=25, choices=ORDERSTATUSLIST, verbose_name="Durumu")
    Supplier = models.ForeignKey(Supplier, related_name='order', null=True, blank=True, verbose_name='Tedarikçi')

    class Meta:
        verbose_name_plural = u'Siparişler'
        verbose_name = u'Sipariş'
        ordering = ['-CreateDate']
        app_label = string_with_title("orders", _(u"Siparişler"))

    def __unicode__(self):
        return self.OrderCode

