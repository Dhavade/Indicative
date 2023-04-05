from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
#from webapp.models import Csv
# Register your models here.

#admin.site.register(Csv)

# Register your models here.
from members.models import Member,Person1

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Member,AuthorAdmin)

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Person1,AuthorAdmin)


'''class BrandAdmin(ImportExportModelAdmin):
    pass
admin.site.register(Productfield,BrandAdmin)'''

'''@admin.register(Productfield)
class ProductBrande_Resources(ImportExportModelAdmin):
    list_display=('Coupon_Rate',"ISIN",'Name_of_the_security','CATEGORY','Rating_Agency','Maturity_Date','IP_Dates','Put_Call_Option','Price_Per_100','YTM','YTC_YTP','Face_Value','Quantum')

    class meta:
        model=Productfield'''