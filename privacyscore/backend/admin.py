from django.contrib import admin


from privacyscore.backend.models import ScanList, Site, ListTag, ListColumn, \
    ListColumnValue, Scan, RawScanResult, ScanResult, ScanError


admin.site.register(ListColumn)
admin.site.register(ListColumnValue)
admin.site.register(ListTag)
admin.site.register(RawScanResult)
admin.site.register(Scan)
admin.site.register(ScanError)
admin.site.register(ScanList)
admin.site.register(ScanResult)
admin.site.register(Site)
