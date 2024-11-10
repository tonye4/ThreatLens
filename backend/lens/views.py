from django.shortcuts import render
from django.http import HttpResponse


from django.http import JsonResponse
from threat.TiktokComments.hackTrent.modelv2 import comments_analysis, get_reputation_score
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(request):
    return render(request, 'lens/dashboard.html')

@csrf_exempt
def reputation_score_view(request):
    json_path = '/Users/aadit/Documents/GitHub/ThreatLens/backend/threat/TiktokComments/hackTrent/comments.json'
    print(request)
    analyzed_comments = comments_analysis(json_path)

    reputation_scores = get_reputation_score(analyzed_comments)

    return JsonResponse(reputation_scores, safe=False)


