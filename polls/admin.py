from django.contrib import admin

# Register your models here.
from .models import Question,Choice

# StackedInline - Choices are stacked (Separate fieldsets)
# TabularInline - Choices are displayed in tables
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
	# Search bar
	search_fields = ['question_text']
	# Filter section
	list_filter = ['pub_date']
	# Fields and their order to be displayed
	list_display = ('question_text', 'pub_date', 'was_published_recently');
	fieldsets = [
	    (None,               {'fields': ['question_text']}),
	    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	# Display choices for each Question in that Question's page
	inlines = [ChoiceInline]

# This format is used for a custom admin model
# Registering a model using default admin model - admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
