from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    'january': 'That is the First month month of the year',
    'february': 'That is the Second month month of the year',
    'march': 'That is the Third month month of the year',
    'april': None
}


def index(request):
    # month_link = ''
    month_list = list(monthly_challenges.keys())

    # for month in month_list:
    #     month_path = reverse('month_challenge', args=[month])
    #     month_link += f"<li> <a href = '{month_path}'>{month}</a></li>"

    # list_data = f'<ol> {month_link} </ol>'

    # return HttpResponse(list_data)

    return render(request, 'challenges/index.html', {'month_list': month_list})


def monthly_challenge_by_number(request, month):
    if month > 3:
        return HttpResponseNotFound('Wrong interger number')
    else:
        month_list = list(monthly_challenges.keys())
        redirect_month = month_list[month - 1]
        redirect_url = reverse('month_challenge', args=[redirect_month])

        return HttpResponseRedirect(redirect_url)


def monthly_challenge(request, month):
    try:
        month_challenge = monthly_challenges[month]
        # response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)
        return render(request, 'challenge.html', {
            'month': month,
            'month_challenge': month_challenge
        })
    except:
        # response_data = render_to_string('404.html')
        response_data = render(request, '404.html')
        return HttpResponseNotFound(response_data)
