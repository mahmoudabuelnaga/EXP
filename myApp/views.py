from django.shortcuts import render
from .models import EXP_Report

def pie_chart(request):
    labels = []
    data = []

    queryset = EXP_Report.objects.all()
    for q in queryset:
        labels.append(q.SM_NAME)
        data.append(q.TOTALPRICE)

    return render(request, 'index.html', {
        'labels': labels,
        'data': data,
    })