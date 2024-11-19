from datetime import datetime
from .forms import FinanceForm
from django.conf import settings
from django.shortcuts import render
from Scripts.Quotes import RandomQuote
from Scripts.GoogleSheetAutomation import GoogleSheetsAutomation


def log_view(request):
    if request.method == "POST":
        form = FinanceForm(request.POST)
        if form.is_valid():
            try:
                data = {
                    'DateTime': form.cleaned_data.get('date', ).strftime('%d %b %Y, %H:%M'),
                    'How Much': form.cleaned_data['howmuch'],
                    'Why': form.cleaned_data['why'],
                    'Mode of Payment': form.cleaned_data['mode']
                }
                gs = GoogleSheetsAutomation()
                ws = gs.select_worksheet(sheet_name="DailyExpenseTracker", worksheet_index=0)
                gs.insert_values(sheet = ws, append_row= list(data.values()))
                random_quote = RandomQuote().get_random_quote()
                return render(request, 'BudgetManagerAppTemplates/Success.html', {'random_quote': random_quote})
            except Exception as e:
                return render(request, 'MasterTemplates/ErrorPage.html', {'error_message': str(e)})
    else:
        form = FinanceForm()
    return render(request, 'BudgetManagerAppTemplates/Index.html', {'form': form})
