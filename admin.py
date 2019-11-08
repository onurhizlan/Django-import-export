# -*- coding: utf-8 -*-

from django.contrib import admin
from import_export.fields import Field
from modules.orders.models import Orders
from import_export.admin import ImportExportModelAdmin
from core.modules.orders.views import GetPickleLoad


class OrdersResource(resources.ModelResource):
    OrderCode = Field(attribute='OrderCode', column_name='Sipariş Kodu')
    full_name = Field(column_name='Ad - Soyad')
    calculate_money = Field(column_name='Toplam Ücret')
    choice_list = Field(column_name='Ödeme Şekli')
    shipping_address = Field(column_name='Teslimat Adresi')
    ShippingCityCountry = Field(attribute='ShippingCityCountry', column_name='Teslimat Şehir / Ülke')
    invoice_address = Field(column_name='Fatura Adresi')
    InvoiceCityCountry = Field(attribute='InvoiceCityCountry', column_name='Fatura Şehir / Ülke')
    ShippingCorp = Field(attribute='ShippingCorp', column_name='Kargo Firması')
    ShippingNo = Field(attribute='ShippingNo', column_name='Kargo Sipariş Numarası')
    CreateDate = Field(attribute='CreateDate', column_name='Oluşturma Tarihi')
    LastUpdateDate = Field(attribute='LastUpdateDate', column_name='Güncelleme Tarihi')
    status_list = Field(column_name='Durumu')
    Supplier = Field(attribute='Supplier', column_name="Tedarikçi")

    class Meta:
        model = Orders
        fields = ('',)

    def dehydrate_calculate_money(self, order):
        x = format(order.TotalPrice, '.2f')
        return x

    def dehydrate_full_name(self, order):
        user = User.objects.get(username=order.AuthorUser)
        return '%s %s' % (user.first_name, user.last_name)

    def dehydrate_shipping_address(self, order):
        order = GetPickleLoad(order.ShippingAddres)
        orderShippingAddres = order.get('Address')
        return orderShippingAddres

    def dehydrate_invoice_address(self, order):
        order = GetPickleLoad(order.InvoiceAddres)
        orderInvoiceAddres = order.get('Address')
        return orderInvoiceAddres

    def dehydrate_choice_list(self, order):
        if order.PaymentMethod == 'ccpay':
            return 'kredi kartı'
        elif order.PaymentMethod == 'transfer':
            return 'EFT/Havale'
        elif order.PaymentMethod == 'cash':
            return 'Nakit'
        elif order.PaymentMethod == 'cash-cargo':
            return 'Kapıda Nakit Ödeme'
        elif order.PaymentMethod == 'cc-cargo':
            return 'Kapıda Kartlı Ödeme'
        elif order.PaymentMethod == 'paypal':
            return 'PayPal'
        elif order.PaymentMethod == 'other':
            return 'Diğer'
        elif order.PaymentMethod == 'offline-payment':
            return 'Offline Ödeme'
        elif order.PaymentMethod == 'point-paymenr':
            return "Puan Alımı"
        else:
            return 'Bonus Pay'

    def dehydrate_status_list(self, order):
        if order.Status == 'pending':
            return 'Beklemede'
        elif order.Status == 'pendingpayment':
            return 'Ödeme Bekliyor'
        elif order.Status == 'approved':
            return 'Onaylandı'
        elif order.Status == 'pending-supplier':
            return 'Ürün Tedarikçiden Beklemede'
        elif order.Status == 'preparing':
            return 'Hazırlanıyor'
        elif order.Status == 'submitted':
            return 'Kargoya verildi'
        elif order.Status == 'magazaprepare':
            return 'Mağazadan sevk bekliyor'
        elif order.Status == 'delivered':
            return 'Teslim edildi'
        elif order.PaymentMethod == 'denied':
            return "Reddedildi"
        else:
            return 'İptal Edildi'



class OrdersAdmin(ImportExportModelAdmin):

    resource_class = OrdersResource
    

admin.site.register(Orders, OrdersAdmin)

