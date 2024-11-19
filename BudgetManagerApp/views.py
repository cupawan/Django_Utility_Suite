from datetime import datetime
from .forms import FinanceForm
from django.conf import settings
from django.shortcuts import render
from Scripts.Quotes import RandomQuote
from Scripts.MongoDbUtils import MongoUtils
from Scripts.GoogleSheetAutomation import GoogleSheetsAutomation


def log_view(request):
    if request.method == "POST":
        form = FinanceForm(request.POST)
        if form.is_valid():
            try:
                mongo_instance = MongoUtils()
                data = {
                    'DateTime': form.cleaned_data.get('date', ).strftime('%d %b %Y, %H:%M'),
                    'How Much': form.cleaned_data['howmuch'],
                    'Why': form.cleaned_data['why'],
                    'Mode of Payment': form.cleaned_data['mode']
                }
                gs = GoogleSheetsAutomation()
                ws = gs.select_worksheet(sheet_name="DailyExpenseTracker", worksheet_index=0)
                gs.insert_values(sheet = ws, append_row= list(data.values()))
                mongo_instance.insert_records(data=data, collection_name= "budget_manager")
                random_quote = RandomQuote().get_random_quote()
                return render(request, 'BudgetManagerAppTemplates/Success.html', {'random_quote': random_quote})
            except Exception as e:
                return render(request, 'MasterTemplates/ErrorPage.html', {'error_message': str(e)})
    else:
        form = FinanceForm()
    return render(request, 'BudgetManagerAppTemplates/Index.html', {'form': form})
