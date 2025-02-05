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
                    'Date': form.cleaned_data.get('date', ).strftime('%d %b %Y, %H:%M'),
                    'How Much': form.cleaned_data['howmuch'],
                    'Who': form.cleaned_data['who'],
                    'Paid To': form.cleaned_data['paidto']
                }
                payers_dict = {"Shyam":0, "Balwan":0, "Rajender":0, "Pawan":0}
                for i in payers_dict.keys():
                    if i == data['Who']:
                        payers_dict.update({i:data['How Much']})
                ingest_data = payers_dict.values()
                ingest_data.insert(0,data['Date'])        
                gs = GoogleSheetsAutomation()
                ws = gs.select_worksheet(sheet_name="MasterSheet", worksheet_index=2)
                gs.insert_values(sheet = ws, append_row= list(ingest_data.values()))
                random_quote = RandomQuote().get_random_quote()
                return render(request, 'BudgetManagerAppTemplates/Success.html', {'random_quote': random_quote})
            except Exception as e:
                return render(request, 'MasterTemplates/ErrorPage.html', {'error_message': str(e)})
    else:
        form = FinanceForm()
    return render(request, 'BudgetManagerAppTemplates/Index.html', {'form': form})
