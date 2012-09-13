from django.contrib import admin

from mtta.models import (
    SignUp, Line, LineDirection, Pattern, Stop, Node, StopByLine,
    StopByPattern, Service, TripDay, TripStop, Trip, TripTime)


# TODO: add fields so that sorting follows model
# TODO: Restrict lookups so that non-readonly dropdowns might be performant
# TODO: Even more useful names

class LineAdmin(admin.ModelAdmin):
    raw_id_fields = ('signup',)


class LineDirectionAdmin(admin.ModelAdmin):
    raw_id_fields = ('line',)


class NodeAdmin(admin.ModelAdmin):
    raw_id_fields = ('stop',)


class PatternAdmin(admin.ModelAdmin):
    raw_id_fields = ('linedir',)
    read_only_fields = ('raw_pattern', 'fixed_pattern')


class ServiceAdmin(admin.ModelAdmin):
    raw_id_fields = ('signup',)
 

class StopAdmin(admin.ModelAdmin):
    raw_id_fields = ('signup',)


class StopByLineAdmin(admin.ModelAdmin):
    raw_id_fields = ('stop', 'linedir', 'node')


class StopByPatternAdmin(admin.ModelAdmin):
    raw_id_fields = ('stop', 'linedir', 'pattern', 'node')


class TripDayAdmin(admin.ModelAdmin):
    raw_id_fields = ('linedir', 'service')


class TripStopAdmin(admin.ModelAdmin):
    raw_id_fields = ('tripday', 'stop', 'node')


class TripTimeAdmin(admin.ModelAdmin):
    raw_id_fields = ('trip', 'tripstop')


class TripAdmin(admin.ModelAdmin):
    raw_id_fields = ('tripday', 'pattern')


admin.site.register(Line, LineAdmin)
admin.site.register(LineDirection, LineDirectionAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Pattern, PatternAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(SignUp)
admin.site.register(Stop, StopAdmin)
admin.site.register(StopByLine, StopByLineAdmin)
admin.site.register(StopByPattern, StopByPatternAdmin)
admin.site.register(TripDay, TripDayAdmin)
admin.site.register(TripStop, TripStopAdmin)
admin.site.register(Trip, TripAdmin)
admin.site.register(TripTime, TripTimeAdmin)
