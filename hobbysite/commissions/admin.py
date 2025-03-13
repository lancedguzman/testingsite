from django.contrib import admin
from .models import Commission, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  
    readonly_fields = ("created_on", "updated_on") 

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    list_display = ("title", "people_required", "created_on", "updated_on") 
    search_fields = ("title", "description")  
    list_filter = ("created_on", "updated_on") 
    inlines = [CommentInline] 

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ("commission", "entry", "created_on", "updated_on") 
    search_fields = ("commission__title", "entry") 
    list_filter = ("created_on", "updated_on", "commission") 

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)