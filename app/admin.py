from django.contrib import admin
from .models import AudioFile
import os

class AudioFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tags', 'parse', 'upload_at', 'audio_file')

    ordering = ('id', )
    actions = ['custom_delete_selected']
    
    def custom_delete_selected(self, request, queryset):
        #custom delete code
        n = queryset.count()
        for i in queryset:
            if i.audio_file:
                if os.path.exists(i.audio_file.path):
                    os.remove(i.audio_file.path)
            i.delete()
        self.message_user(request, ("Successfully deleted %d audio files.") % n)
    custom_delete_selected.short_description = "Delete selected items"
    
    def get_actions(self, request):
        actions = super(AudioFileAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

admin.site.register(AudioFile, AudioFileAdmin)
