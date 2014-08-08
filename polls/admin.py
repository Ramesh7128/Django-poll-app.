from polls.models import Poll
from django.contrib import admin
from polls.models import Choice

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fieldsets = [

		(None, {'fields':['questions']}),
		('data information', {'fields':['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInLine]
	list_display = ('questions', 'pub_date', 'was_published_today')
	search_fields = ['questions']
	date_hierarchy = 'pub_date'
	list_filter = ['pub_date']

admin.site.register(Poll, PollAdmin)
